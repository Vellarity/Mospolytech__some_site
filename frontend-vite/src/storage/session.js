import {defineStore} from "pinia"
import { localRoute } from "../helper/constants";

export const useSessionStore = defineStore('session', {
    state:() => {
        return {
            csrf: "",
            username: "",
            password: "",
            error: "",
            isAuthenticated: false,    
        }
    },
    actions: {
        getCSRF: () => {
            fetch("/api/csrf/", {
              credentials: "same-origin",
            })
            .then((res) => {
              let csrfToken = res.headers.get("X-CSRFToken");
              this.setState({csrf: csrfToken});
              console.log(csrfToken);
            })
            .catch((err) => {
              console.log(err);
            });
          },
        
          getSession: () => {
            fetch("/api/session/", {
              credentials: "same-origin",
            })
            .then((res) => res.json())
            .then((data) => {
              console.log(data);
              if (data.isAuthenticated) {
                this.setState({isAuthenticated: true});
              } else {
                this.setState({isAuthenticated: false});
                this.getCSRF();
              }
            })
            .catch((err) => {
              console.log(err);
            });
          },
        
          whoami: () => {
            fetch("/api/whoami/", {
              headers: {
                "Content-Type": "application/json",
              },
              credentials: "same-origin",
            })
            .then((res) => res.json())
            .then((data) => {
              console.log("You are logged in as: " + data.username);
            })
            .catch((err) => {
              console.log(err);
            });
          },
        
          handlePasswordChange: (event) => {
            this.setState({password: event.target.value});
          },
        
          handleUserNameChange: (event) => {
            this.setState({username: event.target.value});
          },
        
          isResponseOk(response) {
            if (response.status >= 200 && response.status <= 299) {
              return response.json();
            } else {
              throw Error(response.statusText);
            }
          },
        
          login: (event) => {
            event.preventDefault();
            fetch("/api/login/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": this.state.csrf,
              },
              credentials: "same-origin",
              body: JSON.stringify({username: this.state.username, password: this.state.password}),
            })
            .then(this.isResponseOk)
            .then((data) => {
              console.log(data);
              this.setState({isAuthenticated: true, username: "", password: "", error: ""});
            })
            .catch((err) => {
              console.log(err);
              this.setState({error: "Wrong username or password."});
            });
          },
        
          logout: () => {
            fetch("/api/logout", {
              credentials: "same-origin",
            })
            .then(this.isResponseOk)
            .then((data) => {
              console.log(data);
              this.setState({isAuthenticated: false});
              this.getCSRF();
            })
            .catch((err) => {
              console.log(err);
            });
          }
    }
})