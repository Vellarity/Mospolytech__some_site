import {defineStore} from "pinia"
import { localRoute } from "../helper/constants";
import Cookies from "js-cookie"

export const useSessionStore = defineStore('session', {
    state:() => {
        return {
            username: "",
            isAuthenticated: false,    
        }
    },
    actions: {
        isResponseOk(response) {
            if (response.status >= 200 && response.status <= 299) {
                return response.json();
            } else {
                throw Error(response.statusText);
            }
        },

        async login(event) {
            event.preventDefault();
            fetch(`${localRoute}api/auth/token`, {
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                },
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

        async refreshSession() {
            let refresh = localStorage.getItem("REFRESH_TOKEN")
            if (!refresh) return
            fetch(`${localRoute}api/auth/token/refresh`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body:JSON.stringify({
                    "refresh":refresh
                })
            }).then(this.isResponseOk).then((res) => {
                localStorage.setItem("ACCESS_TOKEN", res.access)
                this.isAuthenticated = true
            }).catch((err) => {
                console.log(err);
            });
        },

        async logout() {
            fetch(`${localRoute}api/logout`, {
                credentials:"include",
            }).then(this.isResponseOk).then((data) => {
                console.log(data);
                this.setState({isAuthenticated: false});
                this.getCSRF();
            }).catch((err) => {
                console.log(err);
            });
        },
    }
})