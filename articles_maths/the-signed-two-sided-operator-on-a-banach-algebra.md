
# __The Signed Two-Sided Operator on a Banach Algebra__

## Introduction

The two-sided operator of a Banach algebra is $L_{a}R_{b}(x) = axb$, the operator that multiplies a factor on each side; when the algebra carries a **grade involution** $\alpha$, an involutive automorphism, the argument can be twisted before the multiplication, and the operator

$$
\Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b
$$

is the **signed two-sided operator**. The twist changes the operator in one place only, the argument, and that single change turns the unsigned two-sided operators into a coset of an enlarged group: a signed two-sided operator is the unsigned two-sided operator composed with $\alpha$, the product of two signed two-sided operators is unsigned, and the union of the signed and the unsigned invertible two-sided operators is the group that the reflection operators generate. On a Banach algebra the twist is measured by a norm, because $\alpha$ is continuous, and the signed two-sided operator is bounded with norm at most $\lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$; the whole construction takes place inside the Banach algebra $B(A)$ of bounded operators.

This article assumes the Banach algebra, its submultiplicative norm, the unit group and the spectrum from *Topological Algebras and Banach Algebras*; the bounded operators, the operator norm and the one-sided multiplications from *Operators on a Banach Algebra*; the unsigned two-sided operator, its composition and its group from *The Two-Sided Operator on an Algebra* read on the Banach algebra; the involutive automorphism, the symmetric and skew parts and the grading from *Involutive Topological Algebras* and *The Signed Two-Sided Operator on an Algebra*; and the completeness and closed subalgebras of the operator algebra from *The Operator Algebra of a Banach Space*. The **involution** in the sense of an anti-automorphism $\sigma$ is the structure of the `- * Theory` group of this category and is kept apart from the grade involution $\alpha$ used here; every adjoint and every form is later still. No measure and no Fourier theory occurs.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$; $\alpha$ is a **continuous involutive automorphism** of $A$, so that $\alpha(ab) = \alpha(a)\alpha(b)$, $\alpha(1) = 1$, $\alpha^2 = \mathrm{id}$ and

$$
\lVert\alpha\rVert = \sup_{\lVert x\rVert\leq1}\lVert\alpha(x)\rVert < +\infty ,
$$

with $\lVert\alpha\rVert \geq 1$; $B(A)$ is the unital Banach algebra of bounded linear operators; $L_a(x) = ax$ and $R_b(x) = xb$ are the one-sided multiplications; the **unsigned two-sided operator** is $L_{a}R_{b}$, $L_{a}R_{b}(x) = axb$; the **signed two-sided operator** is $\mathcal{T}_{a,b} = \Sigma^\alpha_{a,b}$, $\mathcal{T}_{a,b}(x) = a\alpha(x)b$; and $A = A^+\oplus A^-$ is the grading of $\alpha$, with $A^\pm$ the $\pm1$-eigenspaces when $2$ is invertible.

## Definition, Decomposition and Bound

**Definition.** For $a,b \in A$ the **signed two-sided operator** by $(a,b)$ is the operator

$$
\mathcal{T}_{a,b} = \Sigma^\alpha_{a,b} : A \to A , \qquad \mathcal{T}_{a,b}(x) = a\,\alpha(x)\,b .
$$

The set of signed two-sided operators is $\Sigma^\alpha(A,A) = \{\mathcal{T}_{a,b} : a,b \in A\}$.

**Proposition (decomposition and continuity).** For all $a,b \in A$,

$$
\boxed{\;\mathcal{T}_{a,b} = L_a\,\alpha\,R_{\alpha(b)} = L_{a}R_{b}\,\alpha , \qquad \alpha = \mathcal{T}_{1,1}\;} ,
$$

and $\mathcal{T}_{a,b}$ is bounded and linear with

$$
\lVert \mathcal{T}_{a,b}\rVert \leq \lVert a\rVert\,\lVert b\rVert\,\lVert\alpha\rVert ,
$$

with $\lVert\alpha\rVert \geq 1$; the assignment $(a,b) \mapsto \mathcal{T}_{a,b}$ is bilinear. When $\alpha$ is isometric the bound is $\lVert a\rVert\lVert b\rVert$.

**Proof.** $L_a\alpha R_{\alpha(b)}(x) = L_a(\alpha(x\alpha(b))) = L_a(\alpha(x)\alpha^2(b)) = a\alpha(x)b = \mathcal{T}_{a,b}(x)$, and $L_{a}R_{b}\alpha(x) = L_{a}R_{b}(\alpha(x)) = a\alpha(x)b$. Boundedness is the composition of the bounded operators $L_a$, $\alpha$ and $R_{\alpha(b)}$, and the norm estimate is submultiplicativity with $\lVert L_a\rVert \leq \lVert a\rVert$, $\lVert R_{\alpha(b)}\rVert \leq \lVert\alpha(b)\rVert \leq \lVert\alpha\rVert\lVert b\rVert$. Bilinearity is the distributivity of the product.

**Proposition (the multiplication table).** For all $a,b,c,d \in A$,

$$
\boxed{\;\mathcal{T}_{a,b}\,L_{c}R_{d} = \mathcal{T}_{a\alpha(c),\,\alpha(d)b} , \qquad L_{a}R_{b}\,\mathcal{T}_{c,d} = \mathcal{T}_{ac,\,db} , \qquad \mathcal{T}_{a,b}\,\mathcal{T}_{c,d} = L_{a\alpha(c)}R_{\,\alpha(d)b}\;} .
$$

Hence the product of two signed two-sided operators is an unsigned two-sided operator, and the signed two-sided operators are closed under composition exactly when $\alpha = \mathrm{id}$.

**Proof.** Using $\mathcal{T}_{p,q} = L_{p}R_{q}\alpha$, $L_{p}R_{q}L_{r}R_{s} = L_{pr}R_{sq}$ and $\alpha L_{r}R_{s} = L_{\alpha(r)}R_{\alpha(s)}\alpha$: for the first, $\mathcal{T}_{a,b}L_{c}R_{d} = L_{a}R_{b}\alpha L_{c}R_{d} = L_{a}R_{b}L_{\alpha(c)}R_{\alpha(d)}\alpha = L_{a\alpha(c)}R_{\alpha(d)b}\alpha = \mathcal{T}_{a\alpha(c),\alpha(d)b}$; the second is $L_{a}R_{b}L_{c}R_{d}\alpha = L_{ac}R_{db}\alpha = \mathcal{T}_{ac,db}$; and the third is the first composed with the second, $\mathcal{T}_{a,b}\mathcal{T}_{c,d} = L_{a}R_{b}\alpha L_{c}R_{d}\alpha = L_{a\alpha(c)}R_{\alpha(d)b}\alpha^2 = L_{a\alpha(c)}R_{\alpha(d)b}$. When $\alpha = \mathrm{id}$ the signed and unsigned families coincide, and conversely $\mathcal{T}_{a,b}\mathcal{T}_{c,d}$ is signed for all $a,b,c,d$ only if $\alpha = \mathrm{id}$ on $A^2 = A$ on a unital algebra.

**Corollary (the coset and the group).** The signed two-sided operators are the coset $\Sigma^\alpha(A,A) = T(A,A)\,\alpha$ of the unsigned two-sided operators by composition with $\alpha$ on the right. The invertible unsigned two-sided operators form the group $G_0 = \{L_{a}R_{b} : a,b \in A^\times\}$, and the union $G_0 \cup G_0\alpha$ is a subgroup of $B(A)^\times$ of index at most two over $G_0$, generated by $G_0$ and $\alpha$.

**Proof.** The coset description is the decomposition; the invertibility of $L_{a}R_{b}$, and hence of $\mathcal{T}_{a,b} = L_{a}R_{b}\alpha$, is exactly for $a,b$ units, by the unsigned two-sided operator computation. The union is closed under products by the table: $G_0G_0 \subseteq G_0$, $G_0(G_0\alpha) \subseteq G_0\alpha$, $(G_0\alpha)G_0 \subseteq G_0\alpha$ and $(G_0\alpha)(G_0\alpha) \subseteq G_0$, and it is closed under inversion because $\alpha^{-1} = \alpha$ and $G_0$ is a group.

**Proposition (the inverse).** The signed two-sided operator $\mathcal{T}_{a,b}$ is invertible exactly when $a,b \in A^\times$, and then

$$
\bigl(\mathcal{T}_{a,b}\bigr)^{-1} = \mathcal{T}_{\alpha(a)^{-1},\,\alpha(b)^{-1}} .
$$

Hence the invertible signed two-sided operators are stable under inversion but not under composition.

**Proof.** $\mathcal{T}_{a,b} = L_{a}R_{b}\alpha$ is a product of invertible operators exactly when $L_{a}R_{b}$ is invertible, that is exactly when $a,b$ are units. For the formula, $\mathcal{T}_{a,b}\mathcal{T}_{\alpha(a)^{-1},\alpha(b)^{-1}} = L_{a\alpha(\alpha(a)^{-1})}R_{\,\alpha(\alpha(b)^{-1})b} = L_{aa^{-1}}R_{\,b^{-1}b} = L_{1}R_{1} = \mathrm{id}$, using $\alpha(\alpha(a)^{-1}) = a^{-1}$; the other composition gives the same, so the two-sided inverse is as displayed.

## The Relation to the Unsigned Two-Sided Operator

**Proposition (the two families differ by the grade involution).** The signed two-sided operators are the composite of the unsigned two-sided operators with the grade involution,

$$
\mathcal{T}_{a,b} = L_{a}R_{b}\circ\alpha , \qquad L_{a}R_{b} = \mathcal{T}_{a,b}\circ\alpha ,
$$

so the two families are related by composition with a fixed operator of order two. A signed two-sided operator equals an unsigned one, $\mathcal{T}_{a,b} = L_{c}R_{d}$, exactly when $L_{c}R_{d}\circ\alpha = L_{a}R_{b}$.

**Proof.** The first identity is the decomposition, and the second follows by composing with $\alpha$ and using $\alpha^2 = \mathrm{id}$. The equality case is the definition.

**Theorem (degeneracy, the inner grade involution).** Suppose $\alpha = c_z$ is the inner automorphism by a unit $z$, $\alpha(x) = zxz^{-1}$. Then every signed two-sided operator is an unsigned two-sided operator,

$$
\alpha = c_z \quad\Longrightarrow\quad \mathcal{T}_{a,b} = L_{az}R_{\,z^{-1}b} ,
$$

and conversely if every signed two-sided operator is unsigned then $\alpha$ is inner on the algebra. In the commutative case $\mathcal{T}_{a,b} = L_{a}R_{\alpha(b)} = \alpha L_{a}R_{b}$, and the signed family carries no information beyond $\alpha$ and the unsigned family; when $\alpha$ is not inner, the signed and the unsigned invertible two-sided operators meet only in the identity of the enlarged group.

**Proof.** For $\alpha = c_z$, $\mathcal{T}_{a,b}(x) = a zxz^{-1} b = (az)x(z^{-1}b) = L_{az}R_{z^{-1}b}(x)$. The converse is the standard fact that $\alpha$ inner is equivalent to the signed family being contained in the unsigned family. In the commutative case $\alpha$ is an automorphism and $a\alpha(x)b = a\alpha(b)x = \alpha(\alpha^{-1}(a)\alpha(b)x)$, which is an unsigned two-sided operator, so the signed operator is $\alpha L_{a}R_{b}$ or $L_{a}R_{\alpha(b)}$ according to the side.

**Remark (the boundary between the two order-two maps).** The map $\alpha$ used here is an **automorphism** of order two, the grade involution of a grading; the anti-automorphism of order two, the **involution** $\sigma$, is the structure of the `- * Theory` group and is not used in this article or in the rest of the signed block. On a commutative algebra the two notions coincide, on a non-commutative one they do not, and no statement here is about $\sigma$.

## The Reflections it Realises

**Definition.** A **reflector** is a unit $u \in A^\times$ with $u\,\alpha(u) \in Z(A)$, the centre; the **reflection** determined by $u$ is the signed conjugation $\rho_u = \mathcal{T}_{u,u^{-1}}$, $\rho_u(x) = u\alpha(x)u^{-1}$.

**Theorem (the square and the involution case).** For every unit $u$ the reflection is bounded, invertible, an algebra automorphism, and

$$
\boxed{\;\rho_u^2 = c_{u\alpha(u)} , \qquad \rho_u = c_u\,\alpha = \alpha\,c_{\alpha(u)}\;} ,
$$

where $c_t(x) = txt^{-1}$. Hence $\rho_u$ is an involutive automorphism, $\rho_u^2 = \mathrm{id}$, exactly when $u$ is a reflector, $u\alpha(u) \in Z(A)$; its fixed set is the closed subalgebra $\{x : u\alpha(x) = xu\}$, and its norm satisfies $\lVert\rho_u\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$.

**Proof.** $\rho_u(\rho_u(x)) = u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)\alpha^2(x)\alpha(u)^{-1}u^{-1} = u\alpha(u)x(u\alpha(u))^{-1} = c_{u\alpha(u)}(x)$, using that $\alpha$ is an automorphism. An inner automorphism is the identity exactly when its conjugating element is central, so $\rho_u^2 = \mathrm{id}$ exactly for a reflector. The composite description is $\rho_u = c_u\alpha$ and $\alpha c_{\alpha(u)}$ by $\alpha c_t = c_{\alpha(t)}\alpha$. The fixed set is the solution set of the continuous equation $u\alpha(x) = xu$, hence closed. The norm bound is submultiplicativity.

**Corollary (the reflection family and the grade involution).** The identity is not a reflector, the unit $1$ is one with $\rho_1 = \alpha$, and the reflections are exactly the signed conjugate automorphisms $\rho_u = c_u\alpha$ with $u$ a reflector; two reflectors give the same reflection exactly when their ratio is a central unit, so the reflections are parametrised by the reflectors modulo $Z(A)^\times$.

**Proof.** $\rho_1 = c_1\alpha = \alpha$; the parametrisation is the standard computation: $\rho_u = \rho_v$ if and only if $v^{-1}u$ commutes with every $\alpha(x)$, that is with all of $A$, so $v^{-1}u \in Z(A)^\times$.

## The Banach Interpretation and Examples

**Proposition (continuity, completeness and closure).** The signed two-sided operators are bounded and their space lies in $B(A)$; the assignment $(a,b)\mapsto \mathcal{T}_{a,b}$ is a bounded bilinear map $A \times A \to B(A)$ with norm at most $\lVert\alpha\rVert$, and it factors through the completed tensor product $\widehat{\otimes}_\pi$ as a bounded linear map of norm at most $\lVert\alpha\rVert$. The reflections are bounded invertible operators; when $\alpha$ is isometric and $u$ is a unitary with $\lVert u\rVert = \lVert u^{-1}\rVert = 1$, the reflection is isometric with $\lVert\rho_u\rVert = 1$.

**Proof.** Boundedness is the decomposition and the norm estimate; bilinear maps of norm at most $\lVert\alpha\rVert$ on a pair of Banach spaces factor through the projective tensor product, and the map is bounded there with the same norm by the universal property. For a reflector $u$ with $\lVert u\rVert = \lVert u^{-1}\rVert = 1$ and $\alpha$ isometric, $\lVert\rho_u(x)\rVert = \lVert u\alpha(x)u^{-1}\rVert \leq \lVert x\rVert$ and the reverse by applying $\rho_u^{-1}$.

**Example (the matrix algebra with a grading).** Let $A = M_n(\mathbb{K})$ with a submultiplicative norm and let $D$ be an invertible diagonal matrix with $D^2 = I$, so that $\alpha(X) = DXD^{-1}$ is a continuous involutive automorphism. The grading separates the diagonal blocks from the off-diagonal ones. The signed two-sided operator is $\mathcal{T}_{A,B}(X) = A(DXD^{-1})B = (AD)X(D^{-1}B)$: for this $\alpha$, which is inner, every signed two-sided operator is an unsigned one, in accordance with the degeneracy theorem.

**Example (a superalgebra).** Let $A = A^0\oplus A^1$ be a Banach algebra with a continuous grading, the product respecting the parity, and let $\alpha$ be the grade involution, $\alpha(x) = (-1)^{\lvert x\rvert}x$ on homogeneous elements. Then $\mathcal{T}_{a,b}(x) = (-1)^{\lvert x\rvert}axb$; the operator commutes with the parity decomposition, and it is the operator by which the algebra acts on itself with the sign rule of a superalgebra. The graded theory is *Superalgebras and Graded Structures*.

**Example (the function algebra).** Let $A = C(X,\mathbb{K})$ with the sup norm for a compact Hausdorff space $X$ and let $E \subseteq X$ be clopen with indicator $\chi$. The map $\alpha(f) = (2\chi - 1)f$, the multiplication by the sign $\pm1$ on the two parts, is a continuous involutive automorphism, and it is the grade involution of the grading of $C(X)$ by the clopen splitting. The signed two-sided operator is $\mathcal{T}_{f,g}(h) = f(2\chi-1)hg$, an isometric perturbation of the unsigned two-sided operator with the sign function.

## Summary

On a unital Banach algebra $A$ with a continuous involutive automorphism $\alpha$, the signed two-sided operator is $\mathcal{T}_{a,b}(x) = a\alpha(x)b$, the unsigned two-sided operator $L_{a}R_{b}$ composed with the twist: $\mathcal{T}_{a,b} = L_a\alpha R_{\alpha(b)} = L_{a}R_{b}\alpha$, bounded with $\lVert \mathcal{T}_{a,b}\rVert \leq \lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$. The multiplication table is $\mathcal{T}_{a,b}L_{c}R_{d} = \mathcal{T}_{a\alpha(c),\alpha(d)b}$, $L_{a}R_{b}\mathcal{T}_{c,d} = \mathcal{T}_{ac,db}$ and $\mathcal{T}_{a,b}\mathcal{T}_{c,d} = L_{a\alpha(c)}R_{\alpha(d)b}$, so a signed two-sided operator followed or preceded by an unsigned one is signed and two signed ones compose to an unsigned one: the signed two-sided operators form the coset $T(A,A)\alpha$, are closed under inversion with $\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{\alpha(a)^{-1},\alpha(b)^{-1}}$, and are closed under composition exactly when $\alpha = \mathrm{id}$. When $\alpha$ is inner every signed two-sided operator is unsigned, $\mathcal{T}_{a,b} = L_{az}R_{z^{-1}b}$ for $\alpha = c_z$, and the signed family adds nothing; the signed block is about the automorphism $\alpha$, the anti-automorphism involution $\sigma$ being the `- * Theory` structure. The reflections that the signed two-sided operators realise are the signed conjugations $\rho_u = \mathcal{T}_{u,u^{-1}}$, whose square is the inner automorphism by $u\alpha(u)$ and which are involutions exactly for the reflectors; they are bounded, and isometric when $\alpha$ and $u$ are. The graded module action over $A$ is *The Graded Action on a Module over an Involutive Banach Algebra*, and the reflection family is *Reflections as Signed Two-Sided Operators on a Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$, $A^\times$, $Z(A)$ | Banach algebra, norm, units, centre |
| $\alpha$ | Continuous involutive automorphism (grade involution), $\alpha^2=\mathrm{id}$, $\lVert\alpha\rVert$ finite |
| $A^\pm$ | The $\pm1$-eigenspaces of $\alpha$, $A = A^+\oplus A^-$ when $2$ invertible |
| $L_{a}R_{b}$ | The unsigned two-sided operator $x\mapsto axb$ |
| $\mathcal{T}_{a,b} = \Sigma^\alpha_{a,b}$ | The signed two-sided operator $x\mapsto a\alpha(x)b$ |
| $\mathcal{T}_{a,b} = L_a\alpha R_{\alpha(b)} = L_{a}R_{b}\alpha$ | Decomposition; $\alpha = \mathcal{T}_{1,1}$ |
| $\lVert \mathcal{T}_{a,b}\rVert \leq \lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$ | Bound of the signed two-sided operator |
| $\mathcal{T}_{a,b}\mathcal{T}_{c,d} = L_{a\alpha(c)}R_{\alpha(d)b}$ | Signed $\times$ signed $=$ unsigned |
| $\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | Inverse, for $a,b$ units |
| $\rho_u = \mathcal{T}_{u,u^{-1}}$ | Reflection, $\rho_u^2 = c_{u\alpha(u)}$ |
| $c_t(x) = txt^{-1}$ | Inner automorphism by $t$ |
| $\alpha = c_z \Rightarrow \mathcal{T}_{a,b} = L_{az}R_{z^{-1}b}$ | Degeneracy when $\alpha$ is inner |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the two-sided operators, the symmetric and skew parts and the grading by an involutive automorphism.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the involutive automorphisms, the inner automorphisms and the signed conjugations.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the bounded operators of a Banach algebra and the automatic continuity of the algebra automorphisms of a $\mathrm{C}^*$-algebra.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the graded Banach algebras, the operators on them and the two-sided operators.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the graded algebras, the grade involution and the operators they generate.
