# __Modules over an Involutive Ring__

## Introduction

A left module over a ring with an involution has a right module hidden in it — the same additive group with the action read through the involution — and the passage between the two is an equivalence of categories. The involution also reaches the dual of a module and the endomorphism ring of a free module, where it produces the transpose-with-the-involution, the self-adjoint matrices and the unitary matrices. This article develops the twist by an involution, the dual of a module over an involutive ring, and the induced involution on the endomorphisms, which is the ring-level form of the adjoint involution that the pairing-based articles define over a field.

*Involutive Rings* supplies the definition of an involution, the fixed and skew elements, the anti-automorphism of order two and the opposite ring; *Modules*, *Direct Sums, Free Modules and Rank* and *The Balanced Product* supply the module theory, the free modules, the rank and the tensor product. *Endomorphisms of a Linear Space* treats the algebra of endomorphisms of a linear space, and *Involutions of the Endomorphism Algebra* treats the adjoint involution from a non-degenerate pairing; the present article is the ring-level companion, and the pairing is deferred to Part II. The forms themselves, the sesquilinear pairings on a module and the Hilbert structure, are *Hilbert Algebras*.

Throughout, $A$ is a ring with $1 \neq 0$ with an involution $\sigma$, $M$ is a left $A$-module, and $R$ is a commutative ring with an involution $\sigma$ when commutativity is needed. The fixed set $A^{\sigma}$ and the two conjugates $a$ and $\sigma(a)$ are those of *Involutive Rings*. No form, no norm and no topology is used.

## The Twist by an Involution

**Definition.** For a left $A$-module $M$ let $M^{\sigma}$ be the same additive group with the right action

$$
x \cdot a = \sigma(a)\,x \qquad (x \in M^{\sigma},\ a \in A) .
$$

**Proposition.** $M^{\sigma}$ is a right $A$-module; the assignment $M \mapsto M^{\sigma}$ is an additive, exact, contravariant equivalence between the categories of left and of right $A$-modules, with inverse the same construction applied to the involution $\sigma$ of $A^{\mathrm{op}}$.

**Proof.** For the right-module axioms, $(x\cdot a)\cdot b = \sigma(b)(\sigma(a)x) = (\sigma(b)\sigma(a))x = \sigma(ab)x = x\cdot(ab)$, using $\sigma(ab)=\sigma(b)\sigma(a)$; and $x\cdot 1 = \sigma(1)x = x$. Additivity in $x$ and exactness are inherited from $M$, because the underlying additive group and the underlying maps are unchanged. Applying the construction twice returns the original left action, $x\cdot a\cdot b = \sigma(b)\sigma(a)x$, which is the associativity of $M$. The construction is the identity on morphisms, so it is an equivalence.

**Corollary (over a commutative ring the twist is a left module).** If $A = R$ is commutative then $M^{\sigma}$, with $a\cdot x = \sigma(a)x$, is again a left $R$-module, and the two readings agree, because $\sigma$ is multiplicative when the ring is commutative.

**Proof.** $(ab)\cdot x = \sigma(ab)x = \sigma(a)\sigma(b)x = a\cdot(b\cdot x)$; the two actions coincide because reading the right action $x\cdot a = \sigma(a)x$ as a left action gives the same formula in the commutative case.

## The Dual Module

**Definition.** For a left $A$-module $M$ the **dual module** is $M^{*} = \operatorname{Hom}_A(M,A)$, with the left action

$$
(a \cdot \varphi)(x) = \varphi(x)\,\sigma(a) .
$$

**Proposition.** $M^{*}$ is a left $A$-module under the action above, and the **evaluation pairing**

$$
\langle \cdot,\cdot\rangle : M^{*} \times M \longrightarrow A, \qquad \langle \varphi,x\rangle = \varphi(x) ,
$$

satisfies $\langle a\cdot\varphi,x\rangle = \langle\varphi,x\rangle\sigma(a)$ and $\langle\varphi,a\cdot x\rangle = a\langle\varphi,x\rangle$; it is $\sigma$-sesquilinear in this sense, and it is non-degenerate when $M$ is free of finite rank.

**Proof.** For the module axioms, $a\cdot(b\cdot\varphi)(x) = (b\cdot\varphi)(x)\sigma(a) = \varphi(x)\sigma(b)\sigma(a) = \varphi(x)\sigma(ab) = (ab)\cdot\varphi(x)$, and $1\cdot\varphi = \varphi$. For the sesquilinearity, the two displayed identities are the definitions of the two actions; non-degeneracy for a free module of finite rank is the statement that a functional is determined by its values on a basis and that every assignment on a basis extends, so a functional vanishing on all of $M$ is $0$ and a vector killed by all functionals is $0$.

**Proposition (the dual functor).** For a homomorphism $f : M \to N$ of left $A$-modules the **transpose** $f^{*} : N^{*} \to M^{*}$, $f^{*}\psi = \psi \circ f$, is a homomorphism of left $A$-modules, $(g f)^{*} = f^{*}g^{*}$ and $\mathrm{id}^{*} = \mathrm{id}$; the dual is therefore a contravariant functor from left $A$-modules to left $A$-modules, and it is the ring-level form of the transposition of *The Transpose of a Linear Map*.

**Proof.** Additivity and $\sigma$-compatibility of $f^{*}\psi$ are the definitions; the composition law and the identity law are the same computation as for vector spaces, $(g f)^{*}\psi = \psi g f = f^{*}(g^{*}\psi)$.

## The Induced Involution on the Endomorphisms

**Definition.** For the free left $A$-module $M = A^{n}$ with its standard basis, the endomorphism ring $\operatorname{End}_A(A^{n})$ is identified with the matrix ring $M_n(A)$, and the **induced map** is

$$
A^{*} = \sigma(A)^{\mathsf{T}}, \qquad (A^{*})_{ij} = \sigma(A_{ji}) .
$$

**Proposition.** The assignment $A \mapsto A^{*}$ is additive and of order two. It is an involution of the ring $M_n(A)$ in the sense of *Involutive Rings* — an anti-automorphism of order two — exactly when $A$ is commutative, and in that case the fixed matrices are the **$\sigma$-self-adjoint** ones and the **unitary** matrices are those with $A^{*}A = AA^{*} = I$.

**Proof.** Additivity and order two are immediate from the entries. For multiplicativity, $(AB)^{*} = \sigma(AB)^{\mathsf{T}} = (\sigma(B)\sigma(A))^{\mathsf{T}} = \sigma(A)^{\mathsf{T}}\sigma(B)^{\mathsf{T}} = A^{*}B^{*}$ in general, the two anti-maps cancelling; when $A$ is commutative $\sigma$ is multiplicative and the computation gives $(AB)^{*} = B^{*}A^{*}$, which is the anti-automorphism law. The fixed and unitary descriptions are the definitions.

**Remark (the general ring: an automorphism, not an involution).** Over a non-commutative ring the map $A \mapsto \sigma(A)^{\mathsf{T}}$ is the composite of the anti-automorphism $\sigma$ and the anti-isomorphism transpose, hence an **automorphism** of order two, not an involution in the corpus sense; the anti-automorphism of order two on the endomorphism ring of a free module over a general involutive ring is the transpose alone, $A \mapsto A^{\mathsf{T}}$, which needs no involution. The involution of the endomorphism ring that the pairings produce, and its classification, are *Involutions of the Endomorphism Algebra*, and the sesquilinear pairing that identifies $M$ with $M^{*}$ and turns the transpose into an adjoint is *Hilbert Algebras*.

**Remark (the diagram of the two dualities).** The dual functor and the twist fit together: the double dual of a module over an involutive ring recovers the module only through an identification $M \cong M^{**}$ given by the evaluation $\varphi \mapsto \varphi(x)$, which is $\sigma$-semilinear on the module variable; the comparison of the dual duality with the pairing duality is the content of *The Involution on the Dual Operator* for the linear case.

## Summary

A ring $A$ with involution $\sigma$ turns every left $A$-module $M$ into a right $A$-module $M^{\sigma}$ by $x\cdot a = \sigma(a)x$, and the construction is an exact contravariant equivalence between left and right modules; over a commutative ring the twisted action is again a left action. The dual $M^{*} = \operatorname{Hom}_A(M,A)$ is a left $A$-module under $(a\cdot\varphi)(x) = \varphi(x)\sigma(a)$, and the evaluation pairing is $\sigma$-sesquilinear, non-degenerate for a free module of finite rank; the transpose $f \mapsto f^{*}$ is a contravariant functor. On the endomorphism ring of the free module $A^{n}$, identified with $M_n(A)$, the map $A \mapsto \sigma(A)^{\mathsf{T}}$ is additive of order two; it is an involution of the matrix ring over a commutative ring, with the $\sigma$-self-adjoint and the unitary matrices as its fixed and its unitary elements, and over a general ring it is an automorphism of order two, the anti-involution being the transpose alone. The pairing-based involution of the endomorphism algebra and the forms themselves are objects of the `*`-operator group and of Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\sigma$ | a ring with $1\neq0$ and an involution |
| $A^{\sigma}$ | the fixed set of $\sigma$ |
| $R$ | a commutative ring with involution $\sigma$ |
| $M$ | a left $A$-module |
| $M^{\sigma}$ | the twisted right module, $x\cdot a=\sigma(a)x$ |
| $M^{*}=\operatorname{Hom}_A(M,A)$ | the dual module |
| $(a\cdot\varphi)(x)=\varphi(x)\sigma(a)$ | the left action on the dual |
| $\langle\varphi,x\rangle=\varphi(x)$ | the evaluation pairing, $\sigma$-sesquilinear |
| $f^{*}=\psi\mapsto\psi f$ | the transpose, a contravariant functor |
| $A^{*}=\sigma(A)^{\mathsf{T}}$ | the induced map on $M_n(A)$ |
| $A^{*}A=AA^{*}=I$ | the unitary matrices of the commutative case |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the duality of modules and the transpose.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutive rings, dual modules and sesquilinear pairings.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions of rings and of endomorphism rings.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the module theory of rings with involution and the dual functor.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the exactness of the dual and the tensor–hom adjunction.
