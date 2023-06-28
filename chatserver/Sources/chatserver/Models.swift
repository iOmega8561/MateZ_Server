//
//  File.swift
//  
//
//  Created by Aryan Garg on 31/05/23.
//

import Foundation

struct SubmittedChatMessage: Decodable {
    let message: String
    let user: String // <- We
}
struct ReceivingChatMessage: Encodable, Identifiable {
    let date = Date()
    let id = UUID()
    let message: String
    let user: String // <- new
}
