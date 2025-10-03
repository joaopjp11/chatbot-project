from typing import List, Dict, Any, Optional

class Person:
	def __init__(
		self,
		nome: Optional[str] = None,
		idade: Optional[int] = None,
		formacao: Optional[str] = None,
		experiencia: Optional[List[Dict[str, Any]]] = None,
		habilidades: Optional[List[str]] = None,
		objetivos: Optional[str] = None,
		info_extra: Optional[Dict[str, Any]] = None
	):
		self.nome = nome if nome is not None else ""
		self.idade = idade if idade is not None else None
		self.formacao = formacao if formacao is not None else ""
		self.experiencia = experiencia if experiencia is not None else []
		self.habilidades = habilidades if habilidades is not None else []
		self.objetivos = objetivos if objetivos is not None else ""
		self.info_extra = info_extra if info_extra is not None else {}

	@classmethod
	def from_dict(cls, data: dict):
		# Handle missing or empty fields
		return cls(
			nome=data.get("nome") if data.get("nome") not in (None, "") else "",
			idade=data.get("idade") if data.get("idade") not in (None, "") else None,
			formacao=data.get("formacao") if data.get("formacao") not in (None, "") else "",
			experiencia=data.get("experiencia") if data.get("experiencia") is not None else [],
			habilidades=data.get("habilidades") if data.get("habilidades") is not None else [],
			objetivos=data.get("objetivos") if data.get("objetivos") not in (None, "") else "",
			info_extra=data.get("info_extra") if data.get("info_extra") is not None else {}
		)
