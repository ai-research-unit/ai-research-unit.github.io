
# __The Graded Action on a Module over a Bimodule over an Algebra__

## Introduction

A $\mathbb{Z}/2$-graded algebra carries two structures at once: a decomposition into an even and an odd part, and the automorphism that is $+1$ on the even part and $-1$ on the odd part. The action of the algebra on a graded module is required to respect the decomposition, and respecting it forces a **sign rule**: moving an odd scalar past an odd element costs a sign. This article states the compatibility condition, $A_iM_j \subseteq M_{i+j}$, derives the sign rule from it, and shows how the rule turns a graded left module over a graded-commutative algebra into a graded bimodule, where the two-sided operators of *The Signed Sandwich on a Bimodule over an Algebra* acquire a parity.

The article is the graded member of the `- Operator Theory` group of this category. It uses the one-sided operators of *Left and Right Multiplication of a Module* and the signed operators of *The Signed Sandwich on a Bimodule over an Algebra* and *The Signed Left Multiplication on a Module over an Algebra*; the grading itself, superalgebras and their morphisms belong to *Superalgebras and Graded Structures*, named here and not developed. The adjoint action of the algebra on its endomorphisms is the subject of *The Graded Adjoint Action on a Module over a Bimodule over an Algebra*, the last article of this group. The article stays inside Part I: no distance, norm, form or limit occurs. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $A=A_{\bar0}\oplus A_{\bar1}$ is a graded unital associative $R$-algebra, $\alpha$ is its grade involution, and $M=M_{\bar0}\oplus M_{\bar1}$ is a graded left $A$-module.

## Graded Algebras, Modules and the Grade Involution

### The grading and its sign operator

**Definition.** A **graded $R$-algebra** is an $R$-algebra $A$ with a direct sum decomposition $A=A_{\bar0}\oplus A_{\bar1}$ such that

$$
A_iA_j \subseteq A_{i+j} \qquad (i,j \in \mathbb{Z}/2).
$$

A **graded left $A$-module** is a left $A$-module $M$ with a decomposition $M=M_{\bar0}\oplus M_{\bar1}$ such that

$$
A_iM_j \subseteq M_{i+j} \qquad (i,j \in \mathbb{Z}/2).
$$

Elements of $A_{\bar0}$ and $M_{\bar0}$ are **even**, those of $A_{\bar1}$ and $M_{\bar1}$ **odd**, and the **degree** $\deg x \in \mathbb{Z}/2$ is defined for homogeneous $x$.

**Definition.** The **grade involution** of $A$ is the $R$-linear map

$$
\alpha : A \to A, \qquad \alpha(a)=(-1)^{i}a \quad (a \in A_i),
$$

and the grade involution of $M$ is the analogous map on $M$.

**Proposition.** The grade involution of $A$ is an $R$-algebra automorphism with $\alpha^{2}=\mathrm{id}$, and its fixed part is $A_{\bar0}$; the grade involution of $M$ is additive with $\alpha^{2}=\mathrm{id}$ and satisfies

$$
\alpha(am)=\alpha(a)\,\alpha(m) \qquad (a \in A,\ m \in M).
$$

Conversely, a map $\alpha$ with these properties determines the grading by $A_i=\{a : \alpha(a)=(-1)^{i}a\}$ and $M_j=\{m : \alpha(m)=(-1)^{j}m\}$.

*Proof.* $\alpha$ is linear and $\alpha(ab)=(-1)^{i+j}ab=\alpha(a)\alpha(b)$ for $a \in A_i$, $b \in A_j$, so it is an automorphism; $\alpha^{2}=\mathrm{id}$ because $(-1)^{2i}=1$. For the compatibility, $a \in A_i$ and $m \in M_j$ have $am \in M_{i+j}$, and both sides of $\alpha(am)=\alpha(a)\alpha(m)$ equal $(-1)^{i+j}am$. The converse is the eigenspace decomposition of an involution when $2$ is invertible. $\square$

Thus a graded module over a graded algebra is the same thing as a module with a compatible grade involution, which is the structure used by the two signed articles cited above; the grading and the involution are two descriptions of one datum.

### The action is even

**Proposition.** The action homomorphism $\rho : A \to \operatorname{End}_R(M)$ carries $A_i$ into the operators of parity $i$:

$$
a \in A_i \implies L_a(M_j) \subseteq M_{i+j}.
$$

*Proof.* This is the compatibility $A_iM_j \subseteq M_{i+j}$ read as a statement about the image of the left multiplication. $\square$

The action of a graded algebra on a graded module is therefore **even**: it preserves the degree, $\deg(am)=\deg a+\deg m$ for homogeneous $a$ and $m$.

## The Sign Rule

### The Koszul sign

**Definition.** The **Koszul sign** of two homogeneous elements $s$ and $t$ is $(-1)^{\deg s\,\deg t}$. It is $+1$ unless both degrees are odd, and then it is $-1$.

The grading forces the sign wherever two homogeneous things are exchanged. The first place it appears is the compatibility of the one-sided operators with the grade involution.

**Proposition (the sign rule for the operators).** For homogeneous $a \in A$,

$$
\alpha\,L_a\,\alpha^{-1}=(-1)^{\deg a}\,L_a, \qquad \alpha\,L_a=L_{\alpha(a)}\,\alpha .
$$

More generally, for every homogeneous operator $T \in \operatorname{End}_R(M)$ of parity $\deg T$,

$$
\alpha\,T\,\alpha^{-1}=(-1)^{\deg T}\,T .
$$

*Proof.* $\alpha L_a\alpha^{-1}(m)=\alpha(a\,\alpha^{-1}(m))=\alpha(a)m=(-1)^{\deg a}am=(-1)^{\deg a}L_a(m)$. For a homogeneous $T$ of parity $i$ and $m \in M_j$, $T(m) \in M_{i+j}$ and $\alpha T\alpha^{-1}(m)=(-1)^{j}\alpha(T(m))=(-1)^{j}(-1)^{i+j}T(m)=(-1)^{i}T(m)$. $\square$

This is the exact sense in which the grade involution imposes a sign on the operators: conjugation by $\alpha$ multiplies an operator of parity $i$ by $(-1)^{i}$, so the two-sided operators of the signed sandwich are exactly the operators twisted by that sign.

### From a graded left module to a graded bimodule

A graded left module carries a canonical right action, and the sign rule is what makes it associative.

**Theorem.** Let $A$ be graded-commutative, that is

$$
bc=(-1)^{\deg b\,\deg c}\,cb \qquad (b,c \text{ homogeneous}),
$$

and define, for homogeneous $b \in A$,

$$
R_b(m)=(-1)^{\deg b\,\deg m}\,bm, \qquad m\text{ homogeneous}.
$$

Then $R$ is a right action, $R_{bc}=R_cR_b$, and the left and right actions commute:

$$
(m\cdot b)\cdot c=m\cdot(bc), \qquad a\,(m\cdot b)=(am)\cdot b .
$$

Consequently $M$ is a graded $(A,A)$-bimodule, and each $R_b$ is $R$-linear of parity $\deg b$.

*Proof.* For the associativity, $(m\cdot b)\cdot c=(-1)^{\deg c(\deg m+\deg b)}(-1)^{\deg b\deg m}c\,b\,m$ and $m\cdot(bc)=(-1)^{(\deg b+\deg c)\deg m}(bc)m$; the two exponents differ by $\deg b\deg c$, and graded-commutativity of $A$ supplies exactly that sign, $cb=(-1)^{\deg b\deg c}bc$. For the compatibility, $a(m\cdot b)=(-1)^{\deg b\deg m}a\,b\,m$ and $(am)\cdot b=(-1)^{\deg b(\deg a+\deg m)}b\,a\,m$, whose exponents differ again by $\deg a\deg b$, supplied by graded-commutativity. The parity is read from $R_b(M_j) \subseteq M_{j+\deg b}$. $\square$

**Corollary.** $R_b=L_b\alpha^{\deg b}$, that is, $R_b=L_b$ for even $b$ and $R_b=L^{\alpha}_b=L_b\alpha$ for odd $b$.

*Proof.* For $b$ even, $R_b(m)=bm=L_b(m)$; for $b$ odd, $R_b(m)=(-1)^{\deg m}bm=b\,\alpha(m)=L_b(\alpha(m))$. $\square$

The theorem is the precise form of the assertion that the grading imposes a sign: without the sign $(-1)^{\deg b\deg m}$ the right action would not be associative, and without graded-commutativity even the signed formula fails.

### The two-sided operators and their parity

**Proposition.** Let ${}_A M_A$ be a graded bimodule with the Koszul right action, and let $S_{a,b}=L_aR_b$ be the unsigned sandwich of *The Signed Sandwich on a Bimodule over an Algebra*. Then

$$
S_{a,b}(M_j) \subseteq M_{j+\deg a+\deg b}, \qquad \alpha\,S_{a,b}\,\alpha^{-1}=(-1)^{\deg a+\deg b}\,S_{a,b},
$$

and $S_{a,b}=L_{ab}\alpha^{\deg b}$. The signed sandwich $S^{\alpha}_{a,b}=S_{a,b}\alpha$ has the same parity $\deg a+\deg b$ and obeys the same sign rule.

*Proof.* $R_b(M_j) \subseteq M_{j+\deg b}$ and $L_a(M_{j+\deg b}) \subseteq M_{j+\deg b+\deg a}$; the sign rule is the proposition above applied to the operator of parity $\deg a+\deg b$. The identity $S_{a,b}=L_aR_b=L_aL_b\alpha^{\deg b}=L_{ab}\alpha^{\deg b}$ uses the corollary. $\square$

Since $\alpha$ has parity $0$ but acts on odd elements by $-1$, the signed sandwich $S^{\alpha}_{a,b}$ is the unsigned one with the middle factor sign-flipped on the odd part; this is the operator form of the Koszul sign, and it agrees with the composition rule of *The Signed Sandwich on a Bimodule over an Algebra*.

## The Graded Endomorphism Algebra

### The grading of the operators

**Definition.** The **graded endomorphism algebra** of $M$ is the direct sum decomposition

$$
\operatorname{End}_R(M)=\operatorname{End}_R(M)_{\bar0}\oplus\operatorname{End}_R(M)_{\bar1}, \qquad \operatorname{End}_R(M)_i=\{T : T(M_j) \subseteq M_{i+j}\}.
$$

**Proposition.** $\operatorname{End}_R(M)$ is a graded $R$-algebra: $\operatorname{End}_i\operatorname{End}_j \subseteq \operatorname{End}_{i+j}$, the identity is even, and $L_a$ has parity $\deg a$. The grade involution acts on it by conjugation, $T\mapsto\alpha T\alpha^{-1}$, and this is an algebra automorphism of order two whose eigenvalue on $\operatorname{End}_i$ is $(-1)^{i}$.

*Proof.* If $S$ has parity $i$ and $T$ has parity $j$, then $ST(M_k)\subseteq S(M_{j+k})\subseteq M_{i+j+k}$, so $\operatorname{End}_i\operatorname{End}_j\subseteq\operatorname{End}_{i+j}$; the identity preserves each $M_j$. The parity of $L_a$ is the proposition on the action. The conjugation is an automorphism because $\alpha$ is invertible, and its eigenvalue is the sign rule above. $\square$

### The graded commutator

The graded endomorphism algebra carries a signed commutator, and the sign rule is the statement that the action is a homomorphism of graded algebras for it.

**Definition.** For homogeneous operators $S,T$ the **graded commutator** is

$$
[S,T]=ST-(-1)^{\deg S\,\deg T}\,TS .
$$

**Proposition.** The graded commutator is graded-alternating, $[S,T]=-(-1)^{\deg S\,\deg T}[T,S]$, it is a graded derivation in each argument,

$$
[S,TT']=[S,T]T'+(-1)^{\deg S\,\deg T}T[S,T'],
$$

and an even operator $T$ is $A$-linear exactly when $[T,L_a]=0$ for all homogeneous $a$.

*Proof.* The alternation is a rewriting of the definition. The derivation identity is the Leibniz rule with the Koszul sign inserted before moving $T$ past $S$, checked by expanding both sides. For the last clause, an even $T$ has $\deg T=0$, so $[T,L_a]=TL_a-L_aT$, whose vanishing is $A$-linearity by *Module Endomorphisms*; for an odd $T$ the graded bracket carries the sign $(-1)^{\deg a}$ and its vanishing is a twisted condition, not $A$-linearity. $\square$

## Examples

**(a) The exterior algebra.** Let $A=\Lambda(V)$ with the usual $\mathbb{Z}/2$-grading by degree parity: it is graded-commutative, so every graded left module acquires the Koszul right action and becomes a graded bimodule. The sign $(-1)^{\deg b\deg m}$ is the sign of the exterior product, and the grade involution is the parity operator.

**(b) A Clifford algebra.** Let $A$ be the Clifford algebra of a quadratic space, graded by the parity of the number of generators. It is not graded-commutative in general, so the Koszul right action of the theorem is available only on modules where the obstruction $bc-(-1)^{\deg b\deg c}cb$ acts trivially; the sign rule for the operators still holds, because it only uses the grade involution.

**(c) The matrix algebra with an even/odd grading.** For $A=M_2(k)$, $J=\operatorname{diag}(1,-1)$, $\alpha(X)=JXJ^{-1}$: the graded-commutativity is vacuous because $A$ is not graded-commutative, and the Koszul right action exists only on modules killed by $[A,A]$-type obstructions. The sign rule $\alpha T\alpha^{-1}=(-1)^{\deg T}T$ holds for every homogeneous operator.

**(d) The group algebra of $\mathbb{Z}/2$.** For $A=k[\mathbb{Z}/2]=k\oplus k\epsilon$ with $\epsilon$ odd and $\epsilon^{2}=1$, the algebra is graded-commutative; every graded module is a graded bimodule with $m\cdot\epsilon=(-1)^{\deg m}\epsilon m$, and $R_\epsilon=L_\epsilon\alpha$. The two-sided operators $S_{1,\epsilon}=L_\epsilon\alpha=L^{\alpha}_\epsilon$ are the signed left multiplications of *The Signed Left Multiplication on a Module over an Algebra*.

**(e) A purely even algebra.** If $A=A_{\bar0}$ then every module is graded with $M=M_{\bar0}$, the grade involution is the identity, the Koszul sign is always $+1$, and all the graded statements reduce to the ungraded ones.

## Summary

A graded algebra $A=A_{\bar0}\oplus A_{\bar1}$ acts on a graded module $M=M_{\bar0}\oplus M_{\bar1}$ with the compatibility $A_iM_j\subseteq M_{i+j}$, equivalently through a grade involution $\alpha$ with $\alpha(am)=\alpha(a)\alpha(m)$; the action is even, sending $A_i$ to the operators of parity $i$. The grading imposes the Koszul sign: for homogeneous $a$, $\alpha L_a\alpha^{-1}=(-1)^{\deg a}L_a$, and for every homogeneous operator $T$, $\alpha T\alpha^{-1}=(-1)^{\deg T}T$. When $A$ is graded-commutative, the sign $R_b(m)=(-1)^{\deg b\deg m}bm$ makes any graded left module a graded bimodule, with $R_b=L_b\alpha^{\deg b}$; without graded-commutativity this right action fails to be associative. The graded endomorphism algebra $\operatorname{End}_R(M)=\operatorname{End}_{\bar0}\oplus\operatorname{End}_{\bar1}$ is a graded algebra on which the grade involution acts by conjugation with eigenvalue $(-1)^{i}$ on $\operatorname{End}_i$, and it carries the graded commutator $[S,T]=ST-(-1)^{\deg S\deg T}TS$, for which the action is a homomorphism of graded algebras. The two-sided sandwiches $S_{a,b}$ have parity $\deg a+\deg b$ and obey the same sign rule.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A_{\bar0}\oplus A_{\bar1}$ | graded $R$-algebra, $A_iA_j\subseteq A_{i+j}$ |
| $M=M_{\bar0}\oplus M_{\bar1}$ | graded left $A$-module, $A_iM_j\subseteq M_{i+j}$ |
| $\deg x \in \mathbb{Z}/2$ | degree of a homogeneous element |
| $\alpha$ | grade involution, $+1$ on the even part, $-1$ on the odd part |
| $(-1)^{\deg s\deg t}$ | the Koszul sign of two homogeneous elements |
| $L_a$, $L^{\alpha}_a$ | unsigned and signed left multiplications |
| $R_b(m)=(-1)^{\deg b\deg m}bm$ | Koszul right multiplication on a graded bimodule |
| $R_b=L_b\alpha^{\deg b}$ | right multiplication in terms of the left one |
| $S_{a,b}=L_aR_b$ | two-sided operator of parity $\deg a+\deg b$ |
| $\alpha T\alpha^{-1}=(-1)^{\deg T}T$ | the sign rule for a homogeneous operator |
| $\operatorname{End}_i$ | operators shifting degree by $i$ |
| $[S,T]=ST-(-1)^{\deg S\deg T}TS$ | the graded commutator |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for gradings, order-two automorphisms and the $\mathbb{Z}/2$-graded structures they define.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the grade involution and its action on operators.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry*, in *Quantum Fields and Strings: A Course for Mathematicians*, American Mathematical Society (1999), for the Koszul sign rule in graded algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, second edition, 2001), for the parity grading of a Clifford algebra and its modules.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for graded modules, the sign rule and the operators built from them.
