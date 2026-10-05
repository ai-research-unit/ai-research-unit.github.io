
# __The Adjoint of a Module Homomorphism__

## Introduction

A pairing between two modules lets a homomorphism be moved from one side of the pairing to the other, and the operator it becomes is its **adjoint**. This article defines the adjoint with respect to a non-degenerate reflexive pairing, proves existence and uniqueness, computes its kernel and image as the paired complements of the image and kernel of the original homomorphism, and identifies it with the transpose in the bilinear case. It also separates the two ways the adjoint can be taken — the left and the right adjoint — and shows that for a reflexive pairing they coincide.

The article is the second of the `* Theory` group of this category. It assumes the modules and the operator layer of *Modules over an Involutive Algebra*, *Left and Right Multiplication of a Module* and *Module Endomorphisms*, and it assumes the involutive algebra of *Involutive Bilinear Algebras*. The pairing here is the abstract pairing named in *Modules over an Involutive Algebra*; the involution it induces on the whole endomorphism ring, its self-adjoint part and its unitary group are the subject of the next article, *The Involution on the Endomorphism Ring of a Module*. The article stays inside Part I: no distance, norm, form, topology or limit, and *pairing* means a biadditive map, not a form with a norm. Throughout, $R$ is a commutative ring with $1 \neq 0$, $A$ is a unital associative $R$-algebra with involution $\sigma$, $M$ and $N$ are left $A$-modules, and the pairing is written $\langle\cdot,\cdot\rangle$.

## The Pairing

### Sesquilinear pairings

**Definition.** A **$\sigma$-sesquilinear pairing** between left $A$-modules $M$ and $N$ is a biadditive map

$$
\langle\cdot,\cdot\rangle : M \times N \to R,
$$

such that for all $a \in A$, $m \in M$, $n \in N$,

$$
\langle am, n\rangle=\langle m,\sigma(a)n\rangle, \qquad\text{equivalently}\qquad \langle m, an\rangle=\langle\sigma(a)m,n\rangle .
$$

When $\sigma=\mathrm{id}$ the pairing is **bilinear**. The pairing is **non-degenerate** when

$$
\langle m,N\rangle=0 \implies m=0, \qquad \langle M,n\rangle=0 \implies n=0,
$$

and **reflexive** when there is a sign $\varepsilon \in \{1,-1\}$ with $\langle n,m\rangle=\varepsilon\langle m,n\rangle$ for all $m \in M$, $n \in N$.

The second display in the definition follows from the first by replacing $a$ with $\sigma(a)$ and using $\sigma^{2}=\mathrm{id}$. Non-degeneracy says that the two maps $m \mapsto \langle m,\cdot\rangle$ and $n \mapsto \langle\cdot,n\rangle$ have trivial kernels, so each of $M$ and $N$ detects the other; reflexivity says the pairing is symmetric or alternating up to a sign.

### The standard examples

**(a) The bilinear square.** For $A=R$ commutative and $\sigma=\mathrm{id}$, every $R$-module is an $A$-module, and a bilinear pairing is an ordinary $R$-bilinear form. The standard one on $R^n$ is $\langle x,y\rangle=\sum_i x_iy_i$.

**(b) The regular pairing of an involutive algebra.** For $M=N=A$ with the product, the map $\langle a,b\rangle=\sigma(a)\,b$ is additive in each variable and satisfies the sesquilinear identity; it is non-degenerate when $A$ is a division ring and is the model for the forms of *Hermitian Forms over an Involution Ring*, which owns them.

**(c) The evaluation pairing.** For $N=M^{\vee}=\operatorname{Hom}_R(M,R)$ with the twisted structure, $\langle m,\varphi\rangle=\varphi(m)$ is the evaluation pairing; it is bilinear and non-degenerate when $M$ is a finite free $R$-module.

## The Adjoint

### Existence and uniqueness

**Theorem.** Let $\langle\cdot,\cdot\rangle$ be a non-degenerate pairing on the pairs $(M,M)$ and $(N,N)$, and let $f : M \to N$ be $A$-linear. Suppose that for every $n \in N$ the functional $m \mapsto \langle f(m),n\rangle$ is represented by an element of $M$; that is, there is $f^{*}(n) \in M$ with

$$
\langle f(m),n\rangle=\langle m,f^{*}(n)\rangle \qquad (m \in M).
$$

Then $f^{*}(n)$ is unique, the assignment $n \mapsto f^{*}(n)$ is $A$-linear, and

$$
f^{*} \in \operatorname{Hom}_A(N,M).
$$

*Proof.* Uniqueness: if $g^{*}(n)$ also represents the functional, then $\langle m,f^{*}(n)-g^{*}(n)\rangle=0$ for all $m$, so $f^{*}(n)=g^{*}(n)$ by non-degeneracy in the first variable. $A$-linearity: for the left action, $\langle m,f^{*}(an)\rangle=\langle f(m),an\rangle=\langle\sigma(a)f(m),n\rangle$ by the sesquilinear identity; since $f$ is $A$-linear, $\sigma(a)f(m)=f(\sigma(a)m)$, so this is $\langle f(\sigma(a)m),n\rangle=\langle\sigma(a)m,f^{*}(n)\rangle=\langle m,a f^{*}(n)\rangle$; non-degeneracy gives $f^{*}(an)=a f^{*}(n)$. Additivity is the same argument applied to the sum. $\square$

When $M=N$ and the pairing is non-degenerate, the representing element always exists after one adds the hypothesis used below, namely that the pairing be **perfect**: every $R$-linear functional on $M$ of the form $m \mapsto \langle m,n\rangle$ is represented. For finite free modules over a field, or more generally for modules with a non-degenerate pairing and a dual basis, this holds; the theorem is stated with the hypothesis explicit.

### The elementary laws

**Theorem.** For a perfect non-degenerate reflexive pairing, the adjoint is additive, anti-multiplicative, involutive and $R$-linear:

$$
(f+g)^{*}=f^{*}+g^{*}, \qquad (fg)^{*}=g^{*}f^{*}, \qquad (f^{*})^{*}=f, \qquad (rf)^{*}=r f^{*}.
$$

*Proof.* Additivity and $R$-linearity follow from the defining identity and uniqueness. For the product, $\langle fg(m),n\rangle=\langle g(m),f^{*}(n)\rangle=\langle m,g^{*}(f^{*}(n))\rangle$, so $(fg)^{*}=g^{*}f^{*}$ by uniqueness. For order two, reflexivity gives $\langle f^{*}(n),m\rangle=\varepsilon\langle m,f^{*}(n)\rangle=\varepsilon\langle f(m),n\rangle=\langle n,f(m)\rangle$, so $f$ represents the functional defining $(f^{*})^{*}$; uniqueness gives $(f^{*})^{*}=f$. $\square$

The assignment $f \mapsto f^{*}$ is therefore an involution of the endomorphism ring when $M=N$, which is the subject of *The Involution on the Endomorphism Ring of a Module*; the article here treats the adjoint as an operator.

### The adjoint of the one-sided multiplications

**Proposition.** Let $M$ be a left $A$-module with a non-degenerate reflexive $\sigma$-sesquilinear pairing. Then for every $a \in A$, the adjoint of the left multiplication $L_a$ on $M$, when it exists, is

$$
L_a^{*}=L_{\sigma(a)} .
$$

*Proof.* $\langle L_a(m),n\rangle=\langle am,n\rangle=\langle m,\sigma(a)n\rangle=\langle m,L_{\sigma(a)}(n)\rangle$, so $L_{\sigma(a)}$ represents the functional, and uniqueness gives the identity. $\square$

The formula is the reason the involution of the algebra and the adjoint of the module are one construction: applying the adjoint to the action applies $\sigma$ to the scalar.

## Kernel, Image and the Paired Complement

### Paired complements

**Definition.** For a submodule $U \subseteq M$ and a submodule $V \subseteq N$,

$$
U^{\mathrm{c}}=\{n \in N : \langle U,n\rangle=0\}, \qquad {}^{\mathrm{c}}V=\{m \in M : \langle m,V\rangle=0\}.
$$

Both are submodules, the first of $N$ and the second of $M$.

**Proposition.** $U^{\mathrm{c}}$ and ${}^{\mathrm{c}}V$ are submodules, and for a reflexive pairing $(U^{\mathrm{c}})^{\mathrm{c}}=U$ and ${}^{\mathrm{c}}({}^{\mathrm{c}}V)=V$. When $M$ and $N$ have a finite length function and the pairing is non-degenerate, the length is complementary, $\ell(U^{\mathrm{c}})=\ell(N)-\ell(U)$, and the assignment $U \mapsto U^{\mathrm{c}}$ is an order-reversing bijection.

*Proof.* The submodule statements are immediate from biadditivity; reflexivity gives the double-complement identities as in the linear-space case, because $\langle m,n\rangle=\varepsilon\langle n,m\rangle$ makes the two kernels dual; for the length formula, the map $N \to U^{\vee}$, $n \mapsto \langle\cdot,n\rangle$, has kernel $U^{\mathrm{c}}$ and image the functionals represented on $U$, which for a perfect pairing is all of $U^{\vee}$, so the length is complementary. $\square$

### The kernel and the image

**Theorem.** For a homomorphism $f : M \to N$ with adjoint $f^{*} : N \to M$,

$$
\ker f^{*}=(\operatorname{im}f)^{\mathrm{c}}, \qquad \operatorname{im}f^{*}={}^{\mathrm{c}}(\ker f).
$$

*Proof.* $f^{*}(n)=0$ means $\langle m,f^{*}(n)\rangle=0$ for all $m$, that is $\langle f(m),n\rangle=0$ for all $m$, which says $n \in (\operatorname{im}f)^{\mathrm{c}}$; this is the first identity. For the second, $\langle m,f^{*}(n)\rangle=\langle f(m),n\rangle$ vanishes for all $n$ exactly when $f(m) \in {}^{\mathrm{c}}N$, that is $m \in \ker f$, so ${}^{\mathrm{c}}(\operatorname{im}f^{*})=\ker f$; taking complements gives the identity. $\square$

**Corollary.** If $M$ and $N$ have equal finite length and the pairing is non-degenerate and perfect, then $\ell(\ker f^{*})=\ell(\ker f)$ and $\ell(\operatorname{im}f^{*})=\ell(\operatorname{im}f)$: the adjoint preserves the length of the kernel, the image and the cokernel.

*Proof.* $\ell(\ker f^{*})=\ell((\operatorname{im}f)^{\mathrm{c}})=\ell(N)-\ell(\operatorname{im}f)=\ell(M)-\ell(\operatorname{im}f)=\ell(\ker f)$, using the length formula and $\ell(M)=\ell(N)$. The image statement follows from $\ell(\operatorname{im}f^{*})=\ell(M)-\ell(\ker f^{*})$. $\square$

**Corollary (invertibility).** $f$ is invertible if and only if $f^{*}$ is, and then $(f^{-1})^{*}=(f^{*})^{-1}$; the adjoint of the identity is the identity, and the adjoint of the scalar $r \in R$ is $r$.

*Proof.* Length preservation makes invertibility correspond; from $ff^{-1}=\mathrm{id}$ and anti-multiplicativity, $(f^{-1})^{*}f^{*}=\mathrm{id}$ and $f^{*}(f^{-1})^{*}=\mathrm{id}$, which is the inverse statement. The last clauses are the definitions. $\square$

## The Transpose

### The evaluation pairing

In the bilinear case the adjoint of a homomorphism with respect to the evaluation pairing is the transpose.

**Proposition.** Let $A=R$ be commutative, $\sigma=\mathrm{id}$, and let $N=M^{\vee}=\operatorname{Hom}_R(M,R)$ with the evaluation pairing $\langle m,\varphi\rangle=\varphi(m)$. Then for $f : M \to M$ the adjoint with respect to the evaluation pairing is the transpose

$$
f^{\mathrm{t}} : M^{\vee} \to M^{\vee}, \qquad f^{\mathrm{t}}(\varphi)=\varphi \circ f .
$$

*Proof.* $\langle f(m),\varphi\rangle=\varphi(f(m))=(f^{\mathrm{t}}\varphi)(m)=\langle m,f^{\mathrm{t}}\varphi\rangle$, so $f^{\mathrm{t}}$ represents the functional and is the adjoint by uniqueness. $\square$

The transpose is contravariant, $(fg)^{\mathrm{t}}=g^{\mathrm{t}}f^{\mathrm{t}}$, and involutive when $M$ is reflexive, in agreement with the general laws.

### The matrix form

**Proposition.** Let $M=R^n$ with the standard pairing $\langle x,y\rangle=\sum_i x_iy_i$, and let $f$ have matrix $X$. Then $f^{*}$ has matrix $X^{\mathsf{T}}$. If instead the pairing has Gram matrix $\Phi$, then $[f^{*}]=\Phi^{-1}X^{\mathsf{T}}\Phi$.

*Proof.* The identity $\langle Xx,y\rangle=\langle x,X^{\mathsf{T}}y\rangle$ is the definition of the transpose; conjugating by the Gram matrix replaces the standard pairing by a general one. $\square$

In the $\sigma$-sesquilinear case the matrix description acquires $\sigma$: the adjoint of a matrix is the conjugate transpose, and its precise form for a module over an involutive algebra is the matrix involution $\Theta(X)_{ij}=\sigma(X_{ji})$ of *Modules over an Involutive Algebra* when the pairing is the standard one on $A^n$.

## The Left and the Right Adjoint

### The two definitions

The defining identity moves $f$ from the first to the second variable. There is a second way to move it, and the two agree for a reflexive pairing.

**Definition.** Let $f \in \operatorname{Hom}_A(M,N)$ with adjoint $f^{*}$ defined by $\langle f(m),n\rangle=\langle m,f^{*}(n)\rangle$. A **left adjoint** of $f$ is a map ${}^{*}f \in \operatorname{Hom}_A(N,M)$ with

$$
\langle n,f(m)\rangle=\langle {}^{*}f(n),m\rangle \qquad (m \in M,\ n \in N).
$$

**Proposition.** For a reflexive pairing the left adjoint exists, is unique, and equals the adjoint: ${}^{*}f=f^{*}$. Without reflexivity, a left adjoint may fail to exist, and when it exists it differs from the adjoint by the reflexivity defect.

*Proof.* Using $\langle n,f(m)\rangle=\varepsilon\langle f(m),n\rangle=\varepsilon\langle m,f^{*}(n)\rangle=\langle f^{*}(n),m\rangle$, the map $f^{*}$ satisfies the defining identity of ${}^{*}f$, so it is a left adjoint; uniqueness is the same non-degeneracy argument as for the adjoint. Conversely, if $\langle n,f(m)\rangle$ is not proportional to $\langle f(m),n\rangle$, nothing guarantees a representing element. $\square$

Thus for the pairings used here the words *left adjoint* and *right adjoint* name the same operator; the distinction is real only for a pairing without reflexivity, and in the sesquilinear case it is the involution $\sigma$ that relates the two conventions.

### Relation to the transpose

**Corollary.** In the bilinear case with the evaluation pairing, the left adjoint of $f$ is its transpose on the dual. In the $\sigma$-sesquilinear case, the adjoint with respect to the pairing $\langle m,n\rangle$ and the adjoint with respect to the pairing $\langle n,m\rangle$ are related by $\sigma$ on the coefficients.

*Proof.* The first clause is the transpose proposition; the second restates the sesquilinear identity $L_a^{*}=L_{\sigma(a)}$ in the two conventions. $\square$

## Examples

**(a) The standard form.** For $A=R$ commutative, $M=R^n$ and $\langle x,y\rangle=\sum x_iy_i$, the adjoint is the transpose, $\ker f^{*}=(\operatorname{im}f)^{\perp}$ and $\operatorname{im}f^{*}=(\ker f)^{\perp}$.

**(b) The symplectic form.** For $M=R^2$ with $\langle x,y\rangle=x_1y_2-x_2y_1$, the pairing is reflexive with sign $\varepsilon=-1$, and the adjoint of a matrix $X$ is $J^{-1}X^{\mathsf{T}}J$ with $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$; the length identities hold and the self-adjoint endomorphisms are the symplectic Lie algebra.

**(c) The regular pairing.** For $M=N=A$ a division ring with $\langle a,b\rangle=\sigma(a)b$, the adjoint of the left multiplication $L_a$ is $L_{\sigma(a)}$, and the adjoint of the right multiplication $R_b$ is $R_{\sigma(b)}$; the pairing is reflexive with sign $\varepsilon=1$ when $\sigma$ fixes the coefficient ring.

**(d) The involution induced by a free basis.** For $M=A^n$ with the standard sesquilinear pairing, the adjoint of a matrix is $\Theta(X)_{ij}=\sigma(X_{ji})$, the involution of *Modules over an Involutive Algebra*; the basis-independent description of that involution is exactly the adjoint with respect to the standard pairing.

## Summary

A $\sigma$-sesquilinear pairing between left $A$-modules $M$ and $N$ is a biadditive map with $\langle am,n\rangle=\langle m,\sigma(a)n\rangle$; it is non-degenerate when each module detects the other and reflexive when $\langle n,m\rangle=\varepsilon\langle m,n\rangle$. For an $A$-linear $f : M \to N$ the adjoint $f^{*} : N \to M$ is defined by $\langle f(m),n\rangle=\langle m,f^{*}(n)\rangle$; it exists and is unique when the pairing is non-degenerate and the functional is represented, and it is $A$-linear. The adjoint is additive, anti-multiplicative, $R$-linear and of order two, and it carries $L_a$ to $L_{\sigma(a)}$. It is described by the paired complements: $\ker f^{*}=(\operatorname{im}f)^{\mathrm{c}}$ and $\operatorname{im}f^{*}={}^{\mathrm{c}}(\ker f)$, so with a finite length function and a perfect pairing it preserves the lengths of the kernel, image and cokernel, and it preserves invertibility with $(f^{-1})^{*}=(f^{*})^{-1}$. In the bilinear case with the evaluation pairing the adjoint is the transpose, with matrix $X^{\mathsf{T}}$ for the standard pairing and $\Phi^{-1}X^{\mathsf{T}}\Phi$ for the pairing with Gram matrix $\Phi$. The left and the right adjoint coincide for a reflexive pairing and differ otherwise, the difference in the sesquilinear case being governed by $\sigma$. The involution the adjoint defines on $\operatorname{End}_A(M)$ is the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$ | unital associative $R$-algebra with involution $\sigma$ |
| $M$, $N$ | left $A$-modules |
| $\langle\cdot,\cdot\rangle$ | $\sigma$-sesquilinear pairing, $\langle am,n\rangle=\langle m,\sigma(a)n\rangle$ |
| $\varepsilon$ | the reflexivity sign, $\langle n,m\rangle=\varepsilon\langle m,n\rangle$ |
| $f^{*}$ | the adjoint, $\langle f(m),n\rangle=\langle m,f^{*}(n)\rangle$ |
| $U^{\mathrm{c}},{}^{\mathrm{c}}V$ | paired complements |
| $\ker f^{*}=(\operatorname{im}f)^{\mathrm{c}}$ | kernel of the adjoint |
| $\operatorname{im}f^{*}={}^{\mathrm{c}}(\ker f)$ | image of the adjoint |
| $L_a$, $R_b$ | left and right multiplications |
| $L_a^{*}=L_{\sigma(a)}$ | the adjoint of a left multiplication |
| $f^{\mathrm{t}}$ | the transpose on the dual, for the evaluation pairing |
| $\Phi$ | Gram matrix, $[f^{*}]=\Phi^{-1}X^{\mathsf{T}}\Phi$ |
| ${}^{*}f$ | the left adjoint, equal to $f^{*}$ for a reflexive pairing |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for sesquilinear forms, duality and adjoints.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for pairings of modules over a ring and the transpose.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for the adjoint of an endomorphism with respect to a bilinear form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for hermitian forms over an involutive ring and the adjoints they define.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for dual modules, non-degenerate pairings and their kernels.
