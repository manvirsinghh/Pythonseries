<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Github Workshop Report</title>
</head>
<body style="font-family: 'Arial', sans-serif; margin: 20px; line-height: 1.6; background-color: #f4f7fc; color: #333;">

    <div style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #0056b3; text-align: center;">Daily Live Report (6 Months)</h1>
        <h2 style="color: #0056b3; text-align: center;">GitHub Workshop Report</h2>
        <p><strong>Date:</strong> 15/01/2025</p>
        <p><strong>Start Time:</strong> 7:00 PM | <strong>End Time:</strong> 9:00 PM</p>

        <h3 style="color: #333; margin-bottom: 10px;">Learnings from the Workshop:</h3>

        <ul style="padding-left: 20px;">
            <li><strong>Version Control System & Git:</strong>
                <p>A version control system is a tool that keeps track of changes, creating different versions of our files. It allows us to manage changes, create commits, and synchronize across different computers, enabling collaboration among multiple people. It also allows multiple people to work in parallel.</p>
            </li>
            
            <li><strong>Setting up Git:</strong>
                <p>When using Git for the first time on a new machine, configure the following:</p>
                <ul>
                    <li>Your name and email address</li>
                    <li>Your preferred text editor</li>
                    <li>Global settings for all projects</li>
                </ul>
            </li>
            
            <li><strong>Git Help and Manual:</strong>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git config -h</pre>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git config --help</pre>
            </li>

            <li><strong>Creating Repository:</strong>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git init</pre>
                <p>Use this to create and initialize a new Git repository.</p>
            </li>

            <li><strong>Tracking Changes:</strong>
                <p>To track new changes, Git will notify if there are untracked files:</p>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git status</pre>
                <p>Output will show untracked files:</p>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">On branch main
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
  file-name
nothing added to commit but untracked files present (use "git add" to track)</pre>
                <p>Use the following command to add a file:</p>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git add file-name</pre>
                <p>Now commit the changes:</p>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git commit -m "commit message"</pre>
            </li>

            <li><strong>Push Changes to Remote Repository:</strong>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git push origin main</pre>
            </li>

            <li><strong>Viewing Commit History:</strong>
                <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">$ git log</pre>
            </li>

            <li><strong>The Staging Area:</strong>
                <p>Git staging area ensures only committed changes are recorded. Use `git add` to stage, and `git commit` to take a snapshot of those changes.</p>
            </li>

            <li><strong>Conflicts:</strong>
                <p>Conflicts happen when two people modify the same lines in a file, requiring manual resolution.</p>
            </li>
        </ul>

        <div style="background-color: #dcdcdc; padding: 15px; border-left: 5px solid #ff5733; margin-bottom: 15px;">
            <p><strong>Sample Code Output:</strong></p>
            <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto;">
On branch main
No commits yet
Untracked files:
   (use "git add <file>..." to include in what will be committed)
	file-name
nothing added to commit but untracked files present (use "git add" to track)
            </pre>
        </div>

        <h3 style="color: #333; margin-bottom: 10px;">Visual Example:</h3>
        <img src="https://github.com/user-attachments/assets/639861d6-1306-49ab-aaf7-1a2f81d5fa62" alt="Git Staging Area" style="display: block; margin: 20px auto; width: 80%; max-width: 600px; border: 1px solid #ccc; border-radius: 5px;">

        <div style="font-size: 0.9em; color: #888; text-align: center; margin-top: 30px;">
            <p>Report generated by: Manvir Singh | GitHub Workshop</p>
        </div>
    </div>

</body>
</html>
