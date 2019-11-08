function displayData() {
    document.getElementById('data').style.display = 'block';
    document.getElementById('displayDataButton').style.display = 'none';
}

function displayName() {
    document.getElementById('nameSection').style.display = 'block';
    document.getElementById('myModal').focus();
    document.getElementById('logForm').action = '/app/signup';
}

function hideName() {
    var modal = document.getElementById('myModal');

    if (modal.style.display === 'none') {
        document.getElementById('nameSection').style.display = 'none';
        document.getElementById('logForm').action = '/app/signin';
    }
}