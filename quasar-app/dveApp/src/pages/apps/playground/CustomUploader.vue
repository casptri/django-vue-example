<template>
  <div class="q-gutter-sm row items-start">
    <div class="col">
    <q-file
      v-model="file"
      filled
      style="max-width: 300px"
      />
    </div>
    <div class="col">
    <q-btn
      icon="add"
      @click="doUpload"
      />
    <q-uploader
        url="http://localhost:8000/file/file"
        field-name="up_file"
        label="No thumbnails"
        color="amber"
        text-color="black"
        no-thumbnails
        style="max-width: 300px"
        />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { api } from 'boot/axios'
//import { _ } from 'vue-underscore'

export default {
  name: 'CustomUploader',
  setup (props, context) {
    const file = ref(null)

    const doUpload = () => {
      let fd = new FormData();
      fd.append("file", file.value);
      fd.append("type", file.value.type);

      api.post("/api/pdf", fd,
        { headers:
          { 'Content-Type': "multipart/form-data"},
        }).then(response =>
        {
          console.log(response)
        }).catch(error => {
          console.log(error)
        })
      }
    return {
      file,
      doUpload,
    }
  },
}
</script>
<style>
</style>

