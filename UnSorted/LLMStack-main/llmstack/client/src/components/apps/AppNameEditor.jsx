import { EditOutlined } from "@mui/icons-material";
import { TextField } from "@mui/material";
import { useState } from "react";

export function AppNameEditor({ appName, setAppName }) {
  const [showInput, setShowInput] = useState(false);

  return (
    <div>
      {showInput ? (
        <TextField
          id="standard-basic"
          label="App Name"
          variant="standard"
          value={appName}
          onChange={(e) => setAppName(e.target.value)}
          sx={{ width: "100%" }}
          onBlur={() => {
            setShowInput(false);
            setAppName(appName || "Untitled");
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              setShowInput(false);
              setAppName(appName || "Untitled");
            }
          }}
          inputRef={(input) => input && input.focus()}
          focused={showInput}
          required
        />
      ) : (
        <h1
          onClick={() => setShowInput(true)}
          style={{ fontSize: "20px", margin: "5px 0", textAlign: "left" }}
        >
          {appName} <EditOutlined style={{ fontSize: "14px", color: "#666" }} />
        </h1>
      )}
    </div>
  );
}
