
# __The Involution on the Endomorphism Ring of a Module__

## Introduction

A non-degenerate reflexive pairing on a module turns the adjoint of a homomorphism into an operation on the endomorphism ring: the map $f \mapsto f^{*}$ is additive, reverses products and has order two, so it is an **involution** of the ring. This article constructs that involution, identifies the endomorphisms it fixes — the **self-adjoint** ones — and the units it preserves — the **unitary** ones, which are exactly the isometries of the pairing.

The article is the third of the `* Theory` group of this category. It assumes the pairing and the adjoint of *The Adjoint of a Module Homomorphism*, the endomorphism ring of *Module Endomorphisms* and *The Endomorphism Algebra of a Module*, and the involution concept of *Involutive Algebras*. It is the module-level counterpart of *Involutions of the Endomorphism Algebra* in the linear-space category, with the same conventions; the operator-level counterparts, in which the adjoint of a specific operator is computed, are the `* Operator Theory` articles that follow. The article stays inside Part I: no distance, norm, form with a norm, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, $M$ is a left $A$-module with a non-degenerate reflexive $\sigma$-sesquilinear pairing $\langle\cdot,\cdot\rangle$, and $E=\operatorname{End}_A(M)$.

## The Involution Induced by a Pairing

### Construction

**Theorem.** Suppose the pairing is perfect, so that the adjoint of every endomorphism exists. Then the assignment

$$
{}^{*} : E \to E, \qquad f \longmapsto f^{*}, \qquad \langle f(m),n\rangle=\langle m,f^{*}(n)\rangle,
$$

is well defined, $R$-linear, additive, anti-multiplicative and of order two:

$$
(f+g)^{*}=f^{*}+g^{*}, \qquad (fg)^{*}=g^{*}f^{*}, \qquad (f^{*})^{*}=f, \qquad (rf)^{*}=r f^{*} .
$$

Hence $(E,{}^{*})$ is an involutive $R$-algebra: ${}^{*}$ is an involution of $E$ whose fixed part is the set of self-adjoint endomorphisms.

*Proof.* Well-definedness, existence and $A$-linearity of $f^{*}$ are *The Adjoint of a Module Homomorphism*, and the four laws are proved there. An involution of a ring is an anti-automorphism of order two; ${}^{*}$ is additive and $R$-linear, so it is an involution of the $R$-algebra $E$, in the sense of *Involutive Algebras*. $\square$

The involution is not an auxiliary structure: it is the pairing, transported to the operators. Two pairings that are equivalent give the same involution, as the last section shows, and a pairing that is not reflexive fails to give an involution because $(f^{*})^{*}=f$ may fail.

### The adjoint of a composite and the elementary elements

**Proposition.** For all $f_1,\dots,f_k \in E$,

$$
(f_1\cdots f_k)^{*}=f_k^{*}\cdots f_1^{*}, \qquad (\mathrm{id})^{*}=\mathrm{id}, \qquad (L_a)^{*}=L_{\sigma(a)} .
$$

*Proof.* The first is induction from $(fg)^{*}=g^{*}f^{*}$, the second is immediate from the definition, and the third is the computation of the adjoint of a left multiplication in *The Adjoint of a Module Homomorphism*. $\square$

The last identity is the bridge between the involution of the algebra and the involution of the endomorphism ring: the action of $a$ has adjoint the action of $\sigma(a)$.

## Self-Adjoint and Skew-Adjoint Elements

### Definition and decomposition

**Definition.** An endomorphism $f \in E$ is **self-adjoint** when $f^{*}=f$ and **skew-adjoint** when $f^{*}=-f$. The **symmetric part** and the **skew part** of $E$ are

$$
\operatorname{Sym}(M)=\{f : f^{*}=f\}, \qquad \operatorname{Skew}(M)=\{f : f^{*}=-f\}.
$$

Both are $R$-submodules of $E$.

**Theorem.** If $2$ is invertible in $R$, then

$$
E=\operatorname{Sym}(M)\oplus\operatorname{Skew}(M), \qquad f=\tfrac12(f+f^{*})+\tfrac12(f-f^{*}),
$$

and the two summands have intersection $0$.

*Proof.* The displayed decomposition writes $f$ as the sum of a self-adjoint and a skew-adjoint element because ${}^{*}$ is $R$-linear and of order two; if $f$ is both, then $f=-f$ and $2f=0$, so $f=0$ when $2$ is invertible. $\square$

The decomposition is the module-level form of the fixed-and-skew decomposition of an involutive algebra, and it reduces the study of $E$ to the self-adjoint part and the skew-adjoint part separately.

### The self-adjoint part is a Jordan algebra

**Theorem.** The self-adjoint part is closed under the **Jordan product**

$$
f \bullet g=\tfrac12(fg+gf),
$$

and under the square $f \mapsto f^{2}$; it contains the identity. Hence $\operatorname{Sym}(M)$ is a unital Jordan subalgebra of $E$, and it is a **special** Jordan algebra.

*Proof.* If $f^{*}=f$ and $g^{*}=g$ then $(fg+gf)^{*}=g^{*}f^{*}+f^{*}g^{*}=gf+fg=fg+gf$, so $(f\bullet g)^{*}=f\bullet g$; taking $g=f$ gives $f^{2}$ self-adjoint; the identity is self-adjoint. $\square$

The symmetric part of an involutive algebra with this Jordan product is treated in *Involutive Algebras*, which owns the general theory of the involutions and their symmetric elements.

### The matrix description

**Proposition.** Let $M=A^n$ with the standard sesquilinear pairing and identify $E=\operatorname{End}_A(A^n)\cong M_n(A^{\mathrm{op}})$. Then the involution is the transpose-entrywise map

$$
\Theta(X)_{ij}=\sigma(X_{ji}),
$$

of *Modules over an Involutive Algebra*, so the self-adjoint matrices are those with $\Theta(X)=X$ and the skew-adjoint matrices those with $\Theta(X)=-X$.

*Proof.* The adjoint with respect to the standard pairing is the transpose-entrywise map, as computed in *The Adjoint of a Module Homomorphism*. $\square$

A change of basis conjugates the involution, by the basis-dependence statement of *Modules over an Involutive Algebra*, so the matrix description is canonical only for the standard basis; the involution as a map on $E$ is canonical.

## Unitary Elements

### Definition and the group

**Definition.** An endomorphism $u \in E$ is **unitary** when

$$
u^{*}u=uu^{*}=\mathrm{id} .
$$

The set of unitary elements is denoted

$$
U(M)=\{u \in E : u^{*}u=uu^{*}=\mathrm{id}\}.
$$

**Proposition.** $U(M)$ is a subgroup of the group $E^{\times}=\operatorname{Aut}_A(M)$ of units, and it is contained in it: a unitary element is invertible with $u^{-1}=u^{*}$. It is the group of **isometries** of the pairing.

*Proof.* If $u\in U(M)$ then $u^{-1}=u^{*}$ explicitly, so $u\in E^{\times}$. Closure: if $u,v\in U(M)$ then $(uv)^{*}(uv)=v^{*}u^{*}uv=v^{*}v=\mathrm{id}$ and similarly on the other side, so $uv\in U(M)$; the identity is unitary; and $u^{-1}\in U(M)$ because $(u^{*})^{*}=u$ and $u^{*}u=uu^{*}=\mathrm{id}$ read as $u^{*}(u^{*})^{*}=(u^{*})^{*}u^{*}=\mathrm{id}$. $\square$

### The isometry characterisation

**Theorem.** An endomorphism $u$ is unitary if and only if it preserves the pairing:

$$
u \in U(M) \iff \langle u(m),u(n)\rangle=\langle m,n\rangle \quad \text{for all } m,n \in M .
$$

*Proof.* $\langle u(m),u(n)\rangle=\langle m,u^{*}u(n)\rangle$. If $u^{*}u=\mathrm{id}$ this is $\langle m,n\rangle$. Conversely, if the identity holds for all $m,n$, then $\langle m,u^{*}u(n)-n\rangle=0$ for all $m$, so $u^{*}u(n)=n$ by non-degeneracy in the first variable, that is $u^{*}u=\mathrm{id}$; a one-sided inverse in a group of units is two-sided, so $u\in U(M)$. $\square$

Thus the unitary elements are exactly the automorphisms of $M$ that preserve the pairing, and $U(M)$ is the **unitary group** of the pairing; in the classical cases it is the orthogonal group, the unitary group or the symplectic group, as the examples show.

### The unitary orbits and the self-adjoint elements

**Proposition.** For $u \in U(M)$ and $f \in E$,

$$
(u^{*}fu)^{*}=u^{*}f^{*}u, \qquad (ufu^{-1})^{*}=u f^{*}u^{*} .
$$

Consequently $U(M)$ acts on the involutive algebra $E$ by **unitary conjugation**, $f \mapsto ufu^{*}=ufu^{-1}$, and this action preserves self-adjointness, skew-adjointness and the Jordan product. It is the **unitary group of the involutive algebra** $(E,{}^{*})$.

*Proof.* The two identities are anti-multiplicativity and $(u^{*})^{*}=u$; for $u\in U(M)$, $u^{*}=u^{-1}$, so $ufu^{-1}=ufu^{*}$ and conjugation by a unitary element maps $f^{*}$ to $(ufu^{*})^{*}=u f^{*}u^{*}$, preserving the fixed and skew parts; it preserves products and hence the Jordan product. $\square$

## The Involution and the Centre

### The kind of the involution

**Definition.** The involution ${}^{*}$ of $E$ is of the **first kind** when it fixes the centre $Z(E)$ pointwise, and of the **second kind** otherwise.

**Proposition.** ${}^{*}$ is of the first kind exactly when $z^{*}=z$ for every central endomorphism, that is, when the centre is contained in the self-adjoint part; and the induced map on the centre is an involution of $Z(E)$.

*Proof.* ${}^{*}$ restricted to the centre is an $R$-linear anti-automorphism of the commutative ring $Z(E)$, hence an automorphism, of order two; it is the identity precisely in the first-kind case. $\square$

For the standard pairing on $A^n$ the centre is $Z(A)$ acting by scalars, and the induced involution is $z \mapsto \sigma(z)$ up to the identification; hence the involution is of the first kind when $\sigma$ fixes the centre, and of the second kind when it does not. Over a field with $\sigma=\mathrm{id}$ the involution is always of the first kind.

### Relation to the involution of the algebra

**Proposition.** Under the identification $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ of *The Endomorphism Algebra of a Module*, the involution ${}^{*}$ induced by the regular pairing is $\sigma$, so the involutive algebra $(E,{}^{*})$ of the regular module is $(A^{\mathrm{op}},\sigma)$.

*Proof.* The endomorphisms of the regular module are the right multiplications $R_a$, the adjoint of $R_a$ with respect to the regular pairing is $R_{\sigma(a)}$ by *The Adjoint of a Module Homomorphism*, and the identification sends $R_a$ to $a$. $\square$

The involution on the endomorphism ring of a module is therefore not a new notion: for the regular module it is the involution of the algebra, and the construction of this article generalises it to every module with a pairing.

## Dependence on the Pairing

### The involution is canonical for a fixed pairing

**Proposition.** For a fixed pairing the involution ${}^{*}$ is independent of the basis: in a basis with Gram matrix $\Phi$ (so $\langle m,n\rangle=[m]^{\mathsf{T}}\Phi[n]$) the involution reads

$$
[f^{*}]=\Phi^{-1}[f]^{\mathsf{T}}\Phi,
$$

and a change of basis conjugates both $[f]$ and $[f^{*}]$ by the same matrix, so the assignment $f\mapsto f^{*}$ on $E$ is unchanged.

*Proof.* $\langle f(m),n\rangle=[m]^{\mathsf{T}}[f]^{\mathsf{T}}\Phi[n]$ and $\langle m,f^{*}(n)\rangle=[m]^{\mathsf{T}}\Phi[f^{*}][n]$, so $\Phi[f^{*}]=[f]^{\mathsf{T}}\Phi$ and the formula follows; a change of basis replaces $[f]$ by $P^{-1}[f]P$ and $\Phi$ by $P^{\mathsf{T}}\Phi P$, and the two changes cancel in the formula. $\square$

Multiplying the pairing by a unit $\lambda$ also leaves the involution unchanged, since $(\lambda\Phi)^{-1}[f]^{\mathsf{T}}(\lambda\Phi)=\Phi^{-1}[f]^{\mathsf{T}}\Phi$: only the class of the pairing up to scalars matters.

### Different pairings give different involutions

The involution belongs to the pair (ring, pairing), not to the ring alone.

**Example.** On $M=k^2$ let the first pairing be the standard symmetric one, $\langle x,y\rangle=x_1y_1+x_2y_2$ with Gram matrix $I$, and the second the alternating one, $\langle x,y\rangle=x_1y_2-x_2y_1$ with Gram matrix $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. The first involution is the transpose, whose fixed space is the three-dimensional space of symmetric matrices; the second is $T\mapsto J^{-1}T^{\mathsf{T}}J$, and a direct computation shows that its fixed space is the one-dimensional space of scalars. Two involutions of a ring with fixed parts of different dimensions are not isomorphic, so the same ring $M_2(k)$ carries two non-isomorphic involutions, induced by two pairings.

The classification of the involutions a module's endomorphism ring can carry, and the question of when two pairings induce isomorphic involutions, is the subject of *Involutions of the Module Endomorphism Ring* in the `* Operator Theory` group. When the two pairings are the same up to a change of basis the involution is the same, by the proposition above; beyond that, two pairings can induce non-isomorphic involutions, as the example shows.

## Examples

**(a) The orthogonal group.** For $A=R$ a field, $M=R^n$ and the standard bilinear pairing $\langle x,y\rangle=\sum x_iy_i$, the involution is the transpose, the self-adjoint elements are the symmetric matrices, the skew-adjoint the alternating ones, and $U(M)=O(n)$.

**(b) The unitary group.** For $A=\mathbb{C}$, $M=\mathbb{C}^n$ and the sesquilinear pairing $\langle x,y\rangle=\sum x_i\overline{y_i}$, the involution is the conjugate transpose, the self-adjoint elements are the hermitian matrices, and $U(M)=U(n)$.

**(c) The symplectic group.** For $M=R^{2n}$ with the alternating pairing $\langle x,y\rangle=\sum_i(x_iy_{i+n}-x_{i+n}y_i)$, the involution is $(f^{*})^{*}=f$ with $f^{*}=J^{-1}f^{\mathsf{T}}J$, and $U(M)=Sp(2n)$.

**(d) The regular module of a division ring.** For $M=A=D$ a division ring with $\langle a,b\rangle=\sigma(a)b$, the involution on $\operatorname{End}_D(D)\cong D^{\mathrm{op}}$ is $\sigma$, the self-adjoint elements are the symmetric elements of $D$, and $U(D)=\{u : \sigma(u)u=1\}$ is the unitary group of $D$.

**(e) A matrix algebra.** For $A=M_n(\mathbb{C})$ with the conjugate transpose involution and $M=A$ as the regular module, the involution on $E\cong A^{\mathrm{op}}$ is the conjugate transpose, the self-adjoint elements are the hermitian matrices, and the unitary group is the classical $U(n)$ acting by right multiplication.

## Summary

A non-degenerate reflexive $\sigma$-sesquilinear pairing on a left $A$-module $M$ induces the adjoint map $f\mapsto f^{*}$ on $E=\operatorname{End}_A(M)$, which is $R$-linear, additive, anti-multiplicative and of order two, hence an involution of the $R$-algebra $E$; on the regular module it is the involution $\sigma$ of the algebra, and on a free module with the standard pairing it is the transpose-entrywise map $\Theta(X)_{ij}=\sigma(X_{ji})$. The fixed part is the set of self-adjoint endomorphisms, the negative-fixed part the skew-adjoint ones, and when $2$ is invertible $E$ is their direct sum; the self-adjoint part is closed under the Jordan product $f\bullet g=\frac12(fg+gf)$, hence a special Jordan algebra. The unitary elements $u$ with $u^{*}u=uu^{*}=\mathrm{id}$ form a subgroup $U(M)$ of the unit group, equal to the group of isometries of the pairing, and they act on $E$ by unitary conjugation, preserving the involution and its symmetric part; in the classical cases $U(M)$ is $O(n)$, $U(n)$ or $Sp(2n)$. The involution is of the first kind when it fixes the centre and of the second kind otherwise, and equivalent pairings induce conjugate involutions, so the same ring can carry several inequivalent involutions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $A$, $\sigma$ | base ring, involutive $R$-algebra, involution |
| $M$, $\langle\cdot,\cdot\rangle$ | module and non-degenerate reflexive σ-sesquilinear pairing |
| $E=\operatorname{End}_A(M)$ | the endomorphism ring |
| $f^{*}$ | the adjoint, $\langle f(m),n\rangle=\langle m,f^{*}(n)\rangle$ |
| $\operatorname{Sym}(M)$, $\operatorname{Skew}(M)$ | self-adjoint and skew-adjoint endomorphisms |
| $f\bullet g=\frac12(fg+gf)$ | the Jordan product on the self-adjoint part |
| $U(M)=\{u : u^{*}u=uu^{*}=\mathrm{id}\}$ | the unitary group |
| $\langle u(m),u(n)\rangle=\langle m,n\rangle$ | the isometry characterisation of unitarity |
| $Z(E)$ | the centre of the endomorphism ring |
| first kind, second kind | involution fixing or moving the centre |
| $\Theta(X)_{ij}=\sigma(X_{ji})$ | the matrix form on a free module |
| $L_a^{*}=L_{\sigma(a)}$ | the adjoint of a left multiplication |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for involutions, sesquilinear forms and their unitary groups.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for involutions of rings and the classical groups.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for involutions, symmetric elements and their Jordan structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for involutions of the first and second kind and the unitary groups they define.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for ring involutions, their fixed parts and matrix examples.
