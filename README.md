<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ATM Workflow in Python - README</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-800 p-4 sm:p-6 md:p-8 lg:p-10">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-lg p-6 sm:p-8 md:p-10">
        <!-- Title -->
        <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-6 border-b-2 border-blue-500 pb-2">
            ATM Workflow in Python
        </h1>

        <!-- Project Description -->
        <p class="text-lg mb-6 leading-relaxed">
            This project simulates a basic ATM (Automated Teller Machine) workflow using Python. It demonstrates
            fundamental concepts of object-oriented programming, file handling for data persistence (balance and
            password), and a simple command-line interface.
        </p>

        <!-- Features Section -->
        <h2 class="text-2xl sm:text-3xl font-semibold text-gray-800 mb-4 border-b border-gray-300 pb-1">
            Features
        </h2>
        <ul class="list-disc list-inside space-y-2 mb-6 ml-4 text-lg">
            <li><strong class="font-medium">Check Balance:</strong> View the current account balance.</li>
            <li><strong class="font-medium">Withdraw Money:</strong> Withdraw funds from the account, with checks for insufficient balance.</li>
            <li><strong class="font-medium">Deposit Money:</strong> Deposit funds into the account.</li>
            <li><strong class="font-medium">Reset Password:</strong> Change the ATM PIN.</li>
            <li><strong class="font-medium">Check Current Password:</strong> Display the currently set PIN.</li>
            <li><strong class="font-medium">Secure (Basic) Password Check:</strong> Requires a password to access ATM operations.</li>
        </ul>

        <!-- How to Run Section -->
        <h2 class="text-2xl sm:text-3xl font-semibold text-gray-800 mb-4 border-b border-gray-300 pb-1">
            How to Run
        </h2>
        <div class="space-y-4 mb-6">
            <p class="text-lg">1. <strong class="font-medium">Clone the repository (or download the <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">ATM.py</code> file):</strong></p>
            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto text-sm sm:text-base"><code>git clone &lt;repository-url&gt;
cd &lt;repository-directory&gt;</code></pre>
            <p class="text-base text-gray-600">
                (Replace <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">&lt;repository-url&gt;</code> and <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">&lt;repository-directory&gt;</code> with your actual repository details if you have one.)
            </p>

            <p class="text-lg">2. <strong class="font-medium">Create necessary files:</strong></p>
            <p class="text-base">
                The script uses two files for data persistence. Please create these empty files in a directory named
                <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm Management Project</code> in the same directory as <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">ATM.py</code>:
            </p>
            <ul class="list-disc list-inside space-y-1 ml-4 text-lg">
                <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm Management Project/balance.txt</code></li>
                <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm Management Project/password.txt</code></li>
            </ul>
            <p class="text-base">
                You can create these manually or use the following commands in your terminal:
            </p>
            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto text-sm sm:text-base"><code>mkdir "Atm Management Project"
touch "Atm Management Project/balance.txt"
touch "Atm Management Project/password.txt"</code></pre>

            <p class="text-lg">3. <strong class="font-medium">Run the Python script:</strong></p>
            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto text-sm sm:text-base"><code>python ATM.py</code></pre>

            <p class="text-lg">4. <strong class="font-medium">Follow the on-screen prompts:</strong></p>
            <ul class="list-disc list-inside space-y-1 ml-4 text-lg">
                <li>Enter your name.</li>
                <li>Enter your password (initially, you might need to set one by directly editing <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">password.txt</code> or using the "Reset Your PASSWORD" option after an initial run).</li>
                <li>Choose from the menu options (Check Balance, Withdraw, Deposit, Reset Password, Check Password, Exit).</li>
            </ul>
        </div>

        <!-- File Structure Section -->
        <h2 class="text-2xl sm:text-3xl font-semibold text-gray-800 mb-4 border-b border-gray-300 pb-1">
            File Structure
        </h2>
        <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto text-sm sm:text-base mb-4"><code>.
├── ATM.py
└── Atm Management Project/
    ├── balance.txt
    └── password.txt</code></pre>
        <ul class="list-disc list-inside space-y-2 mb-6 ml-4 text-lg">
            <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">ATM.py</code>: The main Python script containing the <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm</code> class and the <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">main</code> function to run the ATM simulation.</li>
            <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm Management Project/balance.txt</code>: Stores the current account balance.</li>
            <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm Management Project/password.txt</code>: Stores the ATM password (PIN).</li>
        </ul>

        <!-- Code Overview Section -->
        <h2 class="text-2xl sm:text-3xl font-semibold text-gray-800 mb-4 border-b border-gray-300 pb-1">
            Code Overview
        </h2>
        <p class="text-lg mb-4">
            The <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">ATM.py</code> file contains:
        </p>
        <ul class="list-disc list-inside space-y-2 mb-6 ml-4 text-lg">
            <li><strong class="font-medium"><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm</code> Class:</strong>
                <ul class="list-circle list-inside ml-6 space-y-1 mt-1">
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">__init__</code>: Initializes file paths for <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">balance.txt</code> and <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">password.txt</code>.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">check_balance()</code>: Reads and displays the current balance.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">withdraw(amount)</code>: Handles money withdrawal, updates the balance file.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">deposit(amount)</code>: Handles money deposit, updates the balance file.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">atm_password(pin)</code>: Checks if the entered PIN matches the stored PIN.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">reset_password(new_pin)</code>: Updates the password file with a new PIN.</li>
                    <li><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">check()</code>: Displays the current password.</li>
                </ul>
            </li>
            <li><strong class="font-medium"><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">greet(fx)</code> Decorator:</strong> A simple decorator to add welcome and thank you messages around the <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">main</code> function execution.</li>
            <li><strong class="font-medium"><code class="bg-gray-200 rounded px-1 py-0.5 text-sm">main()</code> Function:</strong>
                <ul class="list-circle list-inside ml-6 space-y-1 mt-1">
                    <li>The entry point of the ATM simulation.</li>
                    <li>Prompts the user for their name and password.</li>
                    <li>If the password is correct, it enters a loop presenting the ATM menu.</li>
                    <li>Handles user choices and calls the appropriate <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">Atm</code> class methods.</li>
                    <li>Includes basic error handling for <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">ValueError</code> when expecting numerical input.</li>
                </ul>
            </li>
        </ul>

        <!-- Important Notes Section -->
        <h2 class="text-2xl sm:text-3xl font-semibold text-gray-800 mb-4 border-b border-gray-300 pb-1">
            Important Notes
        </h2>
        <ul class="list-disc list-inside space-y-2 mb-6 ml-4 text-lg">
            <li><strong class="font-medium">Security:</strong> This project uses basic file handling for storing balance and password. <strong class="text-red-600">It is not secure for real-world applications.</strong> Passwords are stored in plain text, and there's no encryption or robust error handling for file operations.</li>
            <li><strong class="font-medium">Error Handling:</strong> Basic <code class="bg-gray-200 rounded px-1 py-0.5 text-sm">try-except</code> blocks are used for file operations and input validation, but more comprehensive error handling would be needed for a production-ready system.</li>
            <li><strong class="font-medium">Data Persistence:</strong> The balance and password are saved to text files, so they persist between runs of the script.</li>
        </ul>
    </div>
</body>
</html>
