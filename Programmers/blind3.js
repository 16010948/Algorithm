function solution(record) {
    var answer = [];

    let logs = [];
    let idMap = {};
    record.map(r => {
        let [command, uid, id] = r.split(' ');

        switch(command) {
            case "Enter":
                logs.push({uid, msg: "님이 들어왔습니다."});
                idMap[uid] = id;
                break;
            case "Leave":
                logs.push({uid, msg: "님이 나갔습니다."});
                break;
            case "Change":
                idMap[uid] = id;
                break;
        }
    });

    logs.map(log => answer.push(`${idMap[log.uid]}${log.msg}`));

    return answer;
}