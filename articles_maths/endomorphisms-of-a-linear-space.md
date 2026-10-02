# __Endomorphisms of a Linear Space__

## Introduction

The endomorphisms of a linear space $V$ are the linear maps $V \to V$, and they carry two operations at once: they may be added, because a sum of linear maps is linear, and they may be composed, because a composite of linear maps is linear. Under these two operations they form a ring that is also a linear space over the field — an $F$-algebra — and this algebra is the object of the present article. It is the first of the **operator algebras** of the corpus, and it fixes the vocabulary of the whole operator layer of this category: the multiplication, the units, the idempotents, the nilpotents, the centre, the opposite, and the ambient space in which the operators on it live.

The individual endomorphism is treated in *Linear Maps and Matrices*: its kernel, image and rank, its matrix, and the rank–nullity theorem are there, and none of them is reproved. The group of units is treated in *The General Linear Group*: the group of automorphisms, its centre, its action on subspaces and its projective quotient are there. What is established here is the algebra that these maps form, its structure, and the two-sided regular representation that makes the algebra act on itself by left and right multiplication.

The article assumes a field $F$, a finite-dimensional $F$-linear space $V$ of dimension $n$, the algebra of linear maps $\operatorname{Hom}_F(V,W)$ and the identification of an endomorphism with its matrix from *Linear Maps and Matrices*, the vocabulary of rings, units, ideals, idempotents and nilpotents from *Rings*, and the modules over a field that make an $F$-algebra from *Algebras*. It uses no form, no norm and no distance; a pairing occurs nowhere in it, and the trace pairing that the later adjoint articles use is introduced in *The Adjoint of the Left Multiplication on a Linear Space*.

The article is organised in three parts: the algebra itself and its elementary structure, its elements of special type — the units, the idempotents, the nilpotents, the zero divisors — and its global structure, namely its centre, its two-sided ideals, its opposite, and its place as the space on which its own multiplication acts. Throughout, products in $\operatorname{End}_F(V)$ are compositions and are written by juxtaposition, $AB = A \circ B$, so that $(AB)(x) = A(B(x))$; the identity is $\mathrm{id}_V$, and the standard basis of the matrix algebra is the family $E_{ij}$.

## The Algebra of Endomorphisms

### Definition

**Definition.** The **endomorphism algebra** of $V$ is the set

$$
E = \operatorname{End}_F(V) = \operatorname{Hom}_F(V,V)
$$

of $F$-linear maps $V \to V$, with the addition $(A+B)(x) = A(x)+B(x)$ and the multiplication $AB = A \circ B$ given by composition.

**Proposition.** $E$ is a unital associative $F$-algebra, non-commutative as soon as $\dim_F V \ge 2$, and of dimension

$$
\dim_F E = n^2 .
$$

**Proof.** The sum and the composite of linear maps are linear, so both operations are defined on $E$; addition is commutative and associative, composition is associative, and the distributive laws hold because composition of maps distributes over addition of maps. The identity $\mathrm{id}_V$ is a two-sided unit. The identification of $E$ with $\operatorname{Hom}_F(V,V)$, which is a linear space of dimension $n \cdot n$ by *Linear Maps and Matrices*, gives the dimension. For non-commutativity, the maps with matrices $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ in a basis of a two-dimensional space do not commute, and they are supplemented by the identity on the remaining $n-2$ basis vectors.

**Remark (the two operations are of different kinds).** Addition is defined pointwise, so it uses only the abelian group of $V$; composition uses the fact that the source and the target of a linear map coincide, and it is not defined for $\operatorname{Hom}_F(V,W)$ when $V \neq W$. The algebra $E$ is thus the first place in the corpus where a linear space carries a second operation, and the multiplication records the composition of the structure maps of $V$ rather than any extra datum on $V$.

### The Matrix Model

Fix an ordered basis $v_1,\dots,v_n$ of $V$ and let $E_{ij}$ be the endomorphism sending $v_j$ to $v_i$ and every other basis vector to $0$. Its matrix has a single $1$ in position $(i,j)$, so the assignment $A \mapsto [A]$ is an isomorphism of algebras

$$
E \longrightarrow M_n(F),
$$

and $\{E_{ij} : 1 \le i,j \le n\}$ is a basis of $E$. The multiplication is read from the elementary products

$$
E_{ij}E_{kl} = \delta_{jk}E_{il},
$$

where $\delta_{jk}$ is the Kronecker delta. The isomorphism is not canonical: it depends on the basis, and a change of basis conjugates the matrices as in *Linear Maps and Matrices*.

**Example.** For $n=1$ the algebra $E$ is $F$ itself, commutative; for $n=2$ it is $M_2(F)$, of dimension $4$. The four matrices $E_{11},E_{12},E_{21},E_{22}$ multiply by the rule above, and in particular $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$, which is the smallest display of a product of two elements depending on the order.

## The Elements of Special Type

### Units

**Proposition.** The group of units of $E$ is the general linear group,

$$
E^{\times} = \operatorname{GL}(V),
$$

and an endomorphism is a unit if and only if it is injective, if and only if it is surjective.

**Proof.** An element of $E$ is a unit exactly when it has a two-sided inverse in $E$, which is exactly when it is a bijection, and a bijection with linear inverse is an automorphism; that is *The General Linear Group*. For a linear endomorphism of a finite-dimensional space, injective, surjective and bijective coincide, by the rank–nullity theorem of *Linear Maps and Matrices*.

**Proposition (non-units are zero divisors).** In the finite-dimensional algebra $E$, every element that is not a unit is a zero divisor: if $A \notin \operatorname{GL}(V)$ then there are nonzero $B,C \in E$ with $AB=0$ and $CA=0$.

**Proof.** If $A$ is not invertible then $\ker A \neq 0$ and $A(V) \neq V$. Choose $u \neq 0$ with $Au = 0$ and a nonzero $w \in V$ with $Aw = 0$; a nonzero $w$ exists because $A$ is not injective. For $B$ take an endomorphism with $B(V) \subseteq \ker A$, possible and nonzero because $\ker A \neq 0$; then $AB=0$. For $C$ take an endomorphism with $u$ in its image and with $C$ vanishing on $A(V)$; such a $C$ is nonzero, since $u \neq 0$, and $CA=0$ because $C$ kills $A(V)$.

### Idempotents and Projections

**Definition.** An **idempotent** of $E$ is an element $P$ with $P^2 = P$, and a **projection** is an idempotent of $E$; a **nilpotent** is an element $N$ with $N^k = 0$ for some $k \ge 1$.

**Proposition (idempotents and decompositions).** An endomorphism $P \in E$ is an idempotent if and only if

$$
V = \ker P \oplus \operatorname{im}P ,
$$

and then $P$ acts as the identity on $\operatorname{im}P$ and as zero on $\ker P$. Conversely, for every direct decomposition $V = U \oplus W$ there is exactly one idempotent of $E$ with image $U$ and kernel $W$, namely the projection along $W$ onto $U$.

**Proof.** If $P^2=P$ and $x \in V$, write $x = (x-Px)+Px$; the first term lies in $\ker P$ because $P(x-Px) = Px - P^2x = 0$, and the second in $\operatorname{im}P$; the sum is direct because if $Px=0$ then $x-Px=x$. On $\operatorname{im}P$ the map $P$ is the identity: if $x=Py$ then $Px=P^2y=Py=x$. Conversely, if $V=U\oplus W$, define $P$ on $U$ as the identity and on $W$ as zero; then $P$ is linear, $P^2=P$, $\operatorname{im}P=U$ and $\ker P=W$, and the uniqueness holds because a linear map is determined on a decomposition by its values on the summands.

**Proposition (rank of an idempotent).** An idempotent $P$ has $\operatorname{rk}P = \operatorname{tr}P$, and in a basis adapted to the decomposition $V = \operatorname{im}P \oplus \ker P$ its matrix is $\operatorname{diag}(I_r,0)$ with $r = \operatorname{rk}P$.

**Proof.** The matrix statement follows from the proposition; the trace of $\operatorname{diag}(I_r,0)$ is $r$, the rank, and both trace and rank are invariant under the change of basis, as *Linear Maps and Matrices* records.

### Nilpotents

**Proposition.** An endomorphism $N$ is nilpotent if and only if every eigenvalue of $N$ is $0$, equivalently if and only if its characteristic polynomial is $x^n$. For $n \ge 2$ there are nonzero nilpotents, the smallest being the map with matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ on a two-dimensional space.

**Proof.** If $N^k=0$ and $Nv=\lambda v$ with $v \neq 0$, then $0=N^kv=\lambda^kv$, so $\lambda=0$. Conversely, if the only eigenvalue is $0$ then the characteristic polynomial is $x^n$, and the Cayley–Hamilton theorem of *Eigenvalues and Diagonalisation* gives $N^n=0$. The displayed map satisfies $N^2=0$ and $N \neq 0$.

**Remark.** A nonzero nilpotent is neither a unit nor an idempotent, so the three families overlap only at $0$: an element with $P^2=P$ and $P^k=0$ is $0$, since $P = P^k = 0$ for $k \ge 2$.

## The Global Structure

### The Centre

**Proposition.** If $V \neq 0$ then the centre of $E$ is the line of scalar endomorphisms,

$$
Z(E) = \{\lambda\,\mathrm{id}_V : \lambda \in F\} \cong F .
$$

**Proof.** A scalar endomorphism commutes with every endomorphism. Conversely, let $A$ commute with every element of $E$ and let $v \neq 0$. If $v$ and $Av$ were linearly independent they would extend to a basis of a subspace, and an endomorphism $B$ with $B(Av)=v+Av$ and $B(v)=v$ would satisfy $BAv=v+Av$ while $ABv=Av$, a contradiction; hence $Av = \lambda_v v$. For a second vector $u$ the same argument applied to the pair gives $Au = \lambda_u u$, and applying the commutation with an endomorphism carrying $u$ to $v$ shows $\lambda_u = \lambda_v$; alternatively, if $u,v$ are independent then $A(u+v)=\lambda_{u+v}(u+v)$ forces $\lambda_u=\lambda_v$, and if they are dependent the equality is immediate. Hence all $\lambda_v$ agree and $A$ is scalar. This is the computation of *The General Linear Group*, valid here for the whole algebra rather than for its units.

### Ideals and Simplicity

**Definition.** A **two-sided ideal** of $E$ is a linear subspace $I$ with $EIE \subseteq I$; an algebra with no nonzero proper two-sided ideal is **simple** (the notion is that of *Rings*).

**Theorem.** The algebra $E = \operatorname{End}_F(V)$ is simple, and its centre is $F$; equivalently, $E$ is a central simple $F$-algebra.

**Proof.** Let $I \neq 0$ be a two-sided ideal and let $0 \neq A \in I$. Choose $v$ with $Av = w \neq 0$. For $u \in V$ and $\varphi \in V^{*}$ write $u \otimes \varphi$ for the rank-one endomorphism $x \mapsto \varphi(x)u$. Then

$$
(u \otimes \varphi)\,A\,(v \otimes \psi) = \varphi(Av)\,(u \otimes \psi) ,
$$

because $(v\otimes\psi)(x) = \psi(x)v$, then $A$ sends it to $\psi(x)Av$, then $u\otimes\varphi$ sends it to $\varphi(\psi(x)Av)u = \psi(x)\varphi(Av)u$. Choose $\varphi$ with $\varphi(Av) \neq 0$, which is possible because $Av \neq 0$; then for all $u,\psi$ the ideal $I$ contains a nonzero multiple of $u \otimes \psi$. The rank-one endomorphisms $u \otimes \psi$ span $E$, so $I = E$. The centre was computed above, so $E$ is central simple.

**Corollary.** Every nonzero $A \in E$ generates $E$ as a two-sided ideal, $EAE = E$; there is no nontrivial quotient algebra of $E$ by a two-sided ideal.

### The Opposite Algebra

**Definition.** The **opposite algebra** $E^{\mathrm{op}}$ is the same linear space $E$ with the multiplication $A \cdot^{\mathrm{op}} B = BA$.

**Proposition.** $E^{\mathrm{op}}$ is an algebra, the identity map is an anti-isomorphism $E \to E^{\mathrm{op}}$, and a map $E \to E$ that is additive and reverses products is the composite of an algebra homomorphism $E^{\mathrm{op}} \to E$ with this identification.

**Proof.** Reversing the order of a product preserves associativity: $(A\cdot^{\mathrm{op}}B)\cdot^{\mathrm{op}}C = C(BA) = (CB)A = A\cdot^{\mathrm{op}}(B\cdot^{\mathrm{op}}C)$. The rest is the definition of the opposite and of an anti-homomorphism.

**Remark (the transpose is deferred).** The algebra $E$ is isomorphic to its opposite, and the standard anti-isomorphism witnessing it is the transpose, $A \mapsto A^{\mathsf{T}}$, taken with respect to a fixed basis; the intrinsic form of that map, the dual endomorphism on $V^{*}$, and the contravariant functor it defines are the subject of *The Transpose of a Linear Map*, the next article of this group, and they are not used here.

### The Ambient Operator Space

The operator layer of the corpus begins at this algebra, and the operators on it form the ambient space of the later articles.

**Definition.** An **operator** on $E$ is an $F$-linear map $E \to E$; the operators form the algebra $\operatorname{End}_F(E)$, of dimension $n^4$.

**Proposition (the regular representation).** For $A \in E$ the maps

$$
L_A : E \longrightarrow E, \quad L_A(X) = AX , \qquad R_A : E \longrightarrow E, \quad R_A(X) = XA
$$

are $F$-linear; $L_A L_B = L_{AB}$, $R_A R_B = R_{BA}$, $L_A R_B = R_B L_A$ for all $A,B \in E$, and the assignments $A \mapsto L_A$ and $A \mapsto R_{A}$ exhibit $E$ and $E^{\mathrm{op}}$ as subalgebras of $\operatorname{End}_F(E)$. Both are injective when $E$ is unital, with $L_A = 0$ forcing $A = L_A(\mathrm{id}_V) = 0$.

**Proof.** Linearity is the distributivity of composition over addition in $E$; the composition laws are associativity, $L_AL_B(X) = A(BX) = (AB)X = L_{AB}(X)$, and the same read in reverse for $R$; the commutation is associativity again, $L_AR_B(X) = A(XB) = (AX)B = R_BL_A(X)$.

**Remark.** The operator space $\operatorname{End}_F(E)$ is strictly larger than $E$: its dimension is $n^4$ while that of $E$ is $n^2$, and for $n \ge 2$ there are operators on $E$, such as a derivation or an algebra automorphism that is not inner, that are not left or right multiplications. The subalgebras of $\operatorname{End}_F(E)$ and, inside them, the centralizers and the commutants of the image of $E$ are the subject of *Algebras of Endomorphisms*.

## Summary

The endomorphisms of a finite-dimensional linear space $V$ over a field $F$ form, under addition and composition, the unital associative $F$-algebra $E = \operatorname{End}_F(V)$ of dimension $n^2$; after a basis is fixed it is the matrix algebra $M_n(F)$ with the elementary multiplication $E_{ij}E_{kl} = \delta_{jk}E_{il}$. Its units are the automorphisms, $E^{\times} = \operatorname{GL}(V)$, and every non-unit is a zero divisor. Its idempotents are exactly the projections onto a direct summand along a complement, and an idempotent has rank equal to its trace; its nilpotents are the endomorphisms with vanishing spectrum, and the three families of units, idempotents and nilpotents meet only at $0$. The centre of $E$ is the line $F\,\mathrm{id}_V$ of scalars, and $E$ is a central simple $F$-algebra: every nonzero element generates $E$ as a two-sided ideal, so $E$ has no nonzero proper two-sided ideal and no nontrivial quotient. The algebra is isomorphic to its opposite by an anti-isomorphism, whose intrinsic form is the transpose deferred to the next article. Finally, $E$ acts on itself on the left and on the right by the multiplications $L_A(X)=AX$ and $R_A(X)=XA$, which commute and make $E$ and $E^{\mathrm{op}}$ subalgebras of the strictly larger operator algebra $\operatorname{End}_F(E)$ of dimension $n^4$; this is the ambient space of the operator layer of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars |
| $V$ | an $F$-linear space of finite dimension $n$ |
| $E = \operatorname{End}_F(V)$ | the endomorphism algebra, of dimension $n^2$ |
| $AB = A \circ B$ | the product is composition, $(AB)(x) = A(B(x))$ |
| $\mathrm{id}_V$ | the identity endomorphism, the unit of $E$ |
| $E_{ij}$ | the endomorphism with matrix having a single $1$ in position $(i,j)$ |
| $M_n(F)$ | the matrix algebra, isomorphic to $E$ after a basis is fixed |
| $\delta_{jk}$ | the Kronecker delta |
| $E^{\times} = \operatorname{GL}(V)$ | the units of $E$, the general linear group |
| $P$ | an idempotent, $P^2=P$; a projection of $V$ |
| $N$ | a nilpotent, $N^k=0$ |
| $Z(E) = F\,\mathrm{id}_V$ | the centre of $E$ |
| $I$ | a two-sided ideal, $EIE \subseteq I$ |
| $E^{\mathrm{op}}$ | the opposite algebra, $A \cdot^{\mathrm{op}} B = BA$ |
| $A^{\mathsf{T}}$ | the transpose with respect to a basis, deferred to the next article |
| $L_A$, $R_A$ | left and right multiplication by $A$ on $E$, $L_A(X)=AX$, $R_A(X)=XA$ |
| $u \otimes \varphi$ | the rank-one endomorphism $x \mapsto \varphi(x)u$ |
| $\operatorname{End}_F(E)$ | the operator algebra on $E$, of dimension $n^4$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the endomorphism ring of a module, its centre and its idempotents.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the endomorphism algebra of a vector space and the structure of matrix algebras.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the units, the zero divisors and the simplicity of matrix algebras over a field.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for the elementary properties of endomorphisms, projections and nilpotents.
- Nathan Jacobson, *Lectures in Abstract Algebra*, volume II: *Linear Algebra* (Van Nostrand, 1953), for the endomorphism algebra, its regular representation and its place among the operator algebras.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the structure of central simple algebras over a field.
- Joseph J. Rotman, *Advanced Modern Algebra* (American Mathematical Society, 2nd ed. 2010), for the ring-theoretic vocabulary of units, ideals, idempotents and nilpotents applied to endomorphism algebras.
