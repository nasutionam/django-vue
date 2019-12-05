<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link :to="{ name: 'home' }" class="navbar-brand">DISCUSSION</router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto">                
                </ul>
                <router-link :to="{ name: 'home' }" class="btn btn-info">Home</router-link>
                <router-link :to="{ name: 'question-editor' }" class="btn btn-success mx-1">Ask Question</router-link>
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Welcome, {{ username }}
                    </button>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        <a class="dropdown-item" @click="onChangePass">Change Password</a>
                        <a class="dropdown-item" @click="logOut">Logout</a>
                        
                    </div>
                </div>
                
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent",
    data() {
        return {
            username: window.localStorage.getItem("username"),
        }
    },
    
    methods: {
        loadPage() {

        },
        logOut() {
            location.href = '/accounts/logout/';  
                     
        },
        onChangePass () {
        
            location.href = '/accounts/password_change/'
       
        }
    }
}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD;
    }
    .navbar-brand {
        font-weight: bold;
        font-size: 150%;
    }
    .navbar-brand:hover {
        color: grey !important;
    }
</style>