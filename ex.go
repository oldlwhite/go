package main
import (
    "fmt"
    "io/ioutil"
    "net/http"
    "time"
    "protoc-gen-go"
)
// func GetData(c chan string){
//     client := &http.Client{}
//     resp, err := client.Get("https://zhuanlan.zhihu.com/p/55039990")
//     if err != nil {
//         fmt.Println("错误异常",err)
//     }
    
//     defer resp.Body.Close()
//     body, err := ioutil.ReadAll(resp.Body)
//     if err != nil {
//         fmt.Println("错误异常2",err)
//     }
//     // fmt.Println("good")
//     // fmt.Println(string(body))
//     // fmt.Println(len(string(body)))
//     c <- string(body)
// }
// func main(){
//     t:=time.Now().Second()
//     c := make(chan string)
//     for i:=0;i<20;i++{
//         go GetData(c)
//     }
//     for i:=0;i<20;i++{
//         fmt.Println(len(<-c))
//     }
//     // close(c)
//     fmt.Println(time.Now().Second()-t)
//     // fmt.Println(GetData())
// }
git config --global user.email "2216403312@qq.com"
git config --global user.password "aaAA8349276150"
git config --list
