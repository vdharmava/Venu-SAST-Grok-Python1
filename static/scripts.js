// Vuln 54: CWE-620 - Unverified Password Change
function changePassword() {
    let newPass = document.getElementById('newPass').value;
    fetch('/change_password', {
        method: 'POST',
        body: JSON.stringify({ password: newPass })
    });
}

// Vuln 55: CWE-200 - Information Exposure
console.log("API Key: hardcoded_api_key_123");