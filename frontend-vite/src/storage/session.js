import {defineStore} from "pinia"
import { localRoute } from "../helper/constants";
import Cookies from "js-cookie"

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
        async getCSRF() {
            fetch(`${localRoute}api/auth/get_csrf/`,)
                .then((res) => {
                    let csrfToken = res.headers.get("X-CSRFToken");
                    localStorage.setItem('csrftoken', csrfToken)
                    this.csrf = csrfToken;
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        
        async getSession() {
            fetch(`${localRoute}api/auth/session/`,{
               
            })
                .then((res) => res.json())
                .then((data) => {
                    console.log(data);
                    if (data.isAuthenticated) {
                        this.isAuthenticated = true
                    } else {
                        this.isAuthenticated = false
                        this.getCSRF();
                    }
                })
                .catch((err) => {
                    console.error(err);
                });
        },
    
        async whoami() {
            fetch(`${localRoute}api/auth/whoami/`, {
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

        async login(event) {
            event.preventDefault();
            fetch(`${localRoute}api/login/`, {
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

        async logout() {
            fetch(`${localRoute}api/logout`, {
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
        },
    }
})