
# __Split-Complex Analysis on Subspaces__

## Introduction

The article *Split Complex Analysis* defines the differential calculus of a split-complex variable and its Cauchy–Riemann operator; the article *Split-Complex Integration* defines the integral on the same domain. This article specializes the theory to the two one-dimensional real subspaces of $\mathbb{D}$ — the real line $\mathbb{R}_{\mathbb{D}}$ and the split imaginary line $j\mathbb{R}_{\mathbb{D}}$ — and then rewrites the Cauchy–Riemann operator in the idempotent coordinates and its two components, reducing every analytic statement to two independent copies of the real line. It is the two-dimensional counterpart of *Biquaternion Analysis on Subspaces*, and the degeneration is complete: the four four-dimensional subspaces of the biquaternion theory become two lines, and the abstract operators become ordinary derivatives of one variable.

The article owns the differential operators on the two subspaces, the Cauchy–Riemann operator in the idempotent coordinates, the two-component form of split differentiability, the reduction to $\mathbb{R}\oplus\mathbb{R}$, and the role of the zero divisors in that reduction. It assumes the algebra and the conjugation of *Split-Complex Algebra*, the idempotents of *Split-Complex Idempotents and Projections*, the subspaces of *Split-Complex Subspaces*, and the differentiability theory of *Split Complex Analysis*; the zero divisors are treated in *Split-Complex Zero Divisors*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1$, $j$ with $j^2=+1$; a general element is $Z=a+j b$ with $a,b\in\mathbb{R}$; the idempotents are $\Pi_\pm=\tfrac12(1\pm j)$ with idempotent coordinates $Z_\pm=a\pm b$; the norm form is $N(Z)=a^2-b^2$. Functions are written $f=f_+\Pi_1 + f_-\Pi_2$ with $f_\pm$ real-valued. The wave operator (d'Alembertian) is $\Box=\partial_a^2-\partial_b^2$.

## The Two Subspaces and Their Differential Operators

The conjugation $\bar Z=a-j b$ has fixed subspace the real line $\mathbb{R}_{\mathbb{D}}=\{a\}$ and anti-fixed subspace the split imaginary line $j\mathbb{R}_{\mathbb{D}}=\{j b\}$, each of real dimension $1$, and $\mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$.

**Definition.** The differential operator of the real subspace is the derivative $\partial_a = \mathrm{d}/\mathrm{d}a$ along $\mathbb{R}_{\mathbb{D}}$, and the differential operator of the split imaginary subspace is the derivative $\partial_b = \mathrm{d}/\mathrm{d}b$ along $j\mathbb{R}_{\mathbb{D}}$.

**Theorem.** On each one-dimensional real subspace the Cauchy–Riemann operator of the general theory reduces to the ordinary derivative, with no residual Cauchy–Riemann condition: a real-valued function on $\mathbb{R}_{\mathbb{D}}$ or on $j\mathbb{R}_{\mathbb{D}}$ is differentiable in the sense of the general theory exactly when it has an ordinary derivative, and the operator of the subspace is $\partial_a$ or $\partial_b$ accordingly.

**Proof.** A real-valued function on a one-dimensional real space has a derivative iff it is differentiable in its single variable; there is no second real direction along which a Cauchy–Riemann condition could be imposed, so the pair of conditions of the plane collapses to the existence of the derivative. The operators $\partial_a$ and $\partial_b$ are the two commuting coordinate derivations of the plane, restricted to their respective axes. $\square$

The two operators commute, $\partial_a\partial_b=\partial_b\partial_a$, and their squares combine into the wave operator

$$
\Box=\partial_a^2-\partial_b^2,
$$

the signature-$(1,1)$ Laplace operator, which is the **d'Alembertian** of the plane. It is the second-order operator determined by the norm form, in the same way that the Laplacian is determined by a definite form, and it satisfies

$$
\Box = 4\,\frac{\partial}{\partial Z}\frac{\partial}{\partial \bar Z}
$$

for the Wirtinger operators introduced below. The division by the two subspaces is the statement that the plane is the direct sum of the two axes and the second-order operator is the difference of the two one-dimensional second derivatives.

## The Cauchy–Riemann Operator and the Wirtinger Derivatives

**Definition.** The **split Wirtinger derivatives** of a differentiable function $f$ are

$$
\frac{\partial}{\partial Z}=\frac12\Bigl(\partial_a + j\,\partial_b\Bigr), \qquad \frac{\partial}{\partial \bar Z}=\frac12\Bigl(\partial_a - j\,\partial_b\Bigr).
$$

**Theorem (calculus of the Wirtinger operators).** The Wirtinger operators annihilate the conjugate variable and reproduce the coordinate derivatives:

$$
\frac{\partial Z}{\partial Z}=1, \qquad \frac{\partial \bar Z}{\partial Z}=0, \qquad \frac{\partial Z}{\partial \bar Z}=0, \qquad \frac{\partial \bar Z}{\partial \bar Z}=1,
$$

the total differential of a differentiable function is $df=\tfrac{\partial f}{\partial Z}\,dZ+\tfrac{\partial f}{\partial\bar Z}\,d\bar Z$ with $dZ=d a+j\,d b$ and $d\bar Z=d a-j\,d b$, and a function is split complex differentiable iff $\partial f/\partial\bar Z = 0$, in which case $f'(Z)=\partial f/\partial Z$.

**Proof.** Apply $\partial_Z=\tfrac12(\partial_a+j\partial_b)$ to $Z=a+j b$: $\partial_a Z=1$ and $\partial_b Z=j$, so $\partial_Z Z=\tfrac12(1+j\cdot j)=\tfrac12(1+1)=1$, and $\partial_Z\bar Z=\tfrac12(1+j\cdot(-j))=\tfrac12(1-1)=0$. The formulas for $\partial_{\bar Z}$ follow by $j\mapsto-j$. The differentiability criterion is the content of the Cauchy–Riemann theorem of *Split Complex Analysis*, restated in the Wirtinger language. $\square$

**Corollary (the Cauchy–Riemann equations).** Writing $f=u+jv$ with $u,v$ real, the condition $\partial f/\partial\bar Z=0$ is equivalent to

$$
\partial_a u = \partial_b v, \qquad \partial_b u = \partial_a v,
$$

the split Cauchy–Riemann equations, and it implies $\Box u=\Box v=0$.

**Remark (the contrast with the complex field).** For $\mathbb{C}$ the analogous operators give the Cauchy–Riemann equations $\partial_a u=\partial_b v$, $\partial_b u=-\partial_a v$ and the Laplacian $\partial_a^2+\partial_b^2$; the single sign difference in the second equation, inherited from $j^2=+1$ against $i^2=-1$, turns the harmonic functions into the wave functions. The analysis on the two subspaces is otherwise identical in shape.

## The Cauchy–Riemann Operator in the Idempotent Coordinates

The idempotent coordinates are $Z_+=a+b$ and $Z_-=a-b$, with $a=\tfrac12(Z_++Z_-)$ and $b=\tfrac12(Z_+-Z_-)$, so the coordinate derivatives transform as

$$
\partial_{Z_+}=\tfrac12(\partial_a+\partial_b), \qquad \partial_{Z_-}=\tfrac12(\partial_a-\partial_b), \qquad \partial_a=\partial_{Z_+}+\partial_{Z_-}, \qquad \partial_b=\partial_{Z_+}-\partial_{Z_-}.
$$

**Theorem (the Cauchy–Riemann operator and its two components).** In the idempotent coordinates the Cauchy–Riemann operator has the two-component form

$$
\frac{\partial}{\partial Z}=\Pi_1\,\partial_{Z_+}+\Pi_2\,\partial_{Z_-}, \qquad \frac{\partial}{\partial \bar Z}=\Pi_2\,\partial_{Z_+}+\Pi_1\,\partial_{Z_-},
$$

acting on $f=f_+\Pi_1 + f_-\Pi_2$ by

$$
\frac{\partial f}{\partial Z}=\bigl(\partial_{Z_+}f_+\bigr)\Pi_1 + \bigl(\partial_{Z_-}f_-\bigr)\Pi_2, \qquad \frac{\partial f}{\partial \bar Z}=\bigl(\partial_{Z_-}f_+\bigr)\Pi_1 + \bigl(\partial_{Z_+}f_-\bigr)\Pi_2.
$$

**Proof.** Substitute $\partial_a=\partial_{Z_+}+\partial_{Z_-}$ and $\partial_b=\partial_{Z_+}-\partial_{Z_-}$ into $\partial_Z=\tfrac12(\partial_a+j\partial_b)$ and use $1+j=2\Pi_1$, $1-j=2\Pi_2$:

$$
\frac{\partial}{\partial Z}=\tfrac12\bigl(\partial_{Z_+}+\partial_{Z_-}\bigr)+\tfrac12 j\bigl(\partial_{Z_+}-\partial_{Z_-}\bigr)=\partial_{Z_+}\tfrac{1+j}{2}+\partial_{Z_-}\tfrac{1-j}{2}=\Pi_1\,\partial_{Z_+}+\Pi_2\,\partial_{Z_-}.
$$

The form for $\partial_{\bar Z}$ is the same with $j\mapsto-j$. Applying to $f$ and using $\Pi_1\Pi_2=0$, $\Pi_\pm^2=\Pi_\pm$ and $j \Pi_1=\pm \Pi_1$ (with $+$ for $\Pi_1$ and $-$ for $\Pi_2$) gives the two displayed component forms. $\square$

So the Cauchy–Riemann operator has exactly **two components**, $\partial_{Z_+}$ and $\partial_{Z_-}$, and the idempotents $\Pi_\pm$ are the spectral projections that separate them. This is the precise sense in which the differential calculus of $\mathbb{D}$ decomposes along the two components.

## Reduction to the Two Copies of $\mathbb{R}$

**Theorem (split differentiability is componentwise).** A function $f=f_+\Pi_1 + f_-\Pi_2$ is split complex differentiable iff

$$
\partial_{Z_-}f_+=0 \qquad\text{and}\qquad \partial_{Z_+}f_-=0,
$$

that is, iff $f_+=F_+(Z_+)$ and $f_-=F_-(Z_-)$ for differentiable real functions $F_\pm$ of one real variable. Every analytic statement about $f$ is then the corresponding statement about $F_+$ and $F_-$ separately, and

$$
f'(Z)=F_+'(Z_+)\,\Pi_1 + F_-'(Z_-)\,\Pi_2 .
$$

**Proof.** By the two-component form of $\partial_{\bar Z}$, the equation $\partial f/\partial\bar Z=0$ reads $(\partial_{Z_-}f_+)\Pi_1 + (\partial_{Z_+}f_-)\Pi_2=0$, which by the linear independence of $\Pi_1$ and $\Pi_2$ is the pair $\partial_{Z_-}f_+=0$, $\partial_{Z_+}f_-=0$. These say that $f_+$ is constant along $Z_-$ (hence a function of $Z_+$ alone) and $f_-$ is constant along $Z_+$ (hence a function of $Z_-$ alone). The derivative formula follows from $\partial_Z=\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}$. $\square$

**Corollary (the reduction).** Under the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ the algebra of split differentiable functions is the direct product

$$
\mathcal{H}(\mathbb{D})\cong \mathcal{H}(\mathbb{R})\times\mathcal{H}(\mathbb{R}), \qquad f\longmapsto (F_+,F_-),
$$

of two copies of the algebra of differentiable functions of one real variable. Limits, continuity, differentiability, integration and power series all hold componentwise; the integral of $f$ over a contour in $\mathbb{D}$ is the pair of one-dimensional integrals of $F_+$ and $F_-$; and the Cauchy integral formula of *Split-Complex Integration* reduces to the fundamental theorem of calculus on each copy of $\mathbb{R}$.

**Proof.** Each of the operations is defined by the algebra operations and the Wirtinger operators, all of which are componentwise in the idempotent basis; so each statement about $f$ is the conjunction of the two statements about $F_\pm$. $\square$

**Remark (no complex-analytic content).** Over $\mathbb{R}$ the equation $\partial_{Z_-}f_+=0$ has no regularity consequence beyond differentiability: $F_+$ is an arbitrary differentiable function of one real variable, not a holomorphic function of a complex variable. So the function theory of $\mathbb{D}$ is the real analysis of two independent one-variable functions, and the theorems that make complex analysis deep — the identity theorem, the maximum principle, Liouville's theorem — have no counterpart here. Where the split power series of *Split Complex Analysis* appear, they are the diagonal case $F_+=F_-=A$ for a single real power series $A$, and they form the proper subalgebra of functions given by one series in $Z$.

## Comparison and Relations Between the Two Subspaces

The two subspaces are the eigenspaces of the unique non-trivial involution and are exchanged by multiplication by $j$, which sends $\mathbb{R}_{\mathbb{D}}$ onto $j\mathbb{R}_{\mathbb{D}}$ and back,

$$
j\,\bigl(j\mathbb{R}_{\mathbb{D}}\bigr)=j^2\mathbb{R}_{\mathbb{D}}=\mathbb{R}_{\mathbb{D}},
$$

so $j$ is an $\mathbb{R}$-linear isomorphism between them, and the conjugation fixes $\mathbb{R}_{\mathbb{D}}$ pointwise while negating $j\mathbb{R}_{\mathbb{D}}$ pointwise. Their norms have opposite signs, $N|_{\mathbb{R}_{\mathbb{D}}}=a^2$ and $N|_{j\mathbb{R}_{\mathbb{D}}}=-b^2$, so the real subspace is the positive curve and the split imaginary subspace the negative curve of the form; the d'Alembertian $\Box=\partial_a^2-\partial_b^2$ is the difference of their second derivatives.

| feature | $\mathbb{R}_{\mathbb{D}}$ | $j\mathbb{R}_{\mathbb{D}}$ |
|---|---|---|
| dimension | $1$ | $1$ |
| coordinate | $a$ | $b$ |
| differential operator | $\partial_a$ | $\partial_b$ |
| involution $\bar{\cdot}$ | $+1$ | $-1$ |
| restricted $N$ | $a^2$, positive | $-b^2$, negative |
| image under $j$ | $j\mathbb{R}_{\mathbb{D}}$ | $\mathbb{R}_{\mathbb{D}}$ |
| idempotent coordinates | $Z_+=Z_-=a$ | $Z_+=-Z_-=b$ |

In the idempotent coordinates the two subspaces appear as the two diagonal directions $Z_+=Z_-$ and $Z_+=-Z_-$; the change from the eigenbasis $\{a,b\}$ to the idempotent basis $\{Z_+,Z_-\}$ is the linear map of *Split-Complex Subspaces*, and the two decompositions of the plane are the two ways of splitting the same two-dimensional domain.

## The Role of the Zero Divisors

**Theorem.** The idempotents $\Pi_1$ and $\Pi_2$ are zero divisors, and their orthogonality is what makes the differential calculus split. In the algebra of split differentiable functions the two components are annihilated by the opposite idempotent,

$$
\Pi_2 f_+ \Pi_1=0, \qquad \Pi_1 f_- \Pi_2=0,
$$

so the projection of a differentiable function onto one component is itself differentiable and independent of the other.

**Proof.** $\Pi_\pm^2=\Pi_\pm$ and $\Pi_1\Pi_2=0$ give $\Pi_2(f_+\Pi_1)=0$ and $\Pi_1(f_-\Pi_2)=0$. The component $f_+\Pi_1$ depends only on $Z_+$ by the reduction theorem, and it is killed by multiplication by $\Pi_2$; the statements are the algebraic form of the two-component splitting of $\partial/\partial\bar Z$. $\square$

**Corollary (the failure of the domain property).** The algebra of split differentiable functions has zero divisors: for any two differentiable functions, $(F_+\Pi_1)(G_-\Pi_2)=0$ and $(F_-\Pi_2)(G_+\Pi_1)=0$. Consequently the product of two nonvanishing differentiable functions can vanish, and the function algebra is not an integral domain.

**The null cone in the analysis.** The two null lines $a=\pm b$, equivalently $Z_+=0$ or $Z_-=0$, are the locus on which the idempotent coordinate degenerates: on the line $Z_+=0$ the component $\Pi_1$ of any function is evaluated at the branch point of the coordinate change, and the modulus $\sqrt{\lvert N\rvert}$ vanishes. This is where the polar decomposition of the analysis fails and where the division by $Z$, an operation of the derivative, may lose invertibility; the criterion $N(Z)\neq0$ of *Split-Complex Norm and Invertibility* is exactly the condition that the point of evaluation be a unit, so that the difference quotient of the definition of the derivative is defined.

**Remark (why the zero divisors matter here).** In the biquaternion theory the zero-divisor cone is the set on which the partial polar decomposition degenerates, and the four subspace operators are nonsingular away from it. In the split-complex theory the same phenomenon is elementary and total: the zero divisors $\Pi_\pm$ are the coordinate projectors themselves, so the decomposition that makes the analysis tractable is built from the very elements that destroy the domain property.

## Summary

The two one-dimensional real subspaces of the split-complex plane are the fixed line $\mathbb{R}_{\mathbb{D}}$ and the anti-fixed line $j\mathbb{R}_{\mathbb{D}}$, carrying the ordinary derivatives $\partial_a$ and $\partial_b$; on a one-dimensional real subspace the Cauchy–Riemann operator reduces to the derivative, and the two operators combine into the wave operator $\Box=\partial_a^2-\partial_b^2=4\,\partial_Z\partial_{\bar Z}$. The Wirtinger derivatives $\partial_Z=\tfrac12(\partial_a+j\partial_b)$ and $\partial_{\bar Z}=\tfrac12(\partial_a-j\partial_b)$ reproduce the split Cauchy–Riemann equations $\partial_a u=\partial_b v$, $\partial_b u=\partial_a v$, whose only difference from the complex equations is the sign of the second, inherited from $j^2=+1$.

In the idempotent coordinates the Cauchy–Riemann operator becomes the two-component operator $\partial_Z=\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}$, and $\partial_{\bar Z}=\Pi_2\partial_{Z_+}+\Pi_1\partial_{Z_-}$ swaps the components; split differentiability is the pair of conditions $\partial_{Z_-}f_+=0$, $\partial_{Z_+}f_-=0$, so the split differentiable functions are exactly $f=F_+(Z_+)\Pi_1 + F_-(Z_-)\Pi_2$ for differentiable one-variable functions $F_\pm$. Every analytic statement therefore reduces to two independent copies of real one-variable analysis, limits, continuity, differentiation, integration and series holding componentwise, and the function algebra is the direct product $\mathcal{H}(\mathbb{D})\cong\mathcal{H}(\mathbb{R})\times\mathcal{H}(\mathbb{R})$; the split power series form the diagonal subalgebra $F_+=F_-$. The two subspaces are exchanged by multiplication by $j$, are the $+1$ and $-1$ eigenspaces of the involution, and carry the positive and negative restrictions of the norm form. The zero divisors $\Pi_\pm$ are the coordinate projectors of this reduction: their orthogonality makes the calculus split, and it also makes the function algebra fail to be a domain, since $(F_+\Pi_1)(G_-\Pi_2)=0$; the null cone $a=\pm b$ is the locus where the idempotent coordinate degenerates and the derivative's difference quotient loses a unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | Split complex variable |
| $\mathbb{R}_{\mathbb{D}} = \{a\}$ | Real subspace, fixed line of $\bar{\cdot}$ |
| $j\mathbb{R}_{\mathbb{D}} = \{j b\}$ | Split imaginary subspace, anti-fixed line |
| $\partial_a,\ \partial_b$ | Derivatives along the two subspaces |
| $\Box = \partial_a^2-\partial_b^2$ | Wave operator (d'Alembertian) |
| $\partial_Z=\tfrac12(\partial_a+j\partial_b)$ | Split Wirtinger derivative, the Cauchy–Riemann operator |
| $\partial_{\bar Z}=\tfrac12(\partial_a-j\partial_b)$ | Conjugate Wirtinger derivative |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Idempotents, the two components |
| $Z_\pm = a\pm b$ | Idempotent coordinates |
| $\partial_{Z_\pm}=\tfrac12(\partial_a\pm\partial_b)$ | Component derivatives |
| $\partial_Z=\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}$ | Cauchy–Riemann operator in idempotent coordinates |
| $f = f_+\Pi_1 + f_-\Pi_2$ | Two-component form of a function |
| $f=F_+(Z_+)\Pi_1 + F_-(Z_-)\Pi_2$ | General split differentiable function |
| $\mathcal{H}(\mathbb{D})\cong\mathcal{H}(\mathbb{R})\times\mathcal{H}(\mathbb{R})$ | Reduction of the function algebra |
| $N(Z)=a^2-b^2$ | Norm form; unit criterion $N\neq0$ |

## Further Reading

- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 3rd ed. 1976), for the one-variable real analysis to which the split calculus reduces.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 3rd ed. 1987), for the comparison between real one-variable analysis and complex analysis.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split Cauchy–Riemann equations and the wave operator of the split complex plane.
- G. B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the d'Alembertian, its factorization and its characteristic lines.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Cauchy–Riemann operator of the split complex algebra and its components.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for Cauchy–Riemann operators on subspaces and their idempotent decomposition.
