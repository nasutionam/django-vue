<template>
    <div class="example">
        <h1>This is an example page </h1>
        <h2>{{ message }}</h2>
    </div>
</template>

<script>
export default {
    name: "example",
    data() {
        return {
            message: "Hello This is an example"
        }
    }    
}
</script>

<style scoped>
    h1 {
        color: red;
    }
</style>