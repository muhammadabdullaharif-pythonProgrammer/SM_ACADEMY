        function showMenu() {
            document.getElementById("navLinks").style.right = "0";
            console.log('hello World!');
        }

        function hideMenu() {
            document.getElementById("navLinks").style.right = "-200px";
        }

        function submitAdmission(event) {
            event.preventDefault();
            alert("Admission form submitted successfully!");
        }
   