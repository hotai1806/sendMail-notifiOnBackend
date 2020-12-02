import "./App.css";
import { Form, Input, InputNumber, Button } from "antd";
import * as PusherPushNotifications from "@pusher/push-notifications-web";
// importScripts("https://js.pusher.com/beams/service-worker.js");
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [subject, setSubject] = useState("");
  const [receiver, setReceiver] = useState("");
  const [message, setMessage] = useState("");

  const layout = {
    labelCol: {
      span: 6,
    },
    wrapperCol: {
      span: 15,
    },
  };
  const beamsClient = new PusherPushNotifications.Client({
    instanceId: "d1b4fec5-3e57-4347-844d-b94e287ae2d2",
  });
  const headers = {
    "Content-Type": "application/json",
  };
  const onSubmit = (event) => {
    // event.preventDefault();

    axios
      .post("http://localhost:8000/send-email", {
        subject: subject,
        receiver: receiver,
        message: message,
      })
      .then((resp) => {
        console.log(resp.data);
      })
      .catch((err) => console.log(err));
    // custom form handling here
  };

  beamsClient
    .start()
    // .then((beamsClient) => beamsClient.getDeviceId())
    // .then((deviceId) =>
    //   console.log("Successfully registered with Beams. Device ID:", deviceId)
    // )
    .then(() => beamsClient.getDeviceInterests())
    .then((interests) => console.log("Current interests:", interests))
    .then(() => beamsClient.setDeviceInterests(["hello"]))
    .then((data) => console.log(data))
    .catch(console.error);

  return (
    <div>
      <h1 style={{ textAlign: "center", padding: "10px" }}>
        SEND EMAIL WITH CELERY
      </h1>
      <form onSubmit={onSubmit} method="POST">
        <Form {...layout} name="nest-messages">
          <Form.Item
            name="subject"
            label="subject"
            rules={[
              {
                required: true,
              },
            ]}
          >
            <Input
              onChange={(event) => {
                setSubject(event.target.value);
              }}
            />
          </Form.Item>
          <Form.Item
            name="receiver"
            label="receiver"
            rules={[
              {
                type: "email",
              },
            ]}
          >
            <Input
              onChange={(event) => {
                setReceiver(event.target.value);
              }}
            />
          </Form.Item>
          <Form.Item label="message">
            <Input.TextArea
              name="message"
              onChange={(event) => {
                setMessage(event.target.value);
              }}
            />
          </Form.Item>
          <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
            <Button
              type="primary"
              htmlType="submit"
              onClick={onSubmit}
              // onSubmit={(e) => sendMessage(e)}
            >
              Submit
            </Button>
          </Form.Item>
        </Form>
      </form>
    </div>
  );
}

export default App;
