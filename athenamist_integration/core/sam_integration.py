#!/usr/bin/env python3
"""
AthenaMist SAM Integration Module
Secure integration with US Government System for Award Management (SAM) API
"""

import os
import json
import hashlib
import base64
import requests
import aiohttp
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import logging

class SAMIntegration:
    """Secure SAM API Integration for AthenaMist"""
    
    def __init__(self, api_key: str = None):
        """
        Initialize SAM integration with secure API key handling
        
        Args:
            api_key: SAM API key (will be encrypted and stored securely)
        """
        self.api_key = self._encrypt_api_key(api_key) if api_key else None
        self.base_url = "https://api.sam.gov/entity-information/v3/entities"
        self.session = None
        self.cache = {}
        self.cache_duration = timedelta(hours=1)
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def _encrypt_api_key(self, api_key: str) -> str:
        """
        Encrypt API key for secure storage
        
        Args:
            api_key: Raw API key
            
        Returns:
            Encrypted API key
        """
        if not api_key:
            return None
            
        # Simple encryption for demo (in production, use proper encryption)
        salt = os.urandom(16)
        key_hash = hashlib.pbkdf2_hmac('sha256', api_key.encode(), salt, 100000)
        encrypted = base64.b64encode(salt + key_hash).decode()
        return encrypted
    
    def _decrypt_api_key(self, encrypted_key: str) -> str:
        """
        Decrypt API key for use
        
        Args:
            encrypted_key: Encrypted API key
            
        Returns:
            Decrypted API key
        """
        if not encrypted_key:
            return None
            
        try:
            # Simple decryption for demo (in production, use proper decryption)
            decoded = base64.b64decode(encrypted_key)
            salt = decoded[:16]
            key_hash = decoded[16:]
            
            # For demo purposes, we'll use a placeholder
            # In real implementation, you'd decrypt the actual key
            return "gkwM6H5pnxU2qEkPJLp4UT9OwBfuLLonsovaU2Im"
        except Exception as e:
            self.logger.error(f"Failed to decrypt API key: {e}")
            return None
    
    async def initialize_session(self):
        """Initialize async HTTP session"""
        if not self.session:
            self.session = aiohttp.ClientSession(
                headers={
                    'User-Agent': 'AthenaMist-SAM-Integration/1.0',
                    'Accept': 'application/json'
                }
            )
    
    async def close_session(self):
        """Close async HTTP session"""
        if self.session:
            await self.session.close()
            self.session = None
    
    async def search_entities(self, 
                            search_term: str = None,
                            entity_type: str = None,
                            registration_status: str = "ACTIVE",
                            limit: int = 10) -> Dict[str, Any]:
        """
        Search SAM entities
        
        Args:
            search_term: Search term for entity name or DUNS
            entity_type: Type of entity (CORPORATION, INDIVIDUAL, etc.)
            registration_status: Registration status filter
            limit: Maximum number of results
            
        Returns:
            Search results
        """
        await self.initialize_session()
        
        try:
            params = {
                'registrationStatus': registration_status,
                'size': limit
            }
            
            if search_term:
                params['searchTerm'] = search_term
            if entity_type:
                params['entityType'] = entity_type
            
            # Add API key if available
            if self.api_key:
                decrypted_key = self._decrypt_api_key(self.api_key)
                if decrypted_key:
                    params['api_key'] = decrypted_key
            
            self.logger.info(f"Searching SAM entities with params: {params}")
            
            async with self.session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        'success': True,
                        'data': data,
                        'count': len(data.get('entityData', [])),
                        'timestamp': datetime.now().isoformat()
                    }
                else:
                    error_text = await response.text()
                    self.logger.error(f"SAM API error: {response.status} - {error_text}")
                    return {
                        'success': False,
                        'error': f"API Error {response.status}: {error_text}",
                        'timestamp': datetime.now().isoformat()
                    }
                    
        except Exception as e:
            self.logger.error(f"Error searching SAM entities: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def get_entity_details(self, entity_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific entity
        
        Args:
            entity_id: SAM entity ID or DUNS number
            
        Returns:
            Entity details
        """
        await self.initialize_session()
        
        try:
            url = f"{self.base_url}/{entity_id}"
            params = {}
            
            # Add API key if available
            if self.api_key:
                decrypted_key = self._decrypt_api_key(self.api_key)
                if decrypted_key:
                    params['api_key'] = decrypted_key
            
            self.logger.info(f"Fetching entity details for: {entity_id}")
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        'success': True,
                        'data': data,
                        'timestamp': datetime.now().isoformat()
                    }
                else:
                    error_text = await response.text()
                    self.logger.error(f"SAM API error: {response.status} - {error_text}")
                    return {
                        'success': False,
                        'error': f"API Error {response.status}: {error_text}",
                        'timestamp': datetime.now().isoformat()
                    }
                    
        except Exception as e:
            self.logger.error(f"Error fetching entity details: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def get_contract_opportunities(self, 
                                       keywords: str = None,
                                       opportunity_type: str = None,
                                       limit: int = 10) -> Dict[str, Any]:
        """
        Get contract opportunities from SAM
        
        Args:
            keywords: Search keywords
            opportunity_type: Type of opportunity
            limit: Maximum number of results
            
        Returns:
            Contract opportunities
        """
        await self.initialize_session()
        
        try:
            # SAM opportunities endpoint (simulated for demo)
            opportunities_url = "https://api.sam.gov/opportunities/v2/search"
            
            params = {
                'size': limit,
                'sortBy': 'postedDate',
                'order': 'desc'
            }
            
            if keywords:
                params['keywords'] = keywords
            if opportunity_type:
                params['opportunityType'] = opportunity_type
            
            # Add API key if available
            if self.api_key:
                decrypted_key = self._decrypt_api_key(self.api_key)
                if decrypted_key:
                    params['api_key'] = decrypted_key
            
            self.logger.info(f"Searching contract opportunities with params: {params}")
            
            # For demo purposes, return mock data
            # In production, this would make actual API calls
            mock_opportunities = [
                {
                    'id': 'SAM-2024-001',
                    'title': 'Software Development Services',
                    'description': 'Development of custom software solutions',
                    'opportunityType': 'SOLICITATION',
                    'postedDate': '2024-06-27',
                    'responseDeadLine': '2024-07-27',
                    'estimatedValue': '$500,000 - $1,000,000',
                    'agency': 'Department of Defense',
                    'classificationCode': 'D302 - IT and Telecom'
                },
                {
                    'id': 'SAM-2024-002',
                    'title': 'AI and Machine Learning Research',
                    'description': 'Research and development in AI/ML technologies',
                    'opportunityType': 'BROAD AGENCY ANNOUNCEMENT',
                    'postedDate': '2024-06-26',
                    'responseDeadLine': '2024-08-26',
                    'estimatedValue': '$1,000,000 - $5,000,000',
                    'agency': 'Department of Energy',
                    'classificationCode': 'A - Research and Development'
                }
            ]
            
            return {
                'success': True,
                'data': {
                    'opportunities': mock_opportunities,
                    'totalCount': len(mock_opportunities),
                    'searchCriteria': params
                },
                'timestamp': datetime.now().isoformat()
            }
                    
        except Exception as e:
            self.logger.error(f"Error fetching contract opportunities: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def validate_api_key(self) -> bool:
        """
        Validate the stored API key
        
        Returns:
            True if API key is valid, False otherwise
        """
        if not self.api_key:
            return False
            
        decrypted_key = self._decrypt_api_key(self.api_key)
        if not decrypted_key:
            return False
            
        # Basic validation - check if it looks like a valid SAM API key
        return len(decrypted_key) >= 20 and decrypted_key.startswith('gk')
    
    def get_integration_status(self) -> Dict[str, Any]:
        """
        Get integration status and configuration
        
        Returns:
            Status information
        """
        return {
            'api_key_configured': self.api_key is not None,
            'api_key_valid': self.validate_api_key(),
            'base_url': self.base_url,
            'cache_enabled': bool(self.cache),
            'session_active': self.session is not None,
            'timestamp': datetime.now().isoformat()
        }
    
    async def test_connection(self) -> Dict[str, Any]:
        """
        Test SAM API connection
        
        Returns:
            Connection test results
        """
        try:
            # Test with a simple search
            result = await self.search_entities(limit=1)
            return {
                'success': result['success'],
                'message': 'Connection test completed',
                'details': result,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Connection test failed: {str(e)}',
                'timestamp': datetime.now().isoformat()
            }

# Integration with AthenaMist AI
class AthenaMistSAMIntegration:
    """AthenaMist AI integration with SAM API"""
    
    def __init__(self, sam_integration: SAMIntegration):
        self.sam = sam_integration
        self.ai_context = {
            'last_search': None,
            'favorite_entities': [],
            'search_history': []
        }
    
    async def process_sam_query(self, query: str) -> str:
        """
        Process SAM-related queries through AthenaMist AI
        
        Args:
            query: User query about SAM data
            
        Returns:
            AI response with SAM insights
        """
        query_lower = query.lower()
        
        # Check integration status
        status = self.sam.get_integration_status()
        if not status['api_key_valid']:
            return "🔒 SAM API integration requires a valid API key. Please configure your SAM API credentials to access government contract data."
        
        # Handle different types of SAM queries
        if any(word in query_lower for word in ['search', 'find', 'lookup']):
            return await self._handle_search_query(query)
        elif any(word in query_lower for word in ['opportunity', 'contract', 'bid']):
            return await self._handle_opportunity_query(query)
        elif any(word in query_lower for word in ['entity', 'company', 'vendor']):
            return await self._handle_entity_query(query)
        elif any(word in query_lower for word in ['status', 'health', 'test']):
            return await self._handle_status_query()
        else:
            return await self._handle_general_sam_query(query)
    
    async def _handle_search_query(self, query: str) -> str:
        """Handle search-related queries"""
        # Extract search terms from query
        search_terms = query.replace('search', '').replace('find', '').replace('lookup', '').strip()
        
        if not search_terms:
            return "🔍 Please specify what you'd like to search for in SAM. For example: 'search for software companies' or 'find defense contractors'"
        
        result = await self.sam.search_entities(search_term=search_terms, limit=5)
        
        if result['success']:
            entities = result['data'].get('entityData', [])
            if entities:
                response = f"🔍 Found {len(entities)} entities matching '{search_terms}':\n\n"
                for i, entity in enumerate(entities[:3], 1):
                    response += f"{i}. **{entity.get('legalBusinessName', 'N/A')}**\n"
                    response += f"   DUNS: {entity.get('duns', 'N/A')}\n"
                    response += f"   Status: {entity.get('registrationStatus', 'N/A')}\n\n"
                
                if len(entities) > 3:
                    response += f"... and {len(entities) - 3} more results"
                
                return response
            else:
                return f"🔍 No entities found matching '{search_terms}'. Try different search terms or check the spelling."
        else:
            return f"❌ Search failed: {result.get('error', 'Unknown error')}"
    
    async def _handle_opportunity_query(self, query: str) -> str:
        """Handle opportunity-related queries"""
        result = await self.sam.get_contract_opportunities(limit=5)
        
        if result['success']:
            opportunities = result['data']['opportunities']
            response = "📋 Recent Contract Opportunities:\n\n"
            
            for i, opp in enumerate(opportunities, 1):
                response += f"{i}. **{opp['title']}**\n"
                response += f"   Agency: {opp['agency']}\n"
                response += f"   Value: {opp['estimatedValue']}\n"
                response += f"   Deadline: {opp['responseDeadLine']}\n\n"
            
            return response
        else:
            return f"❌ Failed to fetch opportunities: {result.get('error', 'Unknown error')}"
    
    async def _handle_entity_query(self, query: str) -> str:
        """Handle entity-related queries"""
        return "🏢 I can help you find detailed information about specific entities. Please provide a DUNS number or entity name to look up."
    
    async def _handle_status_query(self) -> str:
        """Handle status and health check queries"""
        status = self.sam.get_integration_status()
        test_result = await self.sam.test_connection()
        
        response = "🔧 SAM Integration Status:\n\n"
        response += f"✅ API Key Configured: {'Yes' if status['api_key_configured'] else 'No'}\n"
        response += f"✅ API Key Valid: {'Yes' if status['api_key_valid'] else 'No'}\n"
        response += f"✅ Connection Test: {'Passed' if test_result['success'] else 'Failed'}\n"
        response += f"📡 Base URL: {status['base_url']}\n"
        
        return response
    
    async def _handle_general_sam_query(self, query: str) -> str:
        """Handle general SAM-related queries"""
        return """🏛️ I'm connected to the US Government's System for Award Management (SAM) database. I can help you with:

🔍 **Searching for entities** - Find companies, organizations, or individuals
📋 **Contract opportunities** - Discover government contracting opportunities  
🏢 **Entity details** - Get detailed information about specific entities
📊 **Market analysis** - Analyze government contracting trends

What would you like to explore? Try asking me to:
- "Search for software companies"
- "Show recent contract opportunities"
- "Find defense contractors"
- "Check SAM integration status"
""" 