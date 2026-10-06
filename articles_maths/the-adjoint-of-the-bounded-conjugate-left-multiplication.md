# __The Adjoint of the Bounded Conjugate Left Multiplication__

## Introduction

The conjugate left multiplication $L_{a}(x)=a\star x=ax^{*}$ is the odd one-sided operator of the sesquialgebra: it is $\varsigma$-semilinear, bounded with norm at most $\lVert a\rVert$, and it is the first operator the layer writes down. *The Adjoint of the Conjugate Left Multiplication* computes its adjoint in the algebraic layer, where the pairing is the trace form $\varphi(x,y)=\tau(xy^{*})$ and the answer is the sandwich $S_{1,a}$, $S_{1,a}(y)=y^{*}a$; the present article is the topological entry of the group, and it adds the norm and the continuity and asks for the pairing under which the adjoint exists at all.

The answer separates two pairings, and the separation is the content of the article. For the **canonical pairing** $h(x,y)=x^{*}y$ of the layer the adjoint does not exist, and the obstruction is the same one that keeps the canonical form from adjointing any conjugate-linear operator: the form is $A$-valued and has no cyclicity, so the defining identity forces the adjoint to be the sandwich $S_{1,a}$ and then demands $xa^{*}y=a^{*}yx$ for all $x,y$, which forces $a$ central and then $xy=yx$, failing as soon as $a\neq0$ in a full noncommutative algebra. The pairing that **makes it exist** is the reduction $h_{\tau}(x,y)=\tau(x^{*}y)$ of the canonical form by a continuous central functional $\tau$: the cyclicity of $\tau$ restores the identity, the adjoint is $S_{1,a}$, and its norm is at most $\lVert a\rVert$, so the adjoint is again a bounded conjugate-linear operator. The **degeneracies** are the radicals: that of the canonical form is trivial and yet the form adjoints no conjugate-linear operator, and that of the reduction is the annihilator of $\tau$, nonzero exactly when $\tau$ is not faithful, in which case the adjoint is computed modulo the radical.

**The boundaries.** The canonical form and its reductions are *Hermitian Forms on a Sesquialgebra* and *The Sesquilinear Form and the Conjugation*; the algebraic result $L_{a}^{\dagger}=S_{1,a}$, the two adjoints and the parity obstruction are *The Adjoint of the Conjugate Left Multiplication* and *The Sesquilinear Adjoint Operator*; the operator, its boundedness and its composites are *The Bounded Left and Right Multiplication Operators of a Sesquialgebra* and *The Bounded Sesquilinear Sandwich*; the general adjoint of the piece is *Adjoints of Bounded Sesquilinear Operators*; the form category's general statement is *The Adjoint under a Hermitian Form*. This article stops before the spectral theory of the later entries.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ with the continuous involution $\varsigma$, and $A$ is a normed sesquialgebra of *Banach Sesquialgebras*: the standard example $x\star y=xy^{*}$, submultiplicative norm, isometric involution, $\lVert1\rVert=1$. The bounded $\varsigma$-semilinear operators are $B^{\varsigma}(A)$ and the bounded linear ones $B(A)$, both of *Bounded Operators on a Sesquialgebra*; the canonical pairing is $h(x,y)=x^{*}y$ and the operator families are $L_{a}(x)=ax^{*}$ (the conjugate left multiplication), $R_{a}(x)=xa^{*}$, $S_{a,b}(x)=ax^{*}b$, $T_{p,q}(x)=pxq$. A continuous functional $\tau:A\to\mathbb{K}$ is **central** when $\tau(uv)=\tau(vu)$ and **compatible** when $\tau(u^{*})=\varsigma(\tau(u))$; the reduction of the canonical form by $\tau$ is $h_{\tau}(x,y)=\tau(x^{*}y)=\tau(yx^{*})$.

## The Conjugate Left Multiplication

### The Operator and its Bound

**Definition.** For $a\in A$ the **bounded conjugate left multiplication** is

$$
L_{a}:A\longrightarrow A,\qquad L_{a}(x)=a\star x=ax^{*}.
$$

**Proposition (parity, bound, injectivity).** $L_{a}$ is $\varsigma$-semilinear and bounded, with

$$
L_{a}(\lambda x)=\varsigma(\lambda)L_{a}(x),\qquad \lVert L_{a}\rVert=\lVert a\rVert,\qquad L_{a}(1)=a,
$$

so $L_{a}=0$ if and only if $a=0$; the parameter map $a\mapsto L_{a}$ is $\varsigma$-semilinear and isometric onto its image. The composite of two of them is linear, $L_{a}L_{b}=T_{a,b^{*}}$, so the family is not closed under composition and its composites leave the one-sided operators.

**Proof.** The parity is the semilinearity of the involution in the second slot; the bound is $\lVert L_{a}x\rVert\le\lVert a\rVert\lVert x^{*}\rVert=\lVert a\rVert\lVert x\rVert$ by submultiplicativity and the isometry, with equality at $x=1$; injectivity is $L_{a}(1)=a$; the $\varsigma$-semilinearity of the parameter map is the first scalar rule of the product. The composite is $(L_{a}L_{b})(x)=a(bx^{*})^{*}=a x b^{*}=T_{a,b^{*}}(x)$, a two-sided operator of *Bounded Operators on a Sesquialgebra*, which is linear and not a one-sided operator. $\square$

**Remark.** In the graded algebra $\mathcal{B}(A)$ of *Bounded Operators on a Sesquialgebra* the operator $L_{a}$ is odd and its square is even, $L_{a}L_{b}\in B(A)$; the involution itself is the case $a=1$, $L_{1}={}^{*}$, the fundamental odd operator. The article computes the adjoint of $L_{a}$ for the two pairings of the layer.

### The Definition of the Adjoint

**Definition.** Let $h$ be a pairing. The **adjoint** of $L_{a}$ for $h$ is the $\varsigma$-semilinear operator $L_{a}^{\dagger}$ with

$$
h(L_{a}x,y)=h(x,L_{a}^{\dagger}y)^{*}\qquad\text{for all }x,y\in A,
$$

when such a bounded operator exists; the twisted rule is the rule of *Adjoints of Bounded Sesquilinear Operators*, and it is the rule that preserves the parity.

**Remark.** The linear rule $h(L_{a}x,y)=h(x,Uy)$ has no solution for a $\varsigma$-semilinear operator over a nontrivial involution, by the scalar obstruction of *The Sesquilinear Adjoint Operator*; the twisted rule is the definition, and the two classes of the adjoint operation are the $R$-linear and the $\varsigma$-semilinear ones.

## The Canonical Pairing: No Adjoint

### The Forced Form and its Failure

**Theorem (the adjoint of $L_{a}$ for $h$, when it exists).** Let $h(x,y)=x^{*}y$ and suppose $L_{a}$ has an adjoint $S^{\dagger}$ for $h$. Then $S^{\dagger}=S_{1,a}$, $S_{1,a}(y)=y^{*}a$, and consequently

$$
xa^{*}y=a^{*}yx\qquad\text{for all }x,y\in A .
$$

**Proof.** Put $x=1$ in the defining identity $h(L_{a}x,y)=h(x,S^{\dagger}y)^{*}$: the left side is $h(a,y)=a^{*}y$ and the right is $h(1,S^{\dagger}y)^{*}=(S^{\dagger}y)^{*}$, so $S^{\dagger}y=(a^{*}y)^{*}=y^{*}a=S_{1,a}(y)$, which is $\varsigma$-semilinear. Substituting back, the identity reads $h(ax^{*},y)=h(x,y^{*}a)^{*}$; the left side is $(ax^{*})^{*}y=xa^{*}y$ and the right is $\bigl(x^{*}(y^{*}a)\bigr)^{*}=(x^{*}y^{*}a)^{*}=a^{*}yx$, so the condition is $xa^{*}y=a^{*}yx$ for all $x,y$; at $y=1$ it is $xa^{*}=a^{*}x$, that is $a^{*}$ commutes with every $x$, and with $a^{*}$ central the condition further reads $a^{*}xy=a^{*}yx$, that is $a^{*}[x,y]=0$. $\square$

**Corollary (non-existence in the full case).** Let $A$ be a full noncommutative sesquialgebra with a nontrivial involution, as in the matrix model. Then $L_{a}$ has no adjoint for the canonical pairing whenever $a\neq0$. In particular the bounded involution ${}^{*}=L_{1}$ is not adjointable for $h$.

**Proof.** The condition $xa^{*}y=a^{*}yx$ at $y=1$ is $xa^{*}=a^{*}x$ for every $x$, so $a^{*}$ is central, hence $a$ is central; with $a^{*}$ central the condition is $a^{*}xy=a^{*}yx$ for all $x,y$, that is $a^{*}[x,y]=0$. In the matrix model $a^{*}=\lambda I$ is a scalar and $\lambda[x,y]=0$ for all $x,y$ forces $\lambda=0$, so $a=0$, and the same argument runs in any full noncommutative sesquialgebra. For $a=1$ the condition is $xy=yx$ for all $x,y$, which fails in a noncommutative algebra; the witness is the pair $x=E_{11}$, $y=E_{12}$ of the matrix model, where $E_{11}E_{12}=E_{12}\neq0=E_{12}E_{11}$. $\square$

**Remark (the witness in its smallest form).** The unit alone does not witness the failure: $h(L_{a}1,1)=h(a,1)=a^{*}$ and $h(1,S_{1,a}1)^{*}=(a^{*})^{*}=a^{*}$ agree, and the smallest witness is a non-commuting pair, $x=E_{11}$, $y=E_{12}$ at $a=1$, where $xy\neq yx$. The obstruction is the missing cyclicity: the canonical form reads $h(ax^{*},y)=xa^{*}y$, and the trace pairing of Part I would move the factor to the other side, which the $A$-valued form does not. So the canonical form **degenerates** for the conjugate left multiplication, not because its radical is nonzero — it is trivial on a unital object — but because it is $A$-valued and has no cyclicity.

## The Reduction: The Pairing that Makes it Exist

### The Adjoint for the Reduced Form

**Definition.** Let $\tau:A\to\mathbb{K}$ be a continuous central functional. The **reduction** of the canonical form by $\tau$ is the scalar form $h_{\tau}(x,y)=\tau(x^{*}y)=\tau(yx^{*})$. Throughout the article the symbol $L_{a}$ is the **conjugate** left multiplication $L_{a}(x)=ax^{*}$ of Part I; the plain left multiplication is written $T_{a,1}$.

**Theorem (the adjoint of the conjugate left multiplication).** Let $\tau$ be a continuous central functional whose reduction $h_{\tau}$ is perfect, the map $y\mapsto h_{\tau}(\cdot,y)$ a bijection onto $A^{*}$, so that every bounded functional on $A$ is represented through $h_{\tau}$. Then $L_{a}$ is adjointable for $h_{\tau}$ and

$$
L_{a}^{\dagger}=S_{1,a},\qquad S_{1,a}(y)=y^{*}a,
$$

a bounded $\varsigma$-semilinear operator with $\lVert L_{a}^{\dagger}\rVert\le\lVert a\rVert$.

**Proof.** The defining identity is $h_{\tau}(L_{a}x,y)=\varsigma\bigl(h_{\tau}(x,S_{1,a}y)\bigr)$. The left side is $\tau\bigl((ax^{*})^{*}y\bigr)=\tau(xa^{*}y)$; the right side is $\varsigma\bigl(\tau(x^{*}y^{*}a)\bigr)=\tau\bigl((x^{*}y^{*}a)^{*}\bigr)=\tau(a^{*}yx)$. The cyclicity of $\tau$ moves the factors: $\tau(xa^{*}y)=\tau(a^{*}yx)$, so the two sides agree; existence and uniqueness are the representation of bounded functionals through the perfect form, the hypothesis of *The Sesquilinear Adjoint Operator*, and the bound is $\lVert S_{1,a}(y)\rVert=\lVert y^{*}a\rVert\le\lVert a\rVert\lVert y\rVert$. $\square$

**Corollary (the involution is adjointable after the reduction).** For $a=1$ the adjoint is the involution itself, $L_{1}^{\dagger}={}^{*}$, and the involution is a bounded self-adjoint $\varsigma$-semilinear operator for $h_{\tau}$.

**Proof.** $S_{1,1}(y)=y^{*}1=y^{*}$, so $L_{1}^{\dagger}={}^{*}$. Self-adjointness is $(S^{\dagger})^{\dagger}=S$ of *Adjoints of Bounded Sesquilinear Operators*, which is the statement that the square of the involution is the identity. $\square$

**Remark (the algebraic comparison).** The theorem is the bounded form of *The Adjoint of the Conjugate Left Multiplication*, §*The Adjoint of the Operator*: the algebra is the same, the operator is the same, the adjoint is the same sandwich, and the only addition is that $L_{a}$ and $S_{1,a}$ are bounded with the displayed norms. What the algebraic layer had and the topological object does not carry is the trace $\tau$ itself: the reduction is the datum that the topological category supplies, and with it the cyclicity that the $A$-valued form lacks.

### The Degeneracies

**Proposition (the radical of the reduction).** The left radical of $h_{\tau}$ is $\{x:h_{\tau}(x,y)=0\ \forall y\}$, a left ideal; it is trivial exactly when $\tau$ is faithful on the products, and in that case the adjoint is unique. When it is nonzero the adjoint is defined modulo the radical and $L_{a}^{\dagger}=S_{1,a}$ holds in the quotient $A/\operatorname{rad}(h_{\tau})$.

**Proof.** The radical is a left ideal because $h_{\tau}(ux,y)=\tau((ux)^{*}y)=\tau(x^{*}u^{*}y)=h_{\tau}(x,u^{*}y)$; it is the annihilator of $\tau$ read against the products, and the quotient is well defined by the containment of the radical in the null set, as *Positivity and the Positive Cone of a Hermitian Form* records for a form. The adjoint identity descends because both sides vanish on the radical. $\square$

**Proposition (what fails without the reduction).** For the canonical form the only adjointable conjugate-linear operators are the trivial ones, by the collapse of *Adjoints of Bounded Sesquilinear Operators*; hence the reduction is not a convenience but a necessity: over a full noncommutative sesquialgebra the conjugate left multiplication has no adjoint until the form is reduced by a central functional.

**Proof.** The hypothesis of the collapse is the full noncommutative case, where the Hermitian elements span and the centre is the scalars; the conjugate left multiplication is $S_{1,a}$ with $c=a$, and its adjointability would require $a^{*}[x,y]=0$ for all $x,y$, hence $a=0$. $\square$

**Remark (the two degeneracies are different).** The canonical form has a trivial radical and adjoints almost nothing; the reduction can have a nonzero radical and adjoints everything. The two senses of "degenerate" are therefore not the same, and the article separates them: the first is the absence of cyclicity, the second is the failure of faithfulness. The former is cured by the presence of a central functional, the latter is a property of that functional.

## The Degenerate Cases

**Proposition (the commutative and the trivial-involution cases).** Let $A$ be commutative with the identity involution, so that $\varsigma=\mathrm{id}$ and the layer is bilinear. Then $L_{a}(x)=ax$ is linear, $S_{1,a}(y)=ya$ coincides with $L_{a}$ and with $R_{a}$, the canonical pairing is the ordinary product pairing $h(x,y)=xy$, and $L_{a}$ is adjointable with $L_{a}^{\dagger}=L_{a}$; the obstruction $xa^{*}y=a^{*}yx$ reads $xy=yx$, which holds by commutativity.

**Proof.** With $*=\mathrm{id}$ the involution is linear and the algebra is commutative, since the identity is an anti-automorphism only then; the operator $L_{a}(x)=ax$ is linear, the twisted rule is the linear rule, and the pairing is symmetric, $h(x,y)=xy=h(y,x)$. The condition of the non-existence corollary is the commutativity, which holds. $\square$

**Theorem (the bilinear collapse).** With $\varsigma=\mathrm{id}$, $*=\mathrm{id}$ and $\tau$ the multiplication functional of the commutative algebra, the article reduces to the adjoint of the multiplication under a symmetric bilinear form, and the two adjoints of the conjugate case coincide.

**Proof.** The two classes of operators coincide, the twisted rule is the linear rule, and the sandwich $S_{1,a}$ is the multiplication $L_{a}$; the reduction $h_{\tau}(x,y)=\tau(xy)$ is the symmetric form, and *The Adjoint under a Hermitian Pairing* gives the adjoint of the multiplication for it. $\square$

## Worked Cases

### The Complex Matrices

Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose, the operator norm and $\tau=\operatorname{tr}$. The canonical pairing is $h(X,Y)=X^{*}Y$, the conjugate left multiplication is $L_{A}(X)=AX^{*}$, bounded with $\lVert L_{A}\rVert=\lVert A\rVert$, and for $A\neq0$ it has no adjoint for $h$: the forced compatibility $XA^{*}Y=A^{*}YX$ fails, with the witness $A=I$, $X=E_{11}$, $Y=E_{12}$, where $XY=E_{12}\neq0=YX$. The reduction $h_{\tau}(X,Y)=\operatorname{tr}(X^{*}Y)$ is the Hilbert–Schmidt form, nondegenerate, and the adjoint is $L_{A}^{\dagger}=S_{1,A}$, $S_{1,A}(Y)=Y^{*}A$, bounded with norm $\lVert A\rVert$; the involution $L_{I}={}^{*}$ is self-adjoint for $h_{\tau}$ and not adjointable for $h$.

### The Field and the Sequences

For $A=\mathbb{C}$ the algebra is commutative, $L_{a}(z)=a\bar z$, the canonical pairing is $h(z,w)=\bar zw$ and $L_{a}^{\dagger}=L_{\bar a}$; the obstruction is vacuous because the algebra is commutative, the criterion $c^{*}[x,y]=0$ being satisfied. For $A=\ell^{\infty}$ with the termwise product and the conjugation, $L_{c}(x)_{k}=c_{k}\bar x_{k}$ is bounded for every $c\in\ell^{\infty}$ with $\lVert L_{c}\rVert=\lVert c\rVert_{\infty}$, and the canonical $A$-valued form adjoints it already, $L_{c}^{\dagger}=S_{1,c}$, the commutative algebra being exactly the case where the obstruction vanishes. The contrast with the matrix algebra, where the same operator has no adjoint, shows that the no-adjoint phenomenon is a statement about noncommutativity and not about the non-triviality of the involution.

## Summary

The bounded conjugate left multiplication $L_{a}(x)=a\star x=ax^{*}$ is $\varsigma$-semilinear, bounded with norm $\lVert a\rVert$ and injective with parameter; its adjoint is defined by the twisted rule $h(L_{a}x,y)=h(x,L_{a}^{\dagger}y)^{*}$. For the canonical pairing $h(x,y)=x^{*}y$ the adjoint does not exist: the defining identity forces $L_{a}^{\dagger}=S_{1,a}$ and then demands $xa^{*}y=a^{*}yx$ for all $x,y$, which forces $a$ central and then $a=0$ in a full noncommutative sesquialgebra, the involution $L_{1}$ being not adjointable. The pairing that makes the adjoint exist is the reduction $h_{\tau}(x,y)=\tau(x^{*}y)$ by a continuous central functional, for which $L_{a}^{\dagger}=S_{1,a}$, the sandwich is bounded with norm at most $\lVert a\rVert$, and the involution is self-adjoint; the reduction is the bounded form of *The Adjoint of the Conjugate Left Multiplication*, and the two degeneracies it separates are the absence of cyclicity in the canonical form and the failure of faithfulness of the functional, the first cured by the presence of a central functional and the second a property of that functional. In the commutative case with the identity involution the obstruction vanishes, the pairing is symmetric and the article reduces to the adjoint of a multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{a}(x)=ax^{*}$ | the bounded conjugate left multiplication, odd, $\lVert L_{a}\rVert=\lVert a\rVert$ |
| $L_{a}L_{b}=T_{a,b^{*}}$ | the composite is a two-sided operator, hence linear; the family is not closed |
| $h(x,y)=x^{*}y$ | the canonical pairing, $A$-valued, with no cyclicity |
| $h(L_{a}x,y)=h(x,L_{a}^{\dagger}y)^{*}$ | the twisted defining rule of the adjoint |
| $xa^{*}y=a^{*}yx$ | the condition forced by the canonical form, forcing $a$ central and then $a=0$ in the full case |
| $S_{1,a}(y)=y^{*}a$ | the forced adjoint, and the adjoint after the reduction |
| $h_{\tau}(x,y)=\tau(x^{*}y)$ | the reduction by a continuous central functional |
| $\operatorname{rad}(h_{\tau})$ | the radical, the annihilator of $\tau$, nonzero exactly when $\tau$ is not faithful |
| $L_{1}^{\dagger}={}^{*}$ | the involution is self-adjoint after the reduction and not adjointable before it |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the canonical form $h_c(x,y)=c(x)y$ of an anti-involution, the conjugate-linear maps and the role of a trace.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the trace pairing, its cyclicity and the adjoint anti-automorphism, the algebraic model the reduction recovers.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the bounded conjugate-linear operators, the twisted adjoint rule and the representation of bounded functionals.
- N. E. Wegge-Olsen, *K-Theory and C\*-Algebras* (Oxford University Press, 1993), for the $A$-valued inner product, the adjointable operators and the place of the involution among them.
