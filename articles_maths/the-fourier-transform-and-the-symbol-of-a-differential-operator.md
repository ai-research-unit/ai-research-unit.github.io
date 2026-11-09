# __The Fourier Transform and the Symbol of a Differential Operator__

## Introduction

The Fourier transform turns a constant-coefficient differential operator into the multiplication by one element of an algebra. That sentence is the whole of this article, and it is worth stating at once, because everything that follows is a consequence of it: a differential equation becomes, at each frequency, the equation $a\,x=b$ in a finite-dimensional algebra, and every question about the equation becomes a question about the element $a$.

**The object.** Let $A$ be a finite-dimensional real algebra with unit, of dimension $d$, and let $P(D)=\sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ be a differential operator whose coefficients $a_\alpha$ lie in $A$. Its **symbol** is the element

$$
\sigma_P(\zeta) \;=\; \sum_{|\alpha|\le m} a_\alpha\,(i\zeta)^\alpha \;\in\; A_{\mathbb{C}} ,
$$

a polynomial in the frequency $\zeta\in\mathbb{R}^n$ with values in the complexified algebra. The article proves that the transform of $P(D)u$ is the left multiplication of the transform of $u$ by $\sigma_P$, and then reads four things off that identity: when the equation is solvable at a frequency, what the obstruction is when it is not, how the obstruction is measured by a determinant, and where the obstruction can occur.

**Why the coefficients in an algebra and not in a field.** For $A=\mathbb{C}$ the symbol is a polynomial and the equation $a\,x=b$ is solvable whenever $a\ne0$; the whole of the classical theory is the study of the zero set. For a non-commutative $A$, and still more for an $A$ with zero divisors, the element $a$ can fail to be a unit while being non-zero, and the failure is then not always a point: it is a set, and the set has a shape. The shape depends on the algebra and not on the operator, and the theorem that separates the shapes is the second result of this article. This article fixes the general statement, for an arbitrary finite-dimensional real algebra; the articles of the harmonic-analysis ladder compute the shapes for the particular algebras they treat.

**Boundaries.** The article is about the forward transform and the pointwise algebra at one frequency. It does not carry out the inverse transform, which is *The Fourier Operator*, it does not treat the global solvability of $P(D)u=f$ on $\mathbb{R}^n$, which requires the parametrix construction and belongs to *The Fundamental Solution Operator*, and it does not place the transform in a topological space of test functions, which is *Distributions and Fundamental Solutions*. The coefficients are constant; the variable-coefficient case is stated only to say what fails, in §*What the Transform Does Not Do*. The symbol of an operator over a field, and the law by which symbols compose, are *Differential Operators*; this article takes that law as given and adds the two things the scalar case does not have, a coefficient that does not commute and a symbol that need not be a unit.

**Assumptions and notation.** The algebra $A$ is finite-dimensional, associative, real, with unit $1$. The functions are $A_{\mathbb{C}}$-valued, $u:\mathbb{R}^n\to A_{\mathbb{C}}$, taken smooth and of compact support where a transform is written; the transform of a general function is read in the sense of *Distributions and Fundamental Solutions*. The frequency is $\zeta\in\mathbb{R}^n$, the same letter *Differential Operators* uses for the variable of the symbol, and $\zeta^\alpha=\zeta_1^{\alpha_1}\cdots\zeta_n^{\alpha_n}$.

Two letters differ from that article. The operator is written $P(D)$ and not $L$, because $L$ is the letter of the left multiplication throughout what follows, and the two objects would be one glyph too many. And the transform is written $\mathcal{F}[u]$ and not by a mark on the letter, as the harmonic analysis articles of the corpus write it: $\mathcal{F}[u](\zeta)$.

## The Algebra and the Operator

**The two linear structures.** An element $a\in A$ acts on $A$ on the left and on the right, and the two actions are different when $A$ is not commutative. The left action is the map

$$
L_a : A\longrightarrow A,\qquad L_a(x)=ax ,
$$

and it is the object this article is about. The map $L_a$ is **right $A$-linear**, $L_a(xb)=L_a(x)\,b$, because the product is associative; it is $A$-linear on the left only when $a$ lies in the centre. Its image is the left ideal $Aa$, and a left ideal is what an image of a left multiplication can be.

**Proposition (the regular representation).** The assignment $a\mapsto L_a$ is an injective homomorphism of algebras from $A$ into the endomorphisms of the real vector space $A$, and $L_{ab}=L_aL_b$. It is called the **left regular representation**.

*Proof.* The map is additive and $L_{ab}(x)=(ab)x=a(bx)=L_aL_b(x)$, so it is multiplicative and reverses nothing. It is injective because $L_a=0$ gives $a=L_a(1)=0$.

**The matrix of the representation.** Choosing a real basis $e_1,\dots,e_d$ of $A$ writes $L_a$ as a $d\times d$ real matrix, the **regular matrix** of $a$, and the entry in row $\mu$ column $\nu$ is the $\mu$-th coordinate of $a e_\nu$. Every statement below about a determinant is a statement about this matrix, and it is basis-independent as a vanishing condition.

**The operator.** A **constant-coefficient differential operator with coefficients in $A$** is an expression

$$
P(D)=\sum_{|\alpha|\le m}a_\alpha\,\partial^\alpha ,\qquad a_\alpha\in A ,
$$

acting on $A_{\mathbb{C}}$-valued functions by $(P(D)u)(x)=\sum a_\alpha\,\partial^\alpha u(x)$. The coefficients sit on the left of the derivative, and that placement is part of the definition: for non-commutative $A$ the expression $\sum\partial^\alpha a_\alpha$ is a different operator, and the two are exchanged by the transposition of *Differential Operators*.

Its **order** is the largest $|\alpha|$ with $a_\alpha\ne0$, and its **principal part** is the sum of those terms. The operator is read by its action, so two expressions define the same operator exactly when their coefficients agree, coefficient by coefficient and in the same order.

**Remark (the scalar case is the case $A=\mathbb{R}$ or $\mathbb{C}$).** Everything in this article reduces to the classical statements when $A$ is a field, and the reader may keep that case in view: the symbol is a polynomial, $L_a$ is multiplication by a number, and the only non-unit is $0$. **The general case is separated from it by one fact only, that a non-zero element of $A$ need not be a unit.**

## The Symbol

**Definition.** The **symbol** of $P(D)$ is the $A_{\mathbb{C}}$-valued polynomial on $\mathbb{R}^n$,

$$
\sigma_P(\zeta)=\sum_{|\alpha|\le m}a_\alpha\,(i\zeta)^\alpha ,
$$

and the **principal symbol** is its homogeneous part of degree $m$.

**The relation to the symbol of *Differential Operators*.** That article defines the symbol of $L=\sum a_\alpha\partial^\alpha$ as $\sigma_L(x,\zeta)=\sum a_\alpha(x)\zeta^\alpha$ and proves the composition law for it. With constant coefficients its symbol does not depend on $x$, and the value written here is that symbol read at $\zeta\mapsto i\zeta$:

$$
\sigma_P(\zeta)=\sigma_L(i\zeta) .
$$

The substitution is forced by the transform, which converts $\partial_j$ into the factor $i\zeta_j$; it is a change of variable in the argument and not a second definition. When $A$ is written as a set of real matrices of size $d$, the same substitution turns the polynomial into a matrix polynomial, and everything below is a statement about that matrix.

**The factor $2\pi$.** The harmonic analysis articles of the corpus write the transform with $2\pi$ in the exponential, with the square carried by a root of $1$ in the algebra and the sign by the scalar $i$, so that the multiplier of the gradient reads $2\pi i\tilde{Ζ}\omega$ with $\tilde{Ζ}^{2}=e_t$. This article absorbs both into $\zeta$ and writes the root as the scalar $i$, which the complexified algebra $A_{\mathbb{C}}$ always contains. The two conventions differ by the substitution $\zeta=-2\pi\tilde{Ζ}\omega$, and no result depends on it.

**Proposition (the symbol of a derivative).** The symbol of $\partial_j$ is $i\zeta_j\,1$, the symbol of a constant coefficient $a$ is $a$, and the symbol of a sum is the sum of the symbols. The correspondence $P\mapsto\sigma_P$ is one to one.

*Proof.* Each is read from the definition. The injectivity follows because distinct coefficient families give distinct polynomials, the monomials $(i\zeta)^\alpha$ being linearly independent over $A_{\mathbb{C}}$.

**Theorem (the symbol of a composition).** If $P_1$ and $P_2$ have constant coefficients, the symbol of $P_1P_2$ is the product

$$
\sigma_{P_1P_2}(\zeta)=\sigma_{P_1}(\zeta)\,\sigma_{P_2}(\zeta) ,
$$

the product taken in $A_{\mathbb{C}}$ and in that order.

*Proof.* The composition acts by $\sum_{\alpha,\beta}a_\alpha b_\beta\,\partial^{\alpha+\beta}$, because the coefficients are constant and the derivatives therefore commute with them. Replacing $\partial^{\alpha+\beta}$ by $(i\zeta)^{\alpha+\beta}$ and summing gives $\big(\sum a_\alpha(i\zeta)^\alpha\big)\big(\sum b_\beta(i\zeta)^\beta\big)$.

**Remark (what constant coefficients buy).** For variable coefficients the composition law carries correction terms, $\sigma_{P_1P_2}=\sum_{\gamma}\frac{1}{\gamma!}\,\partial^\gamma_\zeta\sigma_{P_1}\,\partial^\gamma_x\sigma_{P_2}$, as *Differential Operators* states. **With constant coefficients every correction term vanishes, and the symbol becomes multiplicative without qualification.** That multiplicativity is what makes the transform an algebra homomorphism, and it is lost the moment a coefficient depends on $x$. The consequences of that multiplicativity — the order of a composite, its units, its singular set and the zero divisors of the algebra of operators — are worked out in *The Fourier Transform and the Composition of Symbols*.

**The coefficients do not commute.** If $A$ is not commutative, $\sigma_{P_1}\sigma_{P_2}\ne\sigma_{P_2}\sigma_{P_1}$ in general, and the two orders correspond to the two operators $P_1P_2$ and $P_2P_1$, which are different. The symbol therefore remembers an order that the scalar symbol does not have to remember. This is the first of the two facts that separate the general theory from the classical one.

**Example (three symbols).** The following table fixes the notation for the rest of the article.

| Operator | Symbol | Algebra | Degree |
|---|---|---|---|
| $\partial_1^2+\cdots+\partial_n^2$ | $-\lvert\zeta\rvert^2$ | $A=\mathbb{R}$ | $2$ |
| $a_1\partial_1+a_2\partial_2$, $a_j\in A$ | $i(a_1\zeta_1+a_2\zeta_2)$ | any $A$ | $1$ |
| $a\,\partial_1^2+b\,\partial_1+c$ | $-a\zeta_1^2+ib\zeta_1+c$ | any $A$ | $2$ |

The third is the shape that carries the whole difficulty: a quadratic term, a linear term and a constant, with coefficients that need not commute, and a symbol that can vanish without any of its terms vanishing.

## The Transform as Left Multiplication

**Definition.** For $u\in C_c^\infty(\mathbb{R}^n,A_{\mathbb{C}})$ the **Fourier transform** is

$$
\mathcal{F}[u](\zeta)=\int_{\mathbb{R}^n}e^{-i\zeta\cdot x}\,u(x)\,dx ,
$$

the exponential a scalar and the integration entrywise, so that $\mathcal{F}[u]$ is again $A_{\mathbb{C}}$-valued.

**Proposition (the transform of a derivative).** $\mathcal{F}[\partial_j u](\zeta)=i\zeta_j\,\mathcal{F}[u](\zeta)$.

*Proof.* Integrate by parts in the $j$-th variable; the boundary term vanishes because $u$ has compact support.

**Theorem (the transform of the operator).** For every $u\in C_c^\infty(\mathbb{R}^n,A_{\mathbb{C}})$,

$$
\boxed{\;\mathcal{F}[P(D)u](\zeta)\;=\;L_{\sigma_P(\zeta)}\big(\mathcal{F}[u](\zeta)\big)\;=\;\sigma_P(\zeta)\,\mathcal{F}[u](\zeta)\;}
$$

*Proof.* By linearity of the transform it is enough to treat one term $a_\alpha\partial^\alpha u$. The coefficient is constant, so it passes through the integral on the left, $\mathcal{F}[a_\alpha\partial^\alpha u]=a_\alpha\,\mathcal{F}[\partial^\alpha u]$; the derivative contributes $(i\zeta)^\alpha$ by the proposition iterated; and the sum is the left multiplication by $\sigma_P(\zeta)$.

**The reading of the theorem.** A differential operator of order $m$ is, under the transform, the multiplication by one element. Three consequences follow at once, and they are the three that the rest of the article develops.

- The operator is **diagonalized at each frequency**: it acts on the value of $\mathcal{F}[u]$ at $\zeta$ alone, and different frequencies do not mix. This is the sense in which the transform turns the equation into an algebraic one; it is not that the operator becomes a number, but that it becomes a multiplication, and a multiplication acts pointwise.
- The operator is **invertible at the frequency $\zeta$ exactly when the element $\sigma_P(\zeta)$ is a unit**, and then the inverse is the multiplication by $\sigma_P(\zeta)^{-1}$. Nothing else is needed: no boundary condition, no parametrix, no topology.
- The **failure** of invertibility at $\zeta$ is the failure of one element of a finite-dimensional algebra to be a unit. It is therefore a question of linear algebra, and it is decided by a determinant.

**Remark (the theorem is exactly an equivalence).** The correspondence $P\mapsto\sigma_P$ is one to one, and so is the correspondence between constant-coefficient operators and $A_{\mathbb{C}}$-valued polynomials. **The transform is therefore an isomorphism of algebras between the constant-coefficient operators under composition and the polynomials under multiplication**, and a representation of the one is a representation of the other. This is the precise content of the word "algebraic" in the title of the family of studies this article belongs to.

## Solvability at One Frequency

**The equation at one frequency.** Fix $\zeta$ and $b\in A_{\mathbb{C}}$. By the theorem the equation $P(D)u=f$ becomes, at the frequency $\zeta$,

$$
\sigma_P(\zeta)\,x=b ,\qquad x=\mathcal{F}[u](\zeta),\quad b=\mathcal{F}[f](\zeta) .
$$

This is the equation of left multiplication by an element of a finite-dimensional algebra, and it is solved completely by the following theorem.

**Theorem (solvability).** Let $a\in A$ and $L_a$ its left multiplication. Then the following are equivalent.

1. $L_a$ is injective.
2. $L_a$ is surjective.
3. $L_a$ is invertible.
4. $a$ is a unit of $A$.
5. $\det L_a\ne0$.

If they hold, the equation $ax=b$ has the unique solution $x=a^{-1}b$ for every $b$. If they fail, the equation is solvable exactly for those $b$ lying in the left ideal $Aa$, and the solution is determined only up to the left annihilator of $a$.

*Proof.* The space $A$ is finite-dimensional, so by rank–nullity an endomorphism of it is injective exactly when it is surjective; this gives 1 $\Leftrightarrow$ 2 $\Leftrightarrow$ 3. If $L_a$ is surjective there is an $x$ with $L_a(x)=ax=1$. Then $a(xa-1)=(ax)a-a=a-a=0$, so $xa-1$ lies in $\ker L_a$, which is $\{0\}$ because $L_a$ is injective; hence $xa=1$ as well, and $a$ is a unit. Conversely a unit has the inverse $L_{a^{-1}}$. This gives 3 $\Leftrightarrow$ 4. A square matrix is invertible exactly when its determinant is non-zero, which gives 3 $\Leftrightarrow$ 5. The last sentence is the definition of the image and of the kernel: $ax=b$ has a solution exactly when $b\in Aa$, and two solutions differ by an element of $\ker L_a$.

**Definition.** The **left annihilator** of $a$ is $\operatorname{Ann}_L(a)=\{x\in A:ax=0\}=\ker L_a$, and the **cokernel** of $L_a$ is $\operatorname{coker}L_a=A/Aa$. Both are left $A$-modules.

**Corollary (the two counts agree).** For every $a\in A$,

$$
\dim\operatorname{Ann}_L(a)\;=\;\dim\operatorname{coker}L_a\;=\;d-\operatorname{rank}L_a .
$$

*Proof.* The first equality is rank–nullity applied to $L_a$, whose domain has dimension $d$ and whose image is $Aa$; the second is the same statement read on the image.

**Remark (what the corollary says, and what it does not).** The two spaces have the same dimension and they are not the same space: $\operatorname{Ann}_L(a)\subseteq A$ is a subspace of the algebra, and $\operatorname{coker}L_a$ is a quotient of it. **The equality of dimensions is a numerical coincidence of the regular representation, and it fails for a symbol that takes values in a proper subalgebra or in a module.** For the regular representation it is exact and it is the reason a single number, the rank, reports both the freedom in the solution and the number of conditions on the data.

**Remark (the equation is not yet solved on $\mathbb{R}^n$).** The theorem is a statement at one frequency. To pass from it to the equation on $\mathbb{R}^n$ one must solve at every $\zeta$ at once, divide by $\sigma_P(\zeta)$ as a function of $\zeta$, and control the growth of the quotient; that is the construction of a fundamental solution, and it belongs to *The Fundamental Solution Operator*. **What the pointwise statement contributes is the location of the obstruction, and it contributes it exactly**: the obstruction sits at the frequencies where $\sigma_P$ is not a unit, and nowhere else.

## The Determinant of the Regular Representation

**Definition.** The **determinant of the regular representation** of $a$ is $\det L_a$, the determinant of the regular matrix of $a$ in a real basis of $A$. It is a homogeneous polynomial of degree $d$ in the coordinates of $a$, and a change of basis multiplies it by a positive constant, so its vanishing does not depend on the basis.

**Proposition (multiplicativity and vanishing).** For all $a,b\in A$,

$$
\det L_{ab}=\det L_a\,\det L_b ,\qquad \det L_1=1 ,
$$

and $\det L_a\ne0$ exactly when $a$ is a unit.

*Proof.* The first is $L_{ab}=L_aL_b$ and the multiplicativity of the determinant; the second is $L_1=\mathrm{id}$; the third is the theorem of §*Solvability at One Frequency*.

**The determinant is a multiplicative functional, and that is its role.** It converts the question "is this element a unit" into the question "does this polynomial vanish", and it converts the multiplicative structure of $A$ into the multiplicative structure of the scalars. Nothing else in the article uses more about $A$ than this proposition.

**Four algebras, four mechanisms.** The determinant takes a different form in each of the four kinds of algebra, and the table is worth reading by column.

| $A$ | $d$ | $\det L_a$ | the non-units |
|---|---|---|---|
| $\mathbb{C}$ over $\mathbb{R}$ | $2$ | $\lvert a\rvert^2$ | the point $0$ |
| $\mathbb{H}$ | $4$ | $N(a)^2$ | the point $0$ |
| $M_2(\mathbb{R})$ | $4$ | $(\det a)^2$ | the singular matrices |
| $\mathbb{R}[\varepsilon]$, $\varepsilon^2=0$ | $2$ | $a_0^2$ | the line $a_0=0$ |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | $8$ | $\lvert N(\tilde Q)\rvert^{4}$ | the null cone $N(\tilde Q)=0$ |

In the first two rows the determinant is a power of a **positive definite** quadratic form, and its only zero is the origin. In the third row it is the square of an **indefinite** form, and its zero set is the cone of singular matrices. In the fourth row, with $a=a_0+a_1\varepsilon$, the algebra has a nilpotent part, the determinant does not see the coefficient of $\varepsilon$ at all, and its zero set is a linear subspace. The fifth row is the matrix case again, read on a complex matrix algebra and written with a modulus.

**Proposition (matrix algebras).** For $A=M_r(\mathbb{R})$ and $a\in A$,

$$
\det L_a=(\det a)^{r} .
$$

*Proof.* The algebra is $M_r(\mathbb{R})\cong\mathbb{R}^r\otimes\mathbb{R}^r$, of dimension $r^2$, and the left multiplication by $a$ acts on the first factor alone: on a decomposable element $u\otimes w$ it is $(au)\otimes w$. The determinant of an operator that acts on one factor of a tensor product with determinant $\delta$ is $\delta^{r}$, the exponent being the dimension of the other factor. Here $\delta=\det a$ and the other factor has dimension $r$.

**Remark (the exponent is the size, and the degree is the square of the size).** In $M_2(\mathbb{R})$ the determinant has degree $4=2^2$ in the four entries, and it is the square of the quadratic polynomial $\det a$. **The degree of the regular determinant is always $d$, and its shape is the shape of the reduced norm of the algebra**: a form in the division case, the determinant in the matrix case, a form in fewer variables in the presence of a radical.

**Corollary (a single real scalar decides).** The equation at the frequency $\zeta$ is solvable for every $b$ exactly when $\det L_{\sigma_P(\zeta)}\ne0$. So the algebra of the whole problem is decided, at each frequency, by **one real number**, and the number is a polynomial in $\zeta$ of degree $dm$ when $P$ has order $m$.

**Remark (the biquaternion algebra, as the fifth row).** For $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ one has $d=8$, and the algebra is the complex matrix algebra $M_2(\mathbb{C})$. In that model the left multiplication is the multiplication of matrices on the left, so its complex determinant is $N(\tilde Q)^2$ and the real determinant of the same operator is $\lvert N(\tilde Q)\rvert^4$. Two things are worth keeping: the modulus is not decoration, because $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is complex-valued and central while $\tilde Q^2$ is neither; and the exponent is the size of the matrix, not the dimension of the algebra. The zero set is the null cone, of real codimension two in the eight coordinates. For the gradient symbol of *Biquaternion Continuous Harmonic Analysis* the same formula gives $s^4$ on the real frequencies, where $s=\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2$, because the norm there is $-s$ and the fourth power removes the sign; the zero set is then the single point $\zeta=0$. At a non-zero null element the rank is $4$ of $8$, and the kernel and the cokernel both have dimension $4$. The article stops at those sentences: the block form, the four spectral cases and the rank on the cone are the subject of the biquaternion ladder, and the algebra itself is *The Biquaternion Algebra*.

## The Zero Set

**Definition.** The **zero set** of the symbol is

$$
Z(P)=\{\zeta\in\mathbb{C}^n:\sigma_P(\zeta)\text{ is not a unit of }A_{\mathbb{C}}\} ,
$$

where $\sigma_P$ is extended from $\mathbb{R}^n$ to $\mathbb{C}^n$ by the same polynomial, and the **real zero set** is $Z(P)\cap\mathbb{R}^n$. By the corollary of §*The Determinant of the Regular Representation* it is the zero set of the single polynomial $\det L_{\sigma_P}$:

$$
Z(P)=\{\zeta:\det L_{\sigma_P(\zeta)}=0\} .
$$

**Theorem (the zero set is the obstruction, and only the obstruction).** The equation at the frequency $\zeta$ is solvable for every $b$ if and only if $\zeta\notin Z(P)$; and for $\zeta\in Z(P)$ the space of obstructions is $\operatorname{coker}L_{\sigma_P(\zeta)}$, of dimension $d-\operatorname{rank}L_{\sigma_P(\zeta)}$.

*Proof.* Theorem §*Solvability at One Frequency*, applied to $a=\sigma_P(\zeta)$, with the corollary of that section for the dimension.

**The three shapes of a zero set.** The determinant is one polynomial, and the set where it vanishes can have three different shapes. The shape is determined by the algebra and by the symbol, and the three cases are what the rest of the theory has to keep apart.

- **A point, or nothing.** When $A$ is a division algebra, every non-zero element is a unit, so the only candidate is $\zeta=0$, and if the operator carries an invertible constant term the zero set is empty. This is the case of $\mathbb{C}$ and of $\mathbb{H}$, and it is the classical well-posed case.
- **A hypersurface.** When $A$ is a matrix algebra or a split algebra, the non-units form the zero set of an indefinite form: the cone of singular matrices, or the isotropic cone of the form. This is the case of $M_2(\mathbb{R})$ and of the split algebras.
- **A linear subspace.** When $A$ has a nilpotent radical, the determinant depends on fewer coordinates than $A$ has, and its zero set contains whole directions: the symbol is singular for every value of those coordinates.

**Example (the singular cone, computed).** Let $A=M_2(\mathbb{R})$ with the basis $E_{11},E_{12},E_{21},E_{22}$ of the matrix units, and let $P(D)=\sum_{i,j}E_{ij}\partial_{ij}$ be read on $\mathbb{R}^4$ with the frequency $\zeta=(\zeta_{11},\zeta_{12},\zeta_{21},\zeta_{22})$. Then

$$
\sigma_P(\zeta)=\begin{pmatrix}\zeta_{11}&\zeta_{12}\\ \zeta_{21}&\zeta_{22}\end{pmatrix},
\qquad
\det L_{\sigma_P(\zeta)}=\big(\zeta_{11}\zeta_{22}-\zeta_{12}\zeta_{21}\big)^{2} .
$$

The values are these. At $\zeta=(1,0,0,1)$ the matrix is the identity, $\det\sigma=1$, $\det L_\sigma=1$, and the rank of $L_\sigma$ is $4$. At $\zeta=(1,0,0,2)$ the matrix is diag$(1,2)$, $\det\sigma=2$, $\det L_\sigma=4$, and the rank is $4$. At $\zeta=(1,0,0,0)$ the matrix is $E_{11}$, the determinant is $0$, and the rank falls from $4$ to $2$: the image of $L_{E_{11}}$ is the set of matrices whose second column vanishes. At $\zeta=(0,1,0,0)$ the matrix is $E_{12}$, the rank is again $2$. The zero set is the cone of singular $2\times2$ matrices, of real codimension one in $\mathbb{R}^4$.

**Remark (a non-negative determinant does not mean a small zero set).** In the example the determinant is a square and is never negative, and its real zero set is still a hypersurface. **The sign of the polynomial and the codimension of its zero set are two different questions**, and only the second one decides whether the obstruction can be met along a curve of frequencies or whether it fills a region.

**Remark (the shape is a property of the algebra, not of the operator).** Keep an operator of order one with one coefficient per basis element, on four variables, and change the algebra from $M_2(\mathbb{R})$ to $\mathbb{H}$: the symbol is $\zeta_0+\zeta_1i+\zeta_2j+\zeta_3k$, the determinant is $\det L_\sigma=N(\sigma)^2=(\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2)^2$, and the zero set is the single point $0$. **The order, the degree of the determinant and the dimension are the same in the two cases, and the zero set has gone from a cone to a point.** The location of the obstruction is therefore a property of the quadratic form that the algebra carries, and not of the operator alone.

**Remark (the radical is invisible to the determinant).** In $A=\mathbb{R}[\varepsilon]$ with $\varepsilon^2=0$ take $P(D)=\partial_1+\varepsilon\partial_2$. The symbol is $\zeta_1+\varepsilon\zeta_2$, the determinant is $\zeta_1^2$, and the zero set is the plane $\zeta_1=0$, whatever the value of $\zeta_2$. **Every frequency with a vanishing coefficient of $1$ is a zero, and the coefficient of $\varepsilon$ is not seen.** A nilpotent coefficient therefore makes the equation singular on a set that no power of the determinant can narrow, and this is the one case in which the determinant is not a faithful measure of the obstruction.

**Remark (where the zeros are, and what that costs).** At a zero the theorem of §*Solvability at One Frequency* gives no solution for every $b$: some data are unobtainable at that frequency. **The unobtainable data are exactly the cokernel, so the zero set is not a defect of the method but a property of the equation**, and the zero set, together with the rank on it, is all that the transform reports at a single frequency.

## The Kernel and the Cokernel

**The three spaces.** At a frequency $\zeta$ in the zero set, three spaces are attached to the symbol and they are distinct.

$$
\operatorname{Ann}_L(\sigma_P(\zeta))=\ker L_{\sigma_P(\zeta)},\qquad A\sigma_P(\zeta)=\operatorname{im}L_{\sigma_P(\zeta)},\qquad \operatorname{coker}L_{\sigma_P(\zeta)}=A/A\sigma_P(\zeta).
$$

**Theorem (the three dimensions).** Let $r(\zeta)=\operatorname{rank}L_{\sigma_P(\zeta)}$. Then

$$
\dim\ker L_{\sigma_P(\zeta)}=d-r(\zeta),\qquad \dim\operatorname{im}L_{\sigma_P(\zeta)}=r(\zeta),\qquad \dim\operatorname{coker}L_{\sigma_P(\zeta)}=d-r(\zeta).
$$

*Proof.* Rank–nullity on a $d$-dimensional domain, and the dimension formula for a quotient.

**Remark (the kernel is the indeterminacy, the cokernel is the constraint).** A solution at the frequency $\zeta$ is determined up to the kernel, so the kernel measures the **freedom** in the solution; and the data are constrained to lie in the image, so the cokernel measures the **conditions** on the data. **The corollary of §*Solvability at One Frequency* says that, for the regular representation, the freedom and the number of conditions are equal.** This is why a single rank reports both, and it is why the count of a solution and the count of a constraint cannot be read off separately from the rank alone.

**Proposition (the image is a left ideal, and it is proper exactly on the zero set).** $A\sigma_P(\zeta)$ is a left ideal of $A$, it equals $A$ exactly when $\zeta\notin Z(P)$, and at a zero it is a proper left ideal whose dimension is $r(\zeta)$.

*Proof.* The image is $Aa$, and $b(ax)=(ba)x$ shows that it is a left ideal. If $\zeta\notin Z(P)$ then $a$ is a unit and $Aa=A$; otherwise $Aa$ is proper and its dimension is $r(\zeta)$ by rank–nullity.

**Remark (what "proper left ideal" adds).** For $A=\mathbb{C}$ the only proper left ideal is $0$, so at a zero the image collapses and every non-zero datum is unobtainable. **For a non-simple $A$ the image at a zero is a non-trivial ideal: some data remain obtainable, and the equation remains partly solvable.** That is the sense in which a zero divisor is milder than a zero, and it is the reason the zero set of a symbol over a non-simple algebra has to be described stratum by stratum, one stratum for each rank, rather than as a single obstacle.

## The Order and the Degree

**Proposition (order against degree).** If $P$ has order $m$ and coefficients in $A$, then the symbol has degree $m$ in $\zeta$, and $\det L_{\sigma_P}$ has degree $dm$.

*Proof.* The monomial $(i\zeta)^\alpha$ has degree $\lvert\alpha\rvert$, so the top-degree part of $\sigma_P$ is the principal symbol, of degree $m$. The determinant of a $d\times d$ matrix whose entries are polynomials of degree $m$ has degree $dm$.

**Remark (the derivative count is the degree).** Each derivative costs one factor of $\zeta$, and each factor of $\zeta$ costs one degree of the symbol. **The order of the operator and the degree of its symbol are the same integer, and the transform makes them the same object**: the count of derivatives in $x$ becomes the count of powers in $\zeta$. This is the exact sense in which the transform exchanges the order in the position for the degree in the frequency.

**Corollary (the degree of the obstruction).** The zero set is the zero set of a polynomial of degree $dm$ in $n$ variables. Over $\mathbb{C}$ its dimension is at least $n-1$ when it is non-empty and proper, by the principal ideal theorem; it is a cone when $\sigma_P$ is homogeneous of degree $m$. The real zero set can be smaller, and in the third shape of §*The Zero Set* it is smaller by exactly one dimension.

*Proof.* The determinant is a single polynomial; if it is not a unit, its zero set in $\mathbb{C}^n$ has dimension at least $n-1$. If $\sigma_P$ is homogeneous then so is $\det L_{\sigma_P}$, and a homogeneous polynomial vanishes on the cone through each of its zeros.

**Remark (homogeneity is the exception, not the rule).** **An operator of order $m$ with a non-zero coefficient of order $0$ has a symbol that is not homogeneous, and its zero set is then a level set and not a cone.** The constant term shifts the level, and — for a symbol whose quadratic part is degenerate — it can split one level set into several components. The degree $dm$ therefore records the order and not the shape: two operators of the same order have determinants of the same degree and zero sets of different shape.

## Two Multipliers That Do Not Commute

**The question.** The theorem of §*The Transform as Left Multiplication* diagonalizes the operator at each frequency. It does not diagonalize the *element*: a symbol that is a sum of non-commuting terms is a single element of $A$, and the question is whether it can be written as a scalar in some basis.

**Proposition (a commuting family has a common reduction).** Let $B\subseteq A$ be a commutative subalgebra and suppose $\sigma_P(\zeta)\in B$ for every $\zeta$. Then $L_{\sigma_P(\zeta)}$ preserves every $B$-invariant subspace, and on each character $\chi$ of $B$ the operator acts by the scalar $\chi(\sigma_P(\zeta))$.

*Proof.* Left multiplication by an element of $B$ commutes with left multiplication by every element of $B$, so the family is simultaneously reducible; on a character space the multiplication by $b\in B$ is the scalar $\chi(b)$.

**Proposition (no common reduction without commutation).** If $a,b\in A$ do not commute, there is no basis of $A$ in which both $L_a$ and $L_b$ are diagonal.

*Proof.* If both were diagonal in one basis then $L_aL_b$ and $L_bL_a$ would have the same diagonal, hence be equal, hence $ab=ba$ by the injectivity of the regular representation.

**Remark (the consequence for the symbol).** **A symbol whose terms do not commute cannot be reduced to a scalar by a change of basis, and the equation at the frequency is therefore a matrix equation and not a scalar one.** The transform has done all that a transform can do: it has replaced the derivative by an element. It cannot replace the element by a number, because the algebra does not permit it. The two roots of a quadratic symbol in a non-commutative algebra need not commute with one another, and the description of the solutions as two independent branches is then unavailable. **What the transform leaves is a single element, and a single element of a non-commutative algebra is not a tuple of scalars.**

## What the Transform Does Not Do

**Variable coefficients.** If a coefficient depends on $x$, the transform of $a(x)u$ is the convolution $\mathcal{F}[a]*\mathcal{F}[u]$ and not a product. The symbol at a single frequency is then not sufficient, because the value of $\mathcal{F}[u]$ at $\zeta$ receives contributions from every frequency through $\mathcal{F}[a]$. The local statement survives in a weaker form: the **principal** symbol still governs the leading behaviour, because the correction terms of the composition law are of lower order, and this is the content of the calculus of *Differential Operators*.

**Remark (the exact failure).** For variable coefficients the theorem of §*The Transform as Left Multiplication* **fails at the lower orders and holds at the top**. The operator is still, to leading order, the multiplication by the principal symbol, and the lower-order terms become a convolution. This is why the zero set of the principal symbol is the invariant object of the theory and the full symbol is not.

**The inverse.** This article has not inverted anything. For a homogeneous equation the transform of a solution is supported in the zero set of the symbol, and reading the solution back from that support is *The Fourier Operator*. The two articles are separated because the forward statement is linear algebra and the inverse statement is contour analysis, and because the inverse needs a growth condition that the forward statement does not.

**The topological setting.** Nothing here has used a topology on $A$ or on the space of functions beyond the compact support that makes the transform an integral: the theorem is an identity between distributions, and the zero set is a set of frequencies. That is why every statement is stable under the choice of test-function space, and why the analysis of the whole problem sits in the inversion and not in the algebra.

## Summary

The transform of a constant-coefficient operator with coefficients in a finite-dimensional algebra is the left multiplication by the symbol: $\mathcal{F}[P(D)u]=L_{\sigma_P(\zeta)}\mathcal{F}[u]$. The equation at each frequency is therefore $a\,x=b$ with $a=\sigma_P(\zeta)$, and it is solvable for every $b$ exactly when $a$ is a unit, which is exactly when $\det L_a\ne0$. The kernel of $L_a$ is the freedom in the solution, the cokernel is the constraint on the data, and the two have the same dimension, $d-\operatorname{rank}L_a$, by rank–nullity. The zero set of the symbol is the zero set of the single polynomial $\det L_{\sigma_P}$, of degree $dm$; it is a point or empty, a hypersurface, or a linear subspace, according to the algebra: a division algebra, a matrix or split algebra, an algebra with a nilpotent radical.

Three sentences carry the article. **The transform replaces a derivative by an element.** **The element is a unit or it is not, and a determinant decides.** **The set where it is not a unit is the only obstruction the transform reports, and it is a set with a shape.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A finite-dimensional real associative algebra with unit, of dimension $d$ |
| $A_{\mathbb{C}}$ | The complexification $A\otimes_{\mathbb{R}}\mathbb{C}$, where the symbol takes its values |
| $d$ | The dimension of $A$ over $\mathbb{R}$, and the size of the regular matrix |
| $L_a$ | Left multiplication by $a$, $L_a(x)=ax$; an endomorphism of $A$ as a real vector space, right $A$-linear |
| $R_a$ | Right multiplication, $R_a(x)=xa$, used only for contrast |
| $\det L_a$ | The determinant of the regular representation of $a$; a homogeneous polynomial of degree $d$ |
| $\operatorname{Ann}_L(a)$ | The left annihilator $\{x:ax=0\}=\ker L_a$ |
| $\operatorname{coker}L_a$ | The cokernel $A/Aa$ of the left multiplication |
| $P(D)$ | A constant-coefficient differential operator $\sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ with $a_\alpha\in A$ |
| $\sigma_P(\zeta)$ | The symbol $\sum a_\alpha(i\zeta)^\alpha$; an $A_{\mathbb{C}}$-valued polynomial of degree $m$ |
| $m$ | The order of $P$, and the degree of $\sigma_P$ |
| $Z(P)$ | The zero set $\{\zeta:\sigma_P(\zeta)$ is not a unit$\}=\{\zeta:\det L_{\sigma_P(\zeta)}=0\}$ |
| $r(\zeta)$ | The rank of $L_{\sigma_P(\zeta)}$ at the frequency $\zeta$ |
| $M_r(\mathbb{R})$ | The algebra of real $r\times r$ matrices, of dimension $r^2$; the matrix algebra used for the examples |
| $N$ | The norm of a division algebra, $N(a)=a\bar a$; the reduced determinant in the matrix case |
| $\mathbb{B}$, $\tilde Q$ | The biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of dimension $8$, and its element $Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ |
| $N(\tilde Q)$ | The algebraic norm $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, central and complex-valued; $\det L_{\tilde Q}=\lvert N(\tilde Q)\rvert^4$ |
| $s$ | The Euclidean square $\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2$ of the gradient example |
| $\mathbb{R}[\varepsilon]$ | The dual numbers, $\varepsilon^2=0$; the algebra with a nilpotent unit used for the third shape |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (2nd ed., Springer, 1990), for the symbol, the principal symbol, the characteristic set and the composition law in the variable-coefficient case.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (Springer, 1983), for the parametrix and the passage from the pointwise invertibility of the symbol to a fundamental solution.
- Elias M. Stein, *Harmonic Analysis* (Princeton University Press, 1993), for the Fourier transform and its multipliers in the scalar case, which is the case $A=\mathbb{C}$ of this article.
- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the ideals, the quotients and the rank–nullity arguments used in §*The Kernel and the Cokernel*.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the classification of the real algebras by their quadratic forms, which is what decides the shape of the zero set.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure of a finite-dimensional algebra, its radical, its simple factors and its reduced norm.
- T. Y. Lam, *A First Course in Noncommutative Rings* (2nd ed., Springer, 2001), for the units, the zero divisors and the one-sided ideals of a finite-dimensional algebra.
