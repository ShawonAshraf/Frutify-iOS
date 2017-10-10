//: Playground - noun: a place where people can play

import UIKit
import Foundation
import PlaygroundSupport


let url = URL(string: "http://40.71.188.243:9999/api/v1_0")


let task = URLSession.shared.dataTask(with: url!) { (data, response, error) in
    if let data = data,
        let html = String(data: data, encoding: String.Encoding.utf8) {
        print(html)
    }
}

task.resume()
PlaygroundPage.current.needsIndefiniteExecution = true


