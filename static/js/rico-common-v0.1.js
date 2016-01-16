function getQueryParams() {
    var kvs = [];

    var items = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');

    for (var i = 0; i != items.length; ++i) {
        var item = items[i].split('=');
        kvs.push(item[0]);
        kvs[item[0]] = item[1];
    }

    return kvs;
}