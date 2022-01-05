const combination = (idx, menu, order, n, menus) => {
    if(menu.length > n) return -1;

    if(idx === order.length) {
        if(menu.length === n){
            menus[menu] = menus.hasOwnProperty(menu) ? menus[menu] + 1 : 1;
            return menus[menu];
        }
        return -1;
    }

    let maxOrder = 0;
    maxOrder = Math.max(maxOrder, combination(idx + 1, menu, order, n, menus));
    maxOrder = Math.max(maxOrder, combination(idx + 1, menu + order[idx], order, n, menus));

    return maxOrder;
}

function solution(orders, course) {
    var answer = [];

    course.map(n => {
        let menus = {};
        let maxOrder = 0;
        orders.map(order => {
            maxOrder = Math.max(maxOrder, combination(0, '', order.split('').sort(), n, menus));
        });
        if(maxOrder >= 2) {
            Object.keys(menus).map(menu => {
                if(menus[menu] === maxOrder) answer.push(menu)
            });
        }
    });

    return answer.sort();
}