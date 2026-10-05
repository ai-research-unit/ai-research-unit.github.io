
# __The Signed Sandwich on a Banach Algebra__

## Introduction

The two-sided sandwich of a Banach algebra is $T_{a,b}(x) = axb$, the operator that multiplies a factor on each side; when the algebra carries a **grade involution** $\alpha$, an involutive automorphism, the argument can be twisted before the multiplication, and the operator

$$
\Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b
$$

is the **signed sandwich**. The twist changes the operator in one place only, the argument, and that single change turns the unsigned sandwiches into a coset of an enlarged group: a signed sandwich is the unsigned sandwich composed with $\alpha$, the product of two signed sandwiches is unsigned, and the union of the signed and the unsigned invertible sandwiches is the group that the reflection operators generate. On a Banach algebra the twist is measured by a norm, because $\alpha$ is continuous, and the signed sandwich is bounded with norm at most $\lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$; the whole construction takes place inside the Banach algebra $B(A)$ of bounded operators.

This article assumes the Banach algebra, its submultiplicative norm, the unit group and the spectrum from *Topological Algebras and Banach Algebras*; the bounded operators, the operator norm and the one-sided multiplications from *Operators on a Banach Algebra*; the unsigned sandwich, its composition and its group from *The Sandwich Operator on an Algebra* read on the Banach algebra; the involutive automorphism, the symmetric and skew parts and the grading from *Involutive Topological Bilinear Algebras* and *The Signed Sandwich on an Algebra*; and the completeness and closed subalgebras of the operator algebra from *The Operator Algebra of a Banach Space*. The **involution** in the sense of an anti-automorphism $\sigma$ is the structure of the `- * Theory` group of this category and is kept apart from the grade involution $\alpha$ used here; every adjoint and every form is later still. No measure and no Fourier theory occurs.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$; $\alpha$ is a **continuous involutive automorphism** of $A$, so that $\alpha(ab) = \alpha(a)\alpha(b)$, $\alpha(1) = 1$, $\alpha^2 = \mathrm{id}$ and

$$
\lVert\alpha\rVert = \sup_{\lVert x\rVert\leq1}\lVert\alpha(x)\rVert < +\infty ,
$$

with $\lVert\alpha\rVert \geq 1$; $B(A)$ is the unital Banach algebra of bounded linear operators; $L_a(x) = ax$ and $R_b(x) = xb$ are the one-sided multiplications; the **unsigned sandwich** is $T_{a,b} = L_aR_b$, $T_{a,b}(x) = axb$; the **signed sandwich** is $S_{a,b} = \Sigma^\alpha_{a,b}$, $S_{a,b}(x) = a\alpha(x)b$; and $A = A^+\oplus A^-$ is the grading of $\alpha$, with $A^\pm$ the $\pm1$-eigenspaces when $2$ is invertible.

## Definition, Decomposition and Bound

**Definition.** For $a,b \in A$ the **signed sandwich** by $(a,b)$ is the operator

$$
S_{a,b} = \Sigma^\alpha_{a,b} : A \to A , \qquad S_{a,b}(x) = a\,\alpha(x)\,b .
$$

The set of signed sandwiches is $\Sigma^\alpha(A,A) = \{S_{a,b} : a,b \in A\}$.

**Proposition (decomposition and continuity).** For all $a,b \in A$,

$$
S_{a,b} = L_a\,\alpha\,R_{\alpha(b)} = T_{a,b}\,\alpha , \qquad \alpha = S_{1,1} ,
$$

and $S_{a,b}$ is bounded and linear with

$$
\lVert S_{a,b}\rVert \leq \lVert a\rVert\,\lVert b\rVert\,\lVert\alpha\rVert ,
$$

with $\lVert\alpha\rVert \geq 1$; the assignment $(a,b) \mapsto S_{a,b}$ is bilinear. When $\alpha$ is isometric the bound is $\lVert a\rVert\lVert b\rVert$.

**Proof.** $L_a\alpha R_{\alpha(b)}(x) = L_a(\alpha(x\alpha(b))) = L_a(\alpha(x)\alpha^2(b)) = a\alpha(x)b = S_{a,b}(x)$, and $T_{a,b}\alpha(x) = T_{a,b}(\alpha(x)) = a\alpha(x)b$. Boundedness is the composition of the bounded operators $L_a$, $\alpha$ and $R_{\alpha(b)}$, and the norm estimate is submultiplicativity with $\lVert L_a\rVert \leq \lVert a\rVert$, $\lVert R_{\alpha(b)}\rVert \leq \lVert\alpha(b)\rVert \leq \lVert\alpha\rVert\lVert b\rVert$. Bilinearity is the distributivity of the product. $\square$

**Proposition (the multiplication table).** For all $a,b,c,d \in A$,

$$
S_{a,b}\,T_{c,d} = S_{a\alpha(c),\,\alpha(d)b} , \qquad T_{a,b}\,S_{c,d} = S_{ac,\,db} , \qquad S_{a,b}\,S_{c,d} = T_{a\alpha(c),\,\alpha(d)b} .
$$

Hence the product of two signed sandwiches is an unsigned sandwich, and the signed sandwiches are closed under composition exactly when $\alpha = \mathrm{id}$.

**Proof.** Using $S_{p,q} = T_{p,q}\alpha$, $T_{p,q}T_{r,s} = T_{pr,sq}$ and $\alpha T_{r,s} = T_{\alpha(r),\alpha(s)}\alpha$: for the first, $S_{a,b}T_{c,d} = T_{a,b}\alpha T_{c,d} = T_{a,b}T_{\alpha(c),\alpha(d)}\alpha = T_{a\alpha(c),\alpha(d)b}\alpha = S_{a\alpha(c),\alpha(d)b}$; the second is $T_{a,b}T_{c,d}\alpha = T_{ac,db}\alpha = S_{ac,db}$; and the third is the first composed with the second, $S_{a,b}S_{c,d} = T_{a,b}\alpha T_{c,d}\alpha = T_{a\alpha(c),\alpha(d)b}\alpha^2 = T_{a\alpha(c),\alpha(d)b}$. When $\alpha = \mathrm{id}$ the signed and unsigned families coincide, and conversely $S_{a,b}S_{c,d}$ is signed for all $a,b,c,d$ only if $\alpha = \mathrm{id}$ on $A^2 = A$ on a unital algebra. $\square$

**Corollary (the coset and the group).** The signed sandwiches are the coset $\Sigma^\alpha(A,A) = T(A,A)\,\alpha$ of the unsigned sandwiches by composition with $\alpha$ on the right. The invertible unsigned sandwiches form the group $G_0 = \{T_{a,b} : a,b \in A^\times\}$, and the union $G_0 \cup G_0\alpha$ is a subgroup of $B(A)^\times$ of index at most two over $G_0$, generated by $G_0$ and $\alpha$.

**Proof.** The coset description is the decomposition; the invertibility of $T_{a,b}$, and hence of $S_{a,b} = T_{a,b}\alpha$, is exactly for $a,b$ units, by the unsigned sandwich computation. The union is closed under products by the table: $G_0G_0 \subseteq G_0$, $G_0(G_0\alpha) \subseteq G_0\alpha$, $(G_0\alpha)G_0 \subseteq G_0\alpha$ and $(G_0\alpha)(G_0\alpha) \subseteq G_0$, and it is closed under inversion because $\alpha^{-1} = \alpha$ and $G_0$ is a group. $\square$

**Proposition (the inverse).** The signed sandwich $S_{a,b}$ is invertible exactly when $a,b \in A^\times$, and then

$$
\bigl(S_{a,b}\bigr)^{-1} = S_{\alpha(a)^{-1},\,\alpha(b)^{-1}} .
$$

Hence the invertible signed sandwiches are stable under inversion but not under composition.

**Proof.** $S_{a,b} = T_{a,b}\alpha$ is a product of invertible operators exactly when $T_{a,b}$ is invertible, that is exactly when $a,b$ are units. For the formula, $S_{a,b}S_{\alpha(a)^{-1},\alpha(b)^{-1}} = T_{a\alpha(\alpha(a)^{-1}),\,\alpha(\alpha(b)^{-1})b} = T_{aa^{-1},\,b^{-1}b} = T_{1,1} = \mathrm{id}$, using $\alpha(\alpha(a)^{-1}) = a^{-1}$; the other composition gives the same, so the two-sided inverse is as displayed. $\square$

## The Relation to the Unsigned Sandwich

**Proposition (the two families differ by the grade involution).** The signed sandwiches are the composite of the unsigned sandwiches with the grade involution,

$$
S_{a,b} = T_{a,b}\circ\alpha , \qquad T_{a,b} = S_{a,b}\circ\alpha ,
$$

so the two families are related by composition with a fixed operator of order two. A signed sandwich equals an unsigned one, $S_{a,b} = T_{c,d}$, exactly when $T_{c,d}\circ\alpha = T_{a,b}$.

**Proof.** The first identity is the decomposition, and the second follows by composing with $\alpha$ and using $\alpha^2 = \mathrm{id}$. The equality case is the definition. $\square$

**Theorem (degeneracy, the inner grade involution).** Suppose $\alpha = c_z$ is the inner automorphism by a unit $z$, $\alpha(x) = zxz^{-1}$. Then every signed sandwich is an unsigned sandwich,

$$
\alpha = c_z \quad\Longrightarrow\quad S_{a,b} = T_{az,\,z^{-1}b} ,
$$

and conversely if every signed sandwich is unsigned then $\alpha$ is inner on the algebra. In the commutative case $S_{a,b} = T_{a,\alpha(b)} = \alpha T_{a,b}$, and the signed family carries no information beyond $\alpha$ and the unsigned family; when $\alpha$ is not inner, the signed and the unsigned invertible sandwiches meet only in the identity of the enlarged group.

**Proof.** For $\alpha = c_z$, $S_{a,b}(x) = a zxz^{-1} b = (az)x(z^{-1}b) = T_{az,z^{-1}b}(x)$. The converse is the standard fact that $\alpha$ inner is equivalent to the signed family being contained in the unsigned family. In the commutative case $\alpha$ is an automorphism and $a\alpha(x)b = a\alpha(b)x = \alpha(\alpha^{-1}(a)\alpha(b)x)$, which is an unsigned sandwich, so the signed operator is $\alpha T_{a,b}$ or $T_{a,\alpha(b)}$ according to the side. $\square$

**Remark (the boundary between the two order-two maps).** The map $\alpha$ used here is an **automorphism** of order two, the grade involution of a grading; the anti-automorphism of order two, the **involution** $\sigma$, is the structure of the `- * Theory` group and is not used in this article or in the rest of the signed block. On a commutative algebra the two notions coincide, on a non-commutative one they do not, and no statement here is about $\sigma$.

## The Reflections it Realises

**Definition.** A **reflector** is a unit $u \in A^\times$ with $u\,\alpha(u) \in Z(A)$, the centre; the **reflection** determined by $u$ is the signed conjugation $\rho_u = S_{u,u^{-1}}$, $\rho_u(x) = u\alpha(x)u^{-1}$.

**Theorem (the square and the involution case).** For every unit $u$ the reflection is bounded, invertible, an algebra automorphism, and

$$
\rho_u^2 = c_{u\alpha(u)} , \qquad \rho_u = c_u\,\alpha = \alpha\,c_{\alpha(u)} ,
$$

where $c_t(x) = txt^{-1}$. Hence $\rho_u$ is an involutive automorphism, $\rho_u^2 = \mathrm{id}$, exactly when $u$ is a reflector, $u\alpha(u) \in Z(A)$; its fixed set is the closed subalgebra $\{x : u\alpha(x) = xu\}$, and its norm satisfies $\lVert\rho_u\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$.

**Proof.** $\rho_u(\rho_u(x)) = u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)\alpha^2(x)\alpha(u)^{-1}u^{-1} = u\alpha(u)x(u\alpha(u))^{-1} = c_{u\alpha(u)}(x)$, using that $\alpha$ is an automorphism. An inner automorphism is the identity exactly when its conjugating element is central, so $\rho_u^2 = \mathrm{id}$ exactly for a reflector. The composite description is $\rho_u = c_u\alpha$ and $\alpha c_{\alpha(u)}$ by $\alpha c_t = c_{\alpha(t)}\alpha$. The fixed set is the solution set of the continuous equation $u\alpha(x) = xu$, hence closed. The norm bound is submultiplicativity. $\square$

**Corollary (the reflection family and the grade involution).** The identity is not a reflector, the unit $1$ is one with $\rho_1 = \alpha$, and the reflections are exactly the signed conjugate automorphisms $\rho_u = c_u\alpha$ with $u$ a reflector; two reflectors give the same reflection exactly when their ratio is a central unit, so the reflections are parametrised by the reflectors modulo $Z(A)^\times$.

**Proof.** $\rho_1 = c_1\alpha = \alpha$; the parametrisation is the standard computation: $\rho_u = \rho_v$ if and only if $v^{-1}u$ commutes with every $\alpha(x)$, that is with all of $A$, so $v^{-1}u \in Z(A)^\times$. $\square$

## The Banach Reading and Examples

**Proposition (continuity, completeness and closure).** The signed sandwiches are bounded and their space lies in $B(A)$; the assignment $(a,b)\mapsto S_{a,b}$ is a bounded bilinear map $A \times A \to B(A)$ with norm at most $\lVert\alpha\rVert$, and it factors through the completed tensor product $\widehat{\otimes}_\pi$ as a bounded linear map of norm at most $\lVert\alpha\rVert$. The reflections are bounded invertible operators; when $\alpha$ is isometric and $u$ is a unitary with $\lVert u\rVert = \lVert u^{-1}\rVert = 1$, the reflection is isometric with $\lVert\rho_u\rVert = 1$.

**Proof.** Boundedness is the decomposition and the norm estimate; bilinear maps of norm at most $\lVert\alpha\rVert$ on a pair of Banach spaces factor through the projective tensor product, and the map is bounded there with the same norm by the universal property. For a reflector $u$ with $\lVert u\rVert = \lVert u^{-1}\rVert = 1$ and $\alpha$ isometric, $\lVert\rho_u(x)\rVert = \lVert u\alpha(x)u^{-1}\rVert \leq \lVert x\rVert$ and the reverse by applying $\rho_u^{-1}$. $\square$

**Example (the matrix algebra with a grading).** Let $A = M_n(\mathbb{K})$ with a submultiplicative norm and let $D$ be an invertible diagonal matrix with $D^2 = I$, so that $\alpha(X) = DXD^{-1}$ is a continuous involutive automorphism. The grading separates the diagonal blocks from the off-diagonal ones. The signed sandwich is $S_{A,B}(X) = A(DXD^{-1})B = (AD)X(D^{-1}B)$: for this $\alpha$, which is inner, every signed sandwich is an unsigned one, in accordance with the degeneracy theorem.

**Example (a superalgebra).** Let $A = A^0\oplus A^1$ be a Banach algebra with a continuous grading, the product respecting the parity, and let $\alpha$ be the grade involution, $\alpha(x) = (-1)^{\lvert x\rvert}x$ on homogeneous elements. Then $S_{a,b}(x) = (-1)^{\lvert x\rvert}axb$; the operator commutes with the parity decomposition, and it is the operator by which the algebra acts on itself with the sign rule of a superalgebra. The graded theory is *Superalgebras and Graded Structures*.

**Example (the function algebra).** Let $A = C(X,\mathbb{K})$ with the sup norm for a compact Hausdorff space $X$ and let $E \subseteq X$ be clopen with indicator $\chi$. The map $\alpha(f) = (2\chi - 1)f$, the multiplication by the sign $\pm1$ on the two parts, is a continuous involutive automorphism, and it is the grade involution of the grading of $C(X)$ by the clopen splitting. The signed sandwich is $S_{f,g}(h) = f(2\chi-1)hg$, an isometric perturbation of the unsigned sandwich by the sign function.

## Summary

On a unital Banach algebra $A$ with a continuous involutive automorphism $\alpha$, the signed sandwich is $S_{a,b}(x) = a\alpha(x)b$, the unsigned sandwich $T_{a,b}$ composed with the twist: $S_{a,b} = L_a\alpha R_{\alpha(b)} = T_{a,b}\alpha$, bounded with $\lVert S_{a,b}\rVert \leq \lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$. The multiplication table is $S_{a,b}T_{c,d} = S_{a\alpha(c),\alpha(d)b}$, $T_{a,b}S_{c,d} = S_{ac,db}$ and $S_{a,b}S_{c,d} = T_{a\alpha(c),\alpha(d)b}$, so a signed sandwich followed or preceded by an unsigned one is signed and two signed ones compose to an unsigned one: the signed sandwiches form the coset $T(A,A)\alpha$, are closed under inversion with $S_{a,b}^{-1} = S_{\alpha(a)^{-1},\alpha(b)^{-1}}$, and are closed under composition exactly when $\alpha = \mathrm{id}$. When $\alpha$ is inner every signed sandwich is unsigned, $S_{a,b} = T_{az,z^{-1}b}$ for $\alpha = c_z$, and the signed family adds nothing; the signed block is about the automorphism $\alpha$, the anti-automorphism involution $\sigma$ being the `- * Theory` structure. The reflections that the signed sandwiches realise are the signed conjugations $\rho_u = S_{u,u^{-1}}$, whose square is the inner automorphism by $u\alpha(u)$ and which are involutions exactly for the reflectors; they are bounded, and isometric when $\alpha$ and $u$ are. The graded module action over $A$ is *The Graded Action on a Module over an Involutive Banach Algebra*, and the reflection family is *Reflections as Signed Two-Sided Operators on a Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$, $A^\times$, $Z(A)$ | Banach algebra, norm, units, centre |
| $\alpha$ | Continuous involutive automorphism (grade involution), $\alpha^2=\mathrm{id}$, $\lVert\alpha\rVert$ finite |
| $A^\pm$ | The $\pm1$-eigenspaces of $\alpha$, $A = A^+\oplus A^-$ when $2$ invertible |
| $T_{a,b} = L_aR_b$ | The unsigned sandwich $x\mapsto axb$ |
| $S_{a,b} = \Sigma^\alpha_{a,b}$ | The signed sandwich $x\mapsto a\alpha(x)b$ |
| $S_{a,b} = L_a\alpha R_{\alpha(b)} = T_{a,b}\alpha$ | Decomposition; $\alpha = S_{1,1}$ |
| $\lVert S_{a,b}\rVert \leq \lVert a\rVert\lVert b\rVert\lVert\alpha\rVert$ | Bound of the signed sandwich |
| $S_{a,b}S_{c,d} = T_{a\alpha(c),\alpha(d)b}$ | Signed $\times$ signed $=$ unsigned |
| $S_{a,b}^{-1} = S_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | Inverse, for $a,b$ units |
| $\rho_u = S_{u,u^{-1}}$ | Reflection, $\rho_u^2 = c_{u\alpha(u)}$ |
| $c_t(x) = txt^{-1}$ | Inner automorphism by $t$ |
| $\alpha = c_z \Rightarrow S_{a,b} = T_{az,z^{-1}b}$ | Degeneracy when $\alpha$ is inner |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the sandwich operators, the symmetric and skew parts and the grading by an involutive automorphism.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the involutive automorphisms, the inner automorphisms and the signed conjugations.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the bounded operators of a Banach algebra and the automatic continuity of the algebra automorphisms of a $\mathrm{C}^*$-algebra.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the graded Banach algebras, the operators on them and the sandwich operators.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the graded algebras, the grade involution and the operators they generate.
