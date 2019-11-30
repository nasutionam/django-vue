<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link :to="{ name: 'home' }" class="navbar-brand">DISCUSSION</router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto">                
                </ul>
                <router-link :to="{ name: 'home' }" class="btn btn-info">Home</router-link>
                <router-link :to="{ name: 'question-editor' }" class="btn btn-success mx-1">Ask Question</router-link>
                <a class="btn btn-primary my-2 my-sm-0 mx-1" @click="onChangePass">Change Password</a>
                <a class="btn btn-danger my-2 my-sm-0" href="/accounts/logout/">Logout</a>
                
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent",
    methods: {
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