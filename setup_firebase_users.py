#!/usr/bin/env python3
"""
Script para configurar usuários e dados iniciais no Firebase
"""
import firebase_admin
from firebase_admin import credentials, auth, db
import os

# Configuração do Firebase Admin SDK (usando as credenciais do projeto)
firebase_config = {
    "apiKey": "AIzaSyBPgWEv0f8fK25teN6K2S3VGO63s_YRcOA",
    "authDomain": "controleproducao2025-42272.firebaseapp.com",
    "databaseURL": "https://controleproducao2025-42272-default-rtdb.firebaseio.com",
    "projectId": "controleproducao2025-42272",
    "storageBucket": "controleproducao2025-42272.appspot.com",
    "messagingSenderId": "524681663678",
    "appId": "1:524681663678:web:eb4184a410f1e1893bbaef"
}

def create_user_with_role(email, password, role):
    """
    Cria um usuário no Firebase Auth e define seu role no Realtime Database
    """
    try:
        # Criar usuário no Firebase Auth
        user = auth.create_user(
            email=email,
            password=password,
            display_name=f"Usuário {role.title()}"
        )
        
        print(f"✅ Usuário criado: {email} (UID: {user.uid})")
        
        # Definir role no Realtime Database
        ref = db.reference(f'users/{user.uid}')
        ref.set({
            'email': email,
            'role': role,
            'displayName': f"Usuário {role.title()}",
            'createdAt': {'.sv': 'timestamp'}
        })
        
        print(f"✅ Role '{role}' definido para {email}")
        return user.uid
        
    except Exception as e:
        print(f"❌ Erro ao criar usuário {email}: {e}")
        return None

def setup_machine_data():
    """
    Cria dados iniciais das máquinas baseado no HTML original
    """
    machines_data = {
        'A1': {'prefixo': 'SB1036', 'molde': 3, 'blank': 6},
        'A2': {'prefixo': 'A102', 'molde': 7, 'blank': 4},
        'A3': {'prefixo': 'A103', 'molde': 4, 'blank': 4},
        'A4': {'prefixo': 'A104', 'molde': 5, 'blank': 4},
        'A5': {'prefixo': 'A105', 'molde': 4, 'blank': 5},
        'A6': {'prefixo': 'A106', 'molde': 3, 'blank': 4},
        'B1': {'prefixo': 'B101', 'molde': 4, 'blank': 4},
        'B2': {'prefixo': 'B102', 'molde': 4, 'blank': 4},
        'B3': {'prefixo': 'B103', 'molde': 5, 'blank': 4},
        'B4': {'prefixo': 'B104', 'molde': 4, 'blank': 4},
        'B5': {'prefixo': 'B105', 'molde': 6, 'blank': 1},
        'B6': {'prefixo': 'B106', 'molde': 4, 'blank': 4},
        'B7': {'prefixo': 'B107', 'molde': 4, 'blank': 4},
        'B8': {'prefixo': 'B108', 'molde': 4, 'blank': 4},
        'C1': {'prefixo': 'C101', 'molde': 10, 'blank': 5},
        'C2': {'prefixo': 'C102', 'molde': 10, 'blank': 5},
        'C3': {'prefixo': 'C103', 'molde': 4, 'blank': 4},
        'C4': {'prefixo': 'C104', 'molde': 3, 'blank': 4},
        'C5': {'prefixo': 'C105', 'molde': 4, 'blank': 4},
        'C6': {'prefixo': 'C106', 'molde': 4, 'blank': 4},
        'C7': {'prefixo': 'C107', 'molde': 4, 'blank': 4},
        'C8': {'prefixo': 'C108', 'molde': 5, 'blank': 4},
        'D0': {'prefixo': 'D100', 'molde': 4, 'blank': 4},
        'D1': {'prefixo': 'D101', 'molde': 5, 'blank': 4},
        'D2': {'prefixo': 'D102', 'molde': 5, 'blank': 4},
        'D3': {'prefixo': 'D103', 'molde': 4, 'blank': 4},
        'D4': {'prefixo': 'D104', 'molde': 5, 'blank': 4},
        'D5': {'prefixo': 'D105', 'molde': 3, 'blank': 4}
    }
    
    try:
        ref = db.reference('maquinas')
        ref.set(machines_data)
        print("✅ Dados das máquinas configurados com sucesso")
        
        # Calcular totais
        total_moldes = sum(m['molde'] for m in machines_data.values())
        total_blanks = sum(m['blank'] for m in machines_data.values())
        print(f"📊 Total: {total_moldes} moldes, {total_blanks} blanks")
        
    except Exception as e:
        print(f"❌ Erro ao configurar dados das máquinas: {e}")

def main():
    """
    Função principal para configurar Firebase
    """
    try:
        # Inicializar Firebase Admin
        if not firebase_admin._apps:
            # Tentar usar credenciais do arquivo (se existir)
            try:
                cred = credentials.Certificate('firebase-credentials.json')
            except:
                # Usar credenciais default do ambiente
                cred = credentials.ApplicationDefault()
            
            firebase_admin.initialize_app(cred, {
                'databaseURL': firebase_config['databaseURL']
            })
        
        print("🔥 Firebase Admin SDK inicializado")
        
        # Criar usuários de teste
        print("\n👥 Criando usuários de teste...")
        
        # Admin user 
        admin_uid = kNwUX5NAcAQmWLmLROmueIP7dXe2(
            email="admin@sistema.com",
            password="admin123",
            role="admin"
        )
        
        # Regular user
        user_uid = fVo8xOCYR5hE2wpKFAhf6ekEjd83(
            email="usuario@sistema.com", 
            password="usuario123",
            role="usuario"
        )
        
        # Configurar dados das máquinas
        print("\n🏭 Configurando dados das máquinas...")
        setup_machine_data()
        
        print("\n🎉 Configuração completa!")
        print("\n📋 Credenciais para teste:")
        print("┌─────────────────────────────────────┐")
        print("│ ADMIN:                              │")
        print("│ Email: admin@sistema.com            │") 
        print("│ Senha: admin123                     │")
        print("├─────────────────────────────────────┤")
        print("│ USUÁRIO:                            │")
        print("│ Email: usuario@sistema.com          │")
        print("│ Senha: usuario123                   │")
        print("└─────────────────────────────────────┘")
        
    except Exception as e:
        print(f"❌ Erro geral: {e}")

if __name__ == "__main__":
    main()
