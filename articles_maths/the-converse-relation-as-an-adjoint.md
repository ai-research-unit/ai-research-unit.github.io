
# __The Converse Relation as an Adjoint__

## Introduction

The converse $R^{-1}$ of a relation is the adjoint of $R$ in two distinct senses, and this article
separates them and proves that they agree. In the **residuation** of composition, the operator $S
\mapsto R ; S$ has the right adjoint $T \mapsto R \backslash T$, and the right adjoint is computed by
the converse, $R \backslash T = \overline{R^{-1} ; \overline{T}}$; the same holds on the other side,
$T / R = \overline{\overline{T} ; R^{-1}}$. In the **operator layer** of the preceding article, the
conjugation by the converse sends the left-composition with $R$ to the right-composition with
$R^{-1}$, and it exchanges the left and the right adjoints of the residuation; so the converse is the
adjoint of $R$ both for the order and for the involution on the operators. The article proves these
compatibilities, so that "adjoint" means the same thing in *The Converse as an Adjoint*, in *Relation
Algebras and the Converse* and in *Involutions of the Operator Layer*.

The article presupposes *Relation Algebras and the Converse*, for the residuals, and *The Converse as
an Adjoint* and *Involutions of the Operator Layer*, which precede it in this Part. It names no form,
no norm and no topology; the Hilbert-space adjoint is Part II and is not used.

## The Residuation by the Converse

**Definition.** For relations $R \subseteq X \times Y$, $S \subseteq Y \times Z$ and $T \subseteq X
\times Z$, the two composition operators are

$$
L_R(S) = R ; S, \qquad R_R(S) = S ; R ,
$$

the **left** and the **right** composition with $R$, where $R_R$ is defined for relations $S \subseteq
W \times X$.

**Theorem.** The right adjoints of the two composition operators are computed by the converse:

$$
R \backslash T = \overline{R^{-1} ; \overline{T}}, \qquad T / R = \overline{\overline{T} ; R^{-1}} ,
$$

and the adjunctions are

$$
L_R \dashv (T \mapsto R \backslash T), \qquad (S \mapsto S ; R) \dashv (T \mapsto T / R) .
$$

The unit and counit are $S \subseteq R \backslash (R;S)$, $R ; (R \backslash T) \subseteq T$ on the
left, and dually on the right.

**Proof.** The residual identities are proved in *Relation Algebras and the Converse*; the two
formulas are the same computation as for $R \backslash T$ there, with the converse read on the other
side for $T / R$. The unit and counit are the inclusions of the adjunction.

**Corollary.** The converse is the adjoint to composition in the following sense: the operator $L_R$
has, as its right adjoint, the operator $T \mapsto \overline{R^{-1};\overline{T}}$, which is built from
the composition with $R^{-1}$ and the complement, and the operator $R_{R}$ has the right adjoint built
from $R^{-1}$ on the other side. Hence "compose with $R$" is left adjoint to "compose with $R^{-1}$ and
complement".

**Proof.** The statement is the theorem together with the definition of the residuals; the two
composites with $R^{-1}$ appear in the two displayed formulas.

## Compatibility with the Operator-Layer Involution

Let $\varphi$ be the involution of the operator layer of *Involutions of the Operator Layer*, acting on
operators $F$ on relations by $\varphi(F)(R) = (F(R^{-1}))^{-1}$, that is, conjugation by the converse.

**Theorem.** The involution exchanges the two composition operators and substitutes the converse:

$$
\varphi(L_R) = R_{R^{-1}}, \qquad \varphi(R_R) = L_{R^{-1}} .
$$

**Proof.** For the first, $\varphi(L_R)(S) = (L_R(S^{-1}))^{-1} = (R ; S^{-1})^{-1} = (S^{-1})^{-1} ;
R^{-1} = S ; R^{-1} = R_{R^{-1}}(S)$, using the law of the converse for a composite. The second is the
same computation with the roles of the sides exchanged.

**Corollary.** The involution is an automorphism of the composition of operators,
$\varphi(F \circ G) = \varphi(F) \circ \varphi(G)$, and it is an anti-automorphism of the composition of
relations in the following sense: on the operators, it is a homomorphism; on the relations, the operator
it is applied to has its converse taken. It maps the fixed operators of the operator layer, hence the
operators that commute with the converse, to themselves.

**Proof.** The homomorphism property is the general property of the conjugation of *Involutions of the
Operator Layer*; the last statement is the definition of the fixed part there.

**Theorem (the two adjointnesses agree).** The involution $\varphi$ exchanges the two members of the
residuation: if $L_R$ has the right adjoint $K_R : T \mapsto R \backslash T$, then $\varphi(K_R)$ is the
**left** adjoint of $\varphi(L_R) = R_{R^{-1}}$, and explicitly

$$
\varphi(K_R)(T) = \overline{\overline{T} ; R} = T / R^{-1} .
$$

**Proof.** The adjunction-reversal of *Involutions of the Operator Layer* applied to $L_R \dashv K_R$
gives $K_R^{\perp} \dashv L_R^{\perp}$, that is, $\varphi(K_R) \dashv \varphi(L_R)$. For the explicit
formula, $K_R(T) = \overline{R^{-1};\overline{T}}$, so $\varphi(K_R)(T) = (K_R(T^{-1}))^{-1} =
\overline{\overline{(T^{-1})} ; R} = \overline{\overline{T};R}$, using $(\overline{R^{-1};\overline{T^{-1}}})^{-1}
= \overline{(\overline{T^{-1}})^{-1}; R}$; and $\overline{\overline{T};R} = T / R^{-1}$ by the definition
of the left residual, since $(R^{-1})^{-1} = R$.

**Example.** Let $R$ be a function, so that $R^{-1}$ is its inverse relation. Then $R \backslash T =
R^{-1} ; T$ (no complement is needed, because $R$ is total and single-valued), and the two operators
$L_R$ and $L_{R^{-1}}$ are mutually inverse on the level of the induced maps; the involution
$\varphi$ fixes the pair. For a general relation the complement remains and the adjoint is the residual
of the theorem.

## Summary

The converse is the adjoint of a relation for composition: the operator "compose with $R$" is
residuated with right adjoint the residual $R \backslash T = \overline{R^{-1} ; \overline{T}}$, and the
same holds on the other side with $T / R = \overline{\overline{T} ; R^{-1}}$; the converse is exactly
what computes the adjoint, and the unit and counit are the two inclusions of the residuation.

On the operator layer the conjugation by the converse, $\varphi(F)(R) = (F(R^{-1}))^{-1}$, is an
involution and an automorphism of the composition of operators that sends the left-composition with $R$
to the right-composition with $R^{-1}$ and conversely, and it reverses the residuation by exchanging
the left and the right adjoints. So the converse is the adjoint of $R$ for the order and, at the same
time, the operation that makes the operator-layer involution act on composition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_R(S) = R;S$, $R_R(S) = S;R$ | Left and right composition with $R$ |
| $R \backslash T = \overline{R^{-1};\overline{T}}$ | Right residual, computed by the converse |
| $T / R = \overline{\overline{T};R^{-1}}$ | Left residual |
| $\varphi(F)(R) = (F(R^{-1}))^{-1}$ | The operator-layer involution |
| $\varphi(L_R) = R_{R^{-1}}$, $\varphi(R_R) = L_{R^{-1}}$ | The exchange of the composition operators |

## Further Reading

- Chris Brink, Wolfram Kahl and Gunther Schmidt, *Relational Methods in Computer Science* (Springer, 1997), for the residual calculus and the adjointness of the converse.
- Gunther Schmidt and Thomas Ströhlein, *Relations and Graphs* (Springer, 1993), for the algebra of relations, residuals and the converse.
- Michael Barr and Charles Wells, *Category Theory for Computing Science*, 3rd ed. (CRM, 1999), for adjunctions, units and counits.
- Richard Bird and Oege de Moor, *Algebra of Programming* (Prentice Hall, 1997), for the algebra of relations and the residual as an adjoint.
- Francis Borceux, *Handbook of Categorical Algebra 1* (Cambridge University Press, 1994), for adjunctions, units and counits and their duality.
