# __Adjoints of Bounded Sesquilinear Operators__

## Introduction

A sesqualgebra carries a two-variable map that costs nothing and that the layer reads as its form: the **canonical pairing** $h(x,y)=x^{*}y$ of *Hermitian Forms on a Sesqualgebra*, $\mathbb{K}$-valued in the sense that it takes values in the algebra, conjugate-linear in the first slot and linear in the second, and Hermitian, $h(y,x)=h(x,y)^{*}$. The present article develops the adjoint of a bounded operator against this pairing. The adjoint of a bounded linear $T$ is the operator $T^{\dagger}$ with $h(Tx,y)=h(x,T^{\dagger}y)$; the adjoint of a bounded conjugate-linear $S$ is taken by the twisted rule $h(Sx,y)=h(x,S^{\dagger}y)^{*}$, which is the rule that preserves the parity. The pairing is nondegenerate on a unital object, so an adjoint is unique when it exists; what is new with respect to Part I is that **it need not exist**, because the pairing is $A$-valued and carries no cyclicity.

Two facts organise the article. The adjointable bounded linear operators are exactly the **left multiplications** $L_{a}(x)=ax$, and the adjoint is the map $a\mapsto a^{*}$ on the parameter; the right multiplications and the two-sided operators are adjointable only in the degenerate cases where the parameter is central. So the adjoint operation is an anti-automorphism of order two of the adjointable subalgebra, $\varsigma$-semilinear on the linear operators, and it is the topological Hilbert-module fact that the adjointable endomorphisms of the algebra as a module over itself are the left multiplications. The second fact is the obstruction for a conjugate-linear operator: the twisted rule is available in principle, but a conjugate-linear bounded operator is adjointable only when it is the right sandwich $S_{1,c}$, $S(x)=x^{*}c$, and the parameter satisfies $c^{*}[x,y]=0$ for all $x,y$ (so an adjointable conjugate-linear operator is self-adjoint), and in the full noncommutative case the only such operator is zero; the pairing that makes the adjoint exist is the scalar reduction $h_{\tau}(x,y)=\tau(x^{*}y)$ of the $A$-valued form by a continuous central functional $\tau$, for which the whole Part I theory is recovered.

**The boundaries.** The canonical $A$-valued form and its two orientations are *Hermitian Forms on a Sesqualgebra*; the reductions to the scalar forms are *The Sesquilinear Form and the Conjugation*, and the adjoint under such a form is *The Adjoint under a Hermitian Form*; the algebraic model, with a trace pairing and a perfect form, is *The Sesquilinear Adjoint Operator*, whose formulas $L_{a}^{\dagger}=S_{1,a}$, for its conjugate left multiplication $L_{a}(x)=ax^{*}$, and $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$ are the ones the reduction recovers; the bounded operators, their two parities, the norm and the graded algebra are *Bounded Operators on a Sesqualgebra*; the one-sided and two-sided families are *The Bounded Left and Right Multiplication Operators of a Sesqualgebra* and *The Bounded Sesquilinear Sandwich*; and the product-preserving operators are *Unitary Operators of a Banach Sesqualgebra*. This article stops before the spectral theory of the later entries.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ with the continuous involution $\varsigma$, and $A$ is a **normed sesqualgebra** of *Banach Sesqualgebras*: the standard example $x\star y=xy^{*}$ of an involutive normed algebra with submultiplicative norm, isometric involution $\lVert x^{*}\rVert=\lVert x\rVert$ and $\lVert1\rVert=1$. The bounded $\mathbb{K}$-linear operators are $B(A)$, the bounded $\varsigma$-semilinear operators are $B^{\varsigma}(A)$, and $\mathcal{B}(A)=B(A)\oplus B^{\varsigma}(A)$ is the graded Banach algebra they generate, all of *Bounded Operators on a Sesqualgebra*; the operator norm is written $\lVert\cdot\rVert$. The **canonical pairing** is

$$
h(x,y)=x^{*}y,
$$

and the derived product is $x\star y=xy^{*}$. The operator families are $L_{a}(x)=ax$, $R_{b}(x)=xb^{*}$, $T_{p,q}(x)=pxq$ and $S_{a,b}(x)=ax^{*}b$. Here $L_{a}$ multiplies by the **associative** product; *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, following Part I, writes $L_{a}(x)=a\star x=ax^{*}$ for the multiplication by the derived product, which is the conjugate left multiplication $S_{a,1}$ of the families above, and it is that operator, not $L_{a}$, which the trace formulas of Part I adjoint. A continuous functional $\tau:A\to\mathbb{K}$ is **central** when $\tau(uv)=\tau(vu)$ for all $u,v$ and **compatible** when $\tau(u^{*})=\varsigma(\tau(u))$.

## The Canonical Pairing

### The Parities, the Hermitian Property and the Radical

**Definition.** The **canonical pairing** of a sesqualgebra is the $A$-valued map $h(x,y)=x^{*}y$.

**Proposition (the two parities and the Hermitian property).** For $x,y\in A$ and $\lambda\in\mathbb{K}$,

$$
h(\lambda x,y)=\varsigma(\lambda)\,h(x,y), \qquad h(x,\lambda y)=\lambda\,h(x,y), \qquad h(y,x)=h(x,y)^{*}.
$$

**Proof.** The first two are the semilinearity of the involution and the linearity of the product in the second slot; the third is $h(y,x)=y^{*}x=(x^{*}y)^{*}=h(x,y)^{*}$, by the anti-multiplicativity of $*$ and $*^{2}=\mathrm{id}$. $\square$

**Proposition (nondegeneracy on a unital object).** The left radical $\{x:h(x,y)=0\ \forall y\}$ and the right radical $\{y:h(x,y)=0\ \forall x\}$ of $h$ are trivial, because $h(x,1)=x^{*}$ and $h(1,y)=y$. Hence an adjoint, when it exists, is unique.

**Proof.** If $h(x,y)=0$ for every $y$ then $x^{*}=h(x,1)=0$, so $x=0$; if $h(x,y)=0$ for every $x$ then $y=h(1,y)=0$. Uniqueness of an adjoint is the triviality of the radicals: two adjoints of the same operator differ by an operator whose values lie in the right radical. $\square$

**Remark (the two orientations).** The companion form of *Hermitian Forms on a Sesqualgebra* is $\Phi(x,y)=xy^{*}=h(y^{*},x^{*})^{*}$, the same datum read through the involution with the slots exchanged. The article uses $h$, conjugate-linear in the first slot; the formulas of the companion orientation follow by transporting along the involution, and every statement below is read on $h$.

**Remark (no cyclicity).** The trace pairing $\varphi(x,y)=\tau(xy^{*})$ of Part I is a **scalar** form, and its adjoint operation uses the cyclicity $\tau(uv)=\tau(vu)$. The canonical pairing is $A$-valued and has no cyclicity: $h(xa,y)=a^{*}h(x,y)$ while $h(x,ya)=h(x,y)a$, and the two differ by the commutator. This single difference is the source of every restriction of the article.

### The Adjoint Relation

**Definition.** A bounded linear $T\in B(A)$ is **adjointable** when there is $T^{\dagger}\in B(A)$ with

$$
h(Tx,y)=h(x,T^{\dagger}y)\qquad\text{for all }x,y\in A;
$$

a bounded $\varsigma$-semilinear $S\in B^{\varsigma}(A)$ is **adjointable** when there is $S^{\dagger}\in B^{\varsigma}(A)$ with the twisted rule

$$
h(Sx,y)=h(x,S^{\dagger}y)^{*}\qquad\text{for all }x,y\in A .
$$

**Remark (why the twist).** For a conjugate-linear operator the linear rule has no solution: replacing $x$ by $\lambda x$ gives $\lambda h(Sx,y)=\varsigma(\lambda)h(x,Uy)$, and a $\lambda$ with $\varsigma(\lambda)\neq\lambda$ forces the pairing to vanish, as *The Sesquilinear Adjoint Operator* proves for a scalar form. The twisted rule carries the two scalars consistently and preserves the parity, as the next section shows. Both rules are the definitions of the article.

## The Adjoint of a Bounded Linear Operator

### The Adjointable Operators are the Left Multiplications

**Theorem (the characterisation).** A bounded linear $T$ is adjointable if and only if it is a left multiplication, $T=L_{c}$ with $c=T(1)$; then

$$
L_{c}^{\dagger}=L_{c^{*}},\qquad\text{that is,}\qquad L_{c}^{\dagger}(y)=c^{*}y .
$$

**Proof.** Suppose $T^{\dagger}$ exists. Replace $x$ by $xa$ in the defining identity: on the left, $h(T(xa),y)=(T(xa))^{*}y$, and on the right, $h(xa,T^{\dagger}y)=a^{*}h(x,T^{\dagger}y)=a^{*}\bigl((Tx)^{*}y\bigr)=a^{*}(Tx)^{*}y$. The two are equal for every $y$, so $(T(xa))^{*}=a^{*}(Tx)^{*}$ and, taking the involution, $T(xa)=(Tx)\,a$: the operator is right $A$-linear. Evaluating at $x=1$ gives $T(a)=T(1)a$, and replacing $a$ by $x$ gives $T=L_{T(1)}$. Conversely $L_{c}$ is bounded with $\lVert L_{c}\rVert=\lVert c\rVert$, and $h(L_{c}x,y)=(cx)^{*}y=x^{*}c^{*}y=x^{*}(c^{*}y)=h(x,L_{c^{*}}y)$, so $L_{c}$ is adjointable with adjoint $L_{c^{*}}$. $\square$

**Corollary (the adjointable subalgebra).** The adjointable bounded linear operators are exactly $\{L_{c}:c\in A\}$, a closed subalgebra of $B(A)$ isometrically isomorphic to $A$; the right multiplications $R_{b}$ are adjointable exactly when $b$ is central, and the two-sided operators $T_{p,q}$ exactly when $q$ is central.

**Proof.** The set is the image of the isometry $c\mapsto L_{c}$ of *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, hence closed and isometric to $A$. For $R_{b}(x)=xb^{*}$ the defining identity evaluated at $x=1$ forces $R_{b}^{\dagger}=L_{b}$, and the remaining condition is $b x^{*}=x^{*}b$ for every $x$, that is the centrality of $b$; then $R_{b}^{\dagger}=L_{b}$. The case of $T_{p,q}=L_{p}R_{q^{*}}$ follows from the composite law below and the centrality of $q^{*}$. $\square$

**Remark (the contrast with Part I).** Over the trace pairing of *The Sesquilinear Adjoint Operator* every bounded operator is adjointable, because the pairing is perfect and cyclicity moves any parameter; over the canonical pairing only the left multiplications are, and the cyclicity is what the reduction to a scalar form restores. The characterisation is nonetheless the exact topological analogue of the Hilbert-module fact that the adjointable operators on the regular module of a Hilbert module are its module endomorphisms, the left multiplications being those of the algebra over itself.

### The Anti-Automorphism

**Theorem (the adjoint operation).** On the adjointable operators the assignment $T\mapsto T^{\dagger}$ is a $\varsigma$-semilinear anti-automorphism of order two: for adjointable $S,T$ and $\lambda\in\mathbb{K}$,

$$
(S+T)^{\dagger}=S^{\dagger}+T^{\dagger},\qquad (\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger},\qquad (ST)^{\dagger}=T^{\dagger}S^{\dagger},\qquad (T^{\dagger})^{\dagger}=T,\qquad \mathrm{id}^{\dagger}=\mathrm{id}.
$$

**Proof.** Additivity is the additivity of $h$ in the slot that carries the operator; the scalar law is $h((\lambda T)x,y)=\varsigma(\lambda)h(Tx,y)=\varsigma(\lambda)h(x,T^{\dagger}y)=h(x,\varsigma(\lambda)T^{\dagger}y)$, using the linearity of $h$ in the second slot; the composite law is $h(STx,y)=h(Tx,S^{\dagger}y)=h(x,T^{\dagger}S^{\dagger}y)$; the law of order two is the defining identity read with the two arguments exchanged together with the Hermitian property $h(y,x)=h(x,y)^{*}$; and the identity is plainly self-adjoint. On the parameters the laws read $L_{c}^{\dagger}=L_{c^{*}}$, and $a\mapsto a^{*}$ is the involution. $\square$

**Remark.** The operation is $\varsigma$-semilinear and not $\mathbb{K}$-linear, exactly as in *The Sesquilinear Adjoint Operator*: an adjoint operation can be twisted by the pairing or by the elements, and here the twist $\varsigma$ of the base survives on the linear component. In the bilinear case $\varsigma=\mathrm{id}$ it is an ordinary involution of the adjointable subalgebra.

## The Adjoint of a Bounded Conjugate-Linear Operator

### The Twisted Rule and the Parity

**Theorem (parity preservation and the composite laws).** Let $S,S'\in B^{\varsigma}(A)$ be adjointable. Then $S^{\dagger}$ is $\varsigma$-semilinear, so the operation preserves the parity, and for the bounded linear $T$,

$$
(S+S')^{\dagger}=S^{\dagger}+S'^{\dagger},\qquad (\lambda S)^{\dagger}=\lambda S^{\dagger},\qquad (TS)^{\dagger}=S^{\dagger}T^{\dagger},\qquad (ST)^{\dagger}=T^{\dagger}S^{\dagger},\qquad (S^{\dagger})^{\dagger}=S .
$$

**Proof.** The scalar laws are the two scalar laws of the pairing: $h((\lambda S)x,y)=\lambda h(Sx,y)=\lambda h(x,S^{\dagger}y)^{*}=h(x,\lambda S^{\dagger}y)^{*}$, which gives $(\lambda S)^{\dagger}=\lambda S^{\dagger}$. For the parity, replace $y$ by $\lambda y$ in the defining identity: the left side is $h(Sx,\lambda y)^{*}=\bigl(\lambda h(Sx,y)\bigr)^{*}=\varsigma(\lambda)h(Sx,y)^{*}$ and the right is $h\bigl(x,S^{\dagger}(\lambda y)\bigr)^{*}$, so $h\bigl(x,S^{\dagger}(\lambda y)\bigr)=\varsigma(\lambda)h(x,S^{\dagger}y)$ and the nondegeneracy gives $S^{\dagger}(\lambda y)=\varsigma(\lambda)S^{\dagger}y$. The composite laws follow by applying the two defining rules in the two orders, with the twists cancelling in pairs, and the law of order two is the definition with the Hermitian property. $\square$

**Remark (the two scalar laws).** The operation is $R$-linear on the conjugate-linear operators and $\varsigma$-semilinear on the linear ones: $(\lambda S)^{\dagger}=\lambda S^{\dagger}$ against $(\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger}$. This is the split of *The Sesquilinear Adjoint Operator*, §*The Two Parities*, and it is the reason one symbol $\dagger$ serves for the two parities.

**Remark (where the conjugate-linear laws bite).** For the canonical pairing $h$ the theorem above is vacuous in its conjugate-linear part: by the collapse of the next section the only adjointable conjugate-linear operator is $0$. The laws are realized for the reduction $h_{\tau}$ and for the trace pairing of Part I, where every bounded operator is adjointable. Each law is an identity of the pairing and holds whenever the adjoints that appear exist.

### The Existence Criterion and the Obstruction

**Theorem (the criterion for a conjugate-linear operator).** Let $S\in B^{\varsigma}(A)$ be adjointable for $h$. Then $S$ is conjugate-$A$-linear in the sense $S(xa)=a^{*}S(x)$ for all $x,a$, so $S(x)=x^{*}c$ with $c=S(1)$, that is $S=S_{1,c}$; and $S$ is adjointable if and only if $c^{*}[x,y]=0$ for all $x,y$, in which case $S^{\dagger}=S_{1,c}=S$, so an adjointable conjugate-linear operator is self-adjoint.

**Proof.** Replace $x$ by $xa$ in the twisted identity $h(Sx,y)=h(x,S^{\dagger}y)^{*}$: on the left, $h(S(xa),y)=\bigl(S(xa)\bigr)^{*}y$, and on the right, $h(xa,S^{\dagger}y)^{*}=\bigl(a^{*}h(x,S^{\dagger}y)\bigr)^{*}=h(x,S^{\dagger}y)\,a=(Sx)^{*}y\,a$, the last equality by the twisted rule. Equal for every $y$, so $\bigl(S(xa)\bigr)^{*}=(Sx)^{*}a$ and, taking the involution, $S(xa)=a^{*}Sx$; at $x=1$ this is $S(a)=a^{*}S(1)$, so $S(x)=x^{*}c$ with $c=S(1)$, which is $S=S_{1,c}$. For the criterion, put $x=1$: on the one hand $h(S1,y)=h(c,y)=c^{*}y$, on the other $h(1,S^{\dagger}y)^{*}=(S^{\dagger}y)^{*}$, so $(S^{\dagger}y)^{*}=c^{*}y$ and $S^{\dagger}y=(c^{*}y)^{*}=y^{*}c=S_{1,c}(y)$. Substituting $S=S^{\dagger}=S_{1,c}$, the identity reads $c^{*}xy=c^{*}yx$ for all $x,y$, that is $c^{*}[x,y]=0$, and then $S^{\dagger}=S_{1,c}=S$. $\square$

**Corollary (the collapse in the full case).** Let $A=M_{n}(\mathbb{K})$ with $n\ge2$, the matrix model of the layer, so that the commutators span the trace-zero matrices. Then the only adjointable conjugate-linear operator is $0$, and in particular the involution $S_{1,1}$ has no adjoint.

**Proof.** By the theorem an adjointable $S$ is $S_{1,c}$ and $c^{*}[x,y]=0$ for all $x,y$. The commutators $[E_{ik},E_{kk}]=E_{ik}$ for $i\neq k$ give $c^{*}E_{ik}=0$, so every off-diagonal entry of $c^{*}$ vanishes, and $[E_{kk},E_{jj}]=E_{kk}-E_{jj}$ gives $c^{*}(E_{kk}-E_{jj})=0$, so all diagonal entries of $c^{*}$ are equal: hence $c^{*}=\lambda I$ is a scalar, and $c^{*}[x,y]=\lambda[x,y]=0$ for all $x,y$ forces $\lambda=0$ in a noncommutative algebra. Thus $c^{*}=0$, $c=0$, and $S=0$. $\square$

**Remark (the two adjoints coincide).** For a $\varsigma$-semilinear $S$ there are the adjoint, taken against $h$, and the **left adjoint** ${}^{\dagger}S$, taken against the transposed pairing $h^{t}(x,y)=h(y,x)$; they exist together and

$$
{}^{\dagger}S=S^{\dagger},
$$

because the pairing is Hermitian: $h(y,Sx)=h(Sx,y)^{*}=h(x,S^{\dagger}y)=h(S^{\dagger}y,x)^{*}$, the last equality being the Hermitian property read in the second slot, which is the defining identity of the left adjoint with ${}^{\dagger}S=S^{\dagger}$. The two adjoints of a conjugate-linear operator are therefore one operation, the rank-two split of the general sesquilinear pairing collapsing for the Hermitian one, exactly as in Part I.

## The Reduction to a Scalar Form

**Definition.** Let $\tau:A\to\mathbb{K}$ be a continuous central functional. The **reduction** of the canonical pairing by $\tau$ is the scalar form

$$
h_{\tau}(x,y)=\tau(x^{*}y)=\tau(yx^{*}),
$$

the equality being the centrality of $\tau$.

**Theorem (the adjoint exists after the reduction).** Let $\tau$ be a continuous central functional whose reduction $h_{\tau}$ is **perfect**, the map $y\mapsto h_{\tau}(\cdot,y)$ a bijection onto $A^{*}$, so that every bounded linear functional on $A$ is represented by a vector through $h_{\tau}$ — the hypothesis of *The Sesquilinear Adjoint Operator*, satisfied for instance when $A$ is a Hilbert space and $h_{\tau}$ its inner product. Then every bounded operator is adjointable for $h_{\tau}$, and in particular

$$
L_{a}^{\dagger}=L_{a^{*}},\qquad L^{\varsigma}_{a}{}^{\dagger}=S_{1,a},\qquad R_{b}^{\dagger}=R_{b^{*}},\qquad T_{p,q}^{\dagger}=T_{p^{*},q^{*}},\qquad S_{a,b}^{\dagger}=S_{b,a},
$$

the formulas of *The Sesquilinear Adjoint Operator*, where $L_{a}(x)=ax$ is the linear left multiplication and $L^{\varsigma}_{a}(x)=ax^{*}$ the conjugate one.

**Proof.** The representation of bounded functionals is the perfection of the form, the hypothesis of *The Sesquilinear Adjoint Operator*: a bounded functional $\ell$ is $\ell=h_{\tau}(\cdot,y_{0})$ for a unique $y_{0}$, and the map $\ell\mapsto y_{0}$ is its inverse. The form $h_{\tau}$ is sesquilinear, $\varsigma$-linear in the first slot and linear in the second, so the adjoint of a bounded operator exists and is unique by the representation. The four formulas are the algebraic identities of Part I, and they survive because the reduction is bounded: each is an identity of the bounded operators obtained by taking adjoints of the algebraic identity, and the trace pairing of Part I is $h_{\tau}$ read through the involution. $\square$

**Remark (what the reduction restores and what it costs).** The reduction replaces the $A$-valued form by a scalar one, and the scalar form has cyclicity, so the whole Part I theory returns; what it costs is faithfulness, and the radical of $h_{\tau}$ is the set $\{x:h_{\tau}(x,y)=0\ \forall y\}$, which is a left ideal and which is nonzero exactly when $\tau$ is not faithful. The adjoint is then computed modulo the radical, and the degeneracies of the article are exactly the two radicals: the trivial one of the canonical form, and the possibly nontrivial one of the reduction. The pairing that makes the adjoint of the conjugate left multiplication exist is therefore a **faithful continuous central functional**, and the comparison with Part I is the statement that its cyclicity is what the $A$-valued form lacks.

## The Bilinear Collapse

**Theorem (the degeneration).** Put $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, so that $A$ is a commutative normed algebra and $h(x,y)=xy$ is the product. Then the derived product is the product, the pairing is the ordinary multiplication pairing, the twisted rule is the linear rule, and the article reduces to the adjoint under a symmetric bilinear form of *The Adjoint under a Hermitian Pairing*.

**Proof.** With $\varsigma=\mathrm{id}$ the two classes of operators coincide, the scalar laws of the adjoint are ordinary linearity, and the twisted rule becomes the linear rule; with $*=\mathrm{id}$ the pairing $h(x,y)=xy=h(y,x)$ is symmetric, the Hermitian property is symmetry, and the two adjoints of a conjugate-linear operator reduce to the one adjoint of a linear operator. The adjointable operators are the left multiplications $L_{c}(x)=cx$, the multiplication operators by elements, which in the commutative case are the multiplications of the base. $\square$

## Worked Cases

### The Field and the Matrices

For $A=\mathbb{C}$ over $\mathbb{K}=\mathbb{C}$ with the conjugation and the modulus, $h(z,w)=\bar zw$ is the standard form, every linear operator is the multiplication $L_{c}(z)=cz$, and $L_{c}^{\dagger}=L_{\bar c}$: the adjoint is the conjugation of the parameter. For $A=M_{n}(\mathbb{C})$ with the conjugate transpose and the operator norm, $h(X,Y)=X^{*}Y$, the adjointable linear operators are the left multiplications $X\mapsto CX$ with $C^{*}X$ the adjoint, the right multiplications $X\mapsto XB^{*}$ and the two-sided operators $X\mapsto PXQ$ are adjointable exactly when the right parameter is a scalar matrix, and the diagonal $h(X,X)=X^{*}X$ is a positive matrix whose trace is the squared Hilbert–Schmidt norm. The only adjointable conjugate-linear operator is $0$, by the collapse of the criterion.

### The Sequences

Let $A=\ell^{\infty}$ with the termwise product, the complex conjugation as the involution, the sup norm and the constant sequence $1$, a commutative unital sesqualgebra; the pairing is $h(x,y)_{k}=\bar x_{k}y_{k}$, termwise. The left multiplication $L_{c}(x)_{k}=c_{k}x_{k}$ is the multiplication by the sequence $c$, bounded for every $c\in\ell^{\infty}$ with $\lVert L_{c}\rVert=\lVert c\rVert_{\infty}$, and $L_{c}^{\dagger}=L_{c^{*}}=L_{\bar c}$. The right multiplications coincide with the left ones because the algebra is commutative, and the two-sided operators are the multiplications; the reduction by the continuous central functional $\tau(x)=\sum_{k}2^{-k}x_{k}$ is the diagonal form $\sum_{k}2^{-k}\bar x_{k}y_{k}$, nondegenerate. Over the commutative algebra the criterion of the conjugate-linear case is satisfied vacuously, so the conjugate left multiplication is adjointable for the canonical form itself, $S_{c,1}^{\dagger}=S_{1,c}$; the example is the commutative extreme, and the matrices of the previous case the noncommutative one.

## Summary

The canonical pairing $h(x,y)=x^{*}y$ of a sesqualgebra is $A$-valued, conjugate-linear in the first slot, linear in the second and Hermitian, with trivial radicals on a unital object; the adjoint of a bounded linear operator is defined by $h(Tx,y)=h(x,T^{\dagger}y)$ and that of a bounded conjugate-linear operator by the twisted rule $h(Sx,y)=h(x,S^{\dagger}y)^{*}$, which preserves the parity. A bounded linear operator is adjointable if and only if it is a left multiplication, $T=L_{c}$, and then $T^{\dagger}=L_{c^{*}}$; the adjointable operators form a closed subalgebra isometrically isomorphic to $A$, on which $T\mapsto T^{\dagger}$ is a $\varsigma$-semilinear anti-automorphism of order two, and the right multiplications and the two-sided operators are adjointable only when the relevant parameter is central. A bounded conjugate-linear operator is adjointable only if it is the right sandwich $S_{1,c}$, $S(x)=x^{*}c$, and only when $c^{*}[x,y]=0$ for all $x,y$, and then $S^{\dagger}=S_{1,c}=S$; in the full noncommutative case this leaves only $0$; the adjoint and the left adjoint coincide for the Hermitian pairing. The pairing that restores the Part I theory is the reduction $h_{\tau}(x,y)=\tau(x^{*}y)$ by a continuous central functional, for which every bounded operator is adjointable and $L_{a}^{\dagger}=S_{1,a}$, the degeneracies being the radicals of $h$ and of $h_{\tau}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(x,y)=x^{*}y$ | the canonical $A$-valued pairing, conjugate-linear in the first slot, linear in the second |
| $h(y,x)=h(x,y)^{*}$ | the Hermitian property |
| $T^{\dagger}$, $h(Tx,y)=h(x,T^{\dagger}y)$ | the adjoint of a bounded linear operator |
| $S^{\dagger}$, $h(Sx,y)=h(x,S^{\dagger}y)^{*}$ | the adjoint of a bounded conjugate-linear operator, the twisted rule |
| $T^{\dagger}=L_{c^{*}}\iff T=L_{c}$ | the adjointable linear operators are the left multiplications |
| $R_{b}^{\dagger}=L_{b}$ ($b$ central), $T_{p,q}^{\dagger}=L_{(pq)^{*}}$ ($q$ central) | the degenerate adjointable one-sided and two-sided operators for the canonical pairing |
| $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, $(\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger}$ | the adjoint operation is a $\varsigma$-semilinear anti-automorphism |
| $S=S_{1,c}$, $S(x)=x^{*}c$ | an adjointable conjugate-linear operator is the right sandwich $S_{1,c}$ |
| $S^{\dagger}=S_{1,c}=S\iff c^{*}[x,y]=0\ \forall x,y$ | the criterion; an adjointable conjugate-linear operator is self-adjoint |
| ${}^{\dagger}S=S^{\dagger}$ | the left adjoint coincides with the adjoint for the Hermitian pairing |
| $h_{\tau}(x,y)=\tau(x^{*}y)$ | the reduction by a central functional, the scalar form of Part I |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the bounded operators, the adjoint and the conjugate-linear operator, read here in the $A$-valued form.
- N. E. Wegge-Olsen, *K-Theory and C\*-Algebras* (Oxford University Press, 1993), for the Hilbert $C^{*}$-modules, the $A$-valued inner product $h(x,y)=x^{*}y$ and the adjointable operators of the regular module, the standard model of the characterisation.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the canonical form $h_c(x,y)=c(x)y$ of an anti-involution and its reduction by a functional.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the trace pairing, its cyclicity and the adjoint anti-automorphism, the algebraic model the reduction recovers.
