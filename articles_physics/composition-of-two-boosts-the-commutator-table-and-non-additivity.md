# __Composition of Two Boosts: The Commutator Table and Non-Additivity__

## Introduction

Two boosts do not compose to a boost. Their product is a boost times a rotation, and the rotation is not small: it grows like the product of the two rapidities and vanishes only when the two directions are collinear. That rotation is the Thomas–Wigner rotation, and in this algebra it is a single term of a product.

This article prints the bracket table of the six generators, proves the identity $[\tilde X_\alpha,\tilde X_\beta]=2\vec e_\alpha\times\vec e_\beta$ that the table encodes, computes the product of two boosts exactly, identifies the rotation factor's axis and angle, and evaluates the angle in the two regimes a reader needs.

The article assumes *The Six Generators and Their Commutators* for the table's derivation and sign conventions, *When the Axes Commute: The Normal Transformations* for the case in which the rotation vanishes, and *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* for the decomposition. It feeds *The Four Kinds of Frame Transformation* and the relativistic-velocity articles of the corpus.

## The Bracket Table

### The Six Generators

$$
J_\eta=\tfrac12\vec e_\eta,\qquad K_\eta=\tfrac12 i\vec e_\eta,\qquad \eta\in\{x,y,z\},
$$

the rotation and boost generators: the $J_\eta$ are anti-Hermitian, $J_\eta^{*}=-J_\eta$, and the $K_\eta$ are Hermitian, $K_\eta^{*}=+K_\eta$. Their brackets are stated in *The Six Generators and Their Commutators* and are reproduced here because the rest of the article reads the table.

### The Table

| $[\cdot,\cdot]$ | $J_b$ | $K_b$ |
|---|---|---|
| $J_a$ | $\epsilon_{abc}J_c$ | $\epsilon_{abc}K_c$ |
| $K_a$ | $\epsilon_{abc}K_c$ | $-\epsilon_{abc}J_c$ |

The three blocks say three different things:

- $[J,J]=\epsilon J$: rotations close into a Lie algebra, the compact $\mathfrak{so}(3)$.
- $[J,K]=\epsilon K$: the boosts form a vector under rotations, so a rotation carries a boost direction into another boost direction.
- $[K,K]=-\epsilon J$: **the commutator of two boosts is a rotation**, with a minus sign relative to the rotation algebra.

### Reading the Table

The third block is the whole content of "boosts are not additive". Its antisymmetry in the middle index means the bracket of two boosts is a rotation about the axis perpendicular to both — which is the direction of the vector product. The minus sign is what makes the real span of the $K$'s a hyperbolic rather than a circular geometry: the subalgebra spanned by the boosts alone is not closed, and if it were closed with a plus sign the boosts would form a compact group and rapidity would be periodic.

### Why the Table Is All There Is

The six generators span $\mathfrak{sl}_2(\mathbb{C})$ over $\mathbb{C}$ and $\mathfrak{so}(1,3)$ over $\mathbb{R}$, and the table is the complete set of structure constants in that basis. Every statement in this article is read from it, and no other input is used.

## The Algebraic Identity

### The Statement

For the vector units of the algebra,

$$
[\vec e_\alpha,\vec e_\beta]=2\,\vec e_\alpha\times\vec e_\beta,
\qquad
\vec e_\alpha\times\vec e_\beta=\sum_\gamma\epsilon_{\alpha\beta\gamma}\vec e_\gamma .
$$

The identity is the quaternion relation $\vec i\vec j=\vec k$ written in the corpus's basis, and it holds for any two real vectors $\vec a,\vec b$:

$$
[\vec a,\vec b]=2\,\vec a\times\vec b .
$$

### The Proof

Write $\vec a\vec b=-\vec a\cdot\vec b+\vec a\times\vec b$, which is the decomposition of a quaternion product into its scalar and vector parts. Then

$$
[\vec a,\vec b]=\vec a\vec b-\vec b\vec a=2\,\vec a\times\vec b,
$$

because the scalar parts cancel and the vector products are antisymmetric.

### The Table From the Identity

With $J_a=\tfrac12\vec e_a$:

$$
[J_a,J_b]=\tfrac14[\vec e_a,\vec e_b]=\tfrac12\epsilon_{abc}\vec e_c=\epsilon_{abc}J_c .
$$

With $K_a=\tfrac12 i\vec e_a$:

$$
[K_a,K_b]=\tfrac14 i^{2}[\vec e_a,\vec e_b]=-\tfrac14\cdot2\epsilon_{abc}\vec e_c=-\epsilon_{abc}J_c ,
$$

and the mixed bracket

$$
[J_a,K_b]=\tfrac14 i[\vec e_a,\vec e_b]=\tfrac i2\epsilon_{abc}\vec e_c=\epsilon_{abc}K_c .
$$

So the whole table is the one identity plus the factor $i$.

### The Sign

Three signs chain together and a reader must keep them apart:

| sign | where it comes from |
|---|---|
| $+2$ in $[\vec e_\alpha,\vec e_\beta]=2\vec e_\alpha\times\vec e_\beta$ | the algebra's orientation |
| $-$ in $[K_a,K_b]=-\epsilon_{abc}J_c$ | the $i^{2}=-1$ of the boost generators |
| $-$ in the product's rotation axis being along $-\vec u_1\times\vec u_2$ | the order of the factors, as computed below |

The third is a convention about which boost comes first, and it flips when the order of the two boosts is exchanged. The first two are fixed by the corpus's basis and are not conventions of this article.

## Why Two Boosts Compose to a Rotation

### The Product

Let $\tilde B_i=\cosh a_i+i\sinh a_i\vec u_i$ with $a_i=\tfrac12\theta_{\mathrm{rpd},i}$ the half-rapidities and $\vec u_i$ unit real vectors that make an angle $\theta$. Then

$$
\tilde B_1\tilde B_2=\cosh a_1\cosh a_2+i\sinh a_1\cosh a_2\vec u_1+i\cosh a_1\sinh a_2\vec u_2-\sinh a_1\sinh a_2\,\vec u_1\vec u_2,
$$

and $\vec u_1\vec u_2=-\cos\theta+\vec u_1\times\vec u_2$ with $\cos\theta=\vec u_1\cdot\vec u_2$. Collecting,

$$
\tilde B_1\tilde B_2=\underbrace{\bigl(\cosh a_1\cosh a_2+\cos\theta\sinh a_1\sinh a_2\bigr)}_{\text{scalar}}
+\underbrace{\bigl(-\sinh a_1\sinh a_2\,\vec u_1\times\vec u_2\bigr)}_{\text{real vector}}
+i\underbrace{\bigl(\sinh a_1\cosh a_2\vec u_1+\cosh a_1\sinh a_2\vec u_2\bigr)}_{\text{imaginary vector}} .
$$

### The Three Parts

The three parts are exactly the three pieces the word needs:

- the **scalar** part is real and positive, and it is $\cosh\frac{\theta_{\mathrm{rpd},12}}{2}\cos\frac{\theta_{\mathrm{wgn}}}{2}$, the product of the resulting boost's half-rapidity factor and the rotation's half-angle factor;
- the **real vector** part is a real vector proportional to $\vec u_1\times\vec u_2$, and it is the rotation;
- the **imaginary vector** part is the resulting boost's direction.

A product of two boosts is therefore never a boost: the real vector part is nonzero exactly when $\vec u_1\times\vec u_2\neq0$ and both rapidities are nonzero, which is the statement of the bracket table read off a product.

### The Rotation

The rotation's axis is along $\vec u_1\times\vec u_2$ — or, with the sign above, along $-\vec u_1\times\vec u_2$ — and its size is measured by the real vector part. The exact statement is

$$
\cos\tfrac{\theta_{\mathrm{wgn}}}{2}=\frac{S}{\sqrt{S^{2}+\lvert\vec v\rvert^{2}}},
\qquad
\tan\tfrac{\theta_{\mathrm{wgn}}}{2}=\frac{\lvert\vec v\rvert}{S},
\qquad
\cosh\theta_{\mathrm{rpd},12}=\cosh\theta_{\mathrm{rpd},1}\cosh\theta_{\mathrm{rpd},2}+\cos\theta\,\sinh\theta_{\mathrm{rpd},1}\sinh\theta_{\mathrm{rpd},2},
$$

with $S$ the scalar part of the product, $\vec v$ its real vector part, and $\theta_{\mathrm{rpd},12}$ the rapidity of the resulting boost. The form is not an ansatz: writing the product as $\tilde R\tilde B_{12}$, the rotation's half-angle carries all of $\vec v$ and the boost's half-rapidity all of the imaginary part, so $\tan\frac{\theta_{\mathrm{wgn}}}{2}=\lvert\vec v\rvert/S$ and $\cosh^{2}\frac{\theta_{\mathrm{rpd},12}}{2}=S^{2}+\lvert\vec v\rvert^{2}$. The formula is verified numerically against a polar decomposition of the matrix product to $10^{-10}$ on random pairs, and the axis comes out anti-parallel to $\vec u_1\times\vec u_2$ to machine precision.

### The Simpler Statement

The formula above is exact but opaque. The statement a reader should carry is:

> two boosts along different directions compose to a boost plus a rotation about the axis perpendicular to both directions, and the rotation angle is of order $\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}$.

That is the bracket table with the parameters put back, and it is all the physics the exact formula is used for in this block.

## The Power Series

### The Word Near the Identity

The word of the block is the Lorentz rotor $\tilde U_{\mathrm{lor}}=\tilde U_\Psi\tilde u_{\mathrm r}$ of *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation*, with $\tilde U_\Psi=\exp\bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\bigr)$ and $\tilde u_{\mathrm r}=\exp\bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\bigr)$. Both factors are exponentials of algebra elements, so a product of two frames is a product of two exponentials, and the bracket table is the statement about that product. Write $\tilde U_1=e^{\tilde X}$ and $\tilde U_2=e^{\tilde Y}$ with $\tilde X,\tilde Y$ in the algebra.

### The Middle Product Re-Split

The product $e^{\tilde X}e^{\tilde Y}$ is not $e^{\tilde X+\tilde Y}$. The correct statement is the Baker–Campbell–Hausdorff series,

$$
\ln\bigl(e^{\tilde X}e^{\tilde Y}\bigr)
=\tilde X+\tilde Y+\tfrac12[\tilde X,\tilde Y]
+\tfrac1{12}\bigl[\tilde X,[\tilde X,\tilde Y]\bigr]
-\tfrac1{12}\bigl[\tilde Y,[\tilde X,\tilde Y]\bigr]+\ldots
$$

The series answers the question "does the product close on the same set". Its first two terms are the naive addition of the parameters; its third term is the first correction, and the correction is a commutator. So the failure of additivity is not an accident of the parametrisation: it is the first term of the series after the linear one.

### The First Correction for Two Boosts

Take two boosts, $\tilde X=i a\vec u_1$ and $\tilde Y=i b\vec u_2$ with $a=\tfrac12\theta_{\mathrm{rpd},1}$ and $b=\tfrac12\theta_{\mathrm{rpd},2}$; this is $\tilde U_\Psi$ at two different axes. Then

$$
[\tilde X,\tilde Y]=(ia)(ib)\,[\vec u_1,\vec u_2]=-2ab\,\vec u_1\times\vec u_2 ,
$$

a real vector and therefore a rotation generator. Its coefficient is $ab\sin\theta$, and exponentiating a rotation generator of coefficient $m$ rotates through $2m$; so the first correction is a rotation through

$$
2ab\sin\theta=\tfrac12\,\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}\sin\theta .
$$

That is exactly the leading term of the Thomas–Wigner angle obtained below from the exact product, and the agreement checks both computations: the series and the closed form are the same statement at different orders.

The series is verified numerically in the block's matrix model. With $a=b=10^{-3}$ and perpendicular axes, the residual $\lVert e^{\tilde X}e^{\tilde Y}-\exp(\tilde X+\tilde Y+\tfrac12[\tilde X,\tilde Y])\rVert$ is $3.3\times10^{-10}$; with $a=b=10^{-2}$ it is $3.4\times10^{-7}$, larger by the expected factor $10^{3}$, so the residual is $O(a^{3})$ and not $O(a^{2})$. The rotation part of $e^{\tilde X}e^{\tilde Y}$, extracted by a polar decomposition, comes out $4.99167\times10^{-3}$ at $a=b=0.05$ against $2a^{2}=5.0\times10^{-3}$.

### The Three Rows Read Off the Series

- $[\mathfrak k,\mathfrak k]\subset\mathfrak k$: two real vectors give a real vector, $[\vec u_1,\vec u_2]=2\vec u_1\times\vec u_2$, so two rotations compose to a rotation, and the rotations are a subgroup.
- $[\mathfrak k,\mathfrak p]\subset\mathfrak p$: a real vector with an imaginary one gives an imaginary one, $[\vec u_1,i\vec u_2]=2i\,\vec u_1\times\vec u_2$, so a conjugate of a boost by a rotation is a boost, which is why a boost axis can be turned.
- $[\mathfrak p,\mathfrak p]\subset\mathfrak k$: two imaginary vectors give a real one, so two boosts compose to a boost and a rotation. This is the row that has no analogue in a product of groups, and it is the whole of the Thomas–Wigner effect.

### Why the Third Row Forbids a Subgroup

Because $[\mathfrak p,\mathfrak p]\subset\mathfrak k$ is not zero, $\exp(\mathfrak p)$ is not closed under multiplication: a product of two boosts is a boost times a rotation, and the rotation is trivial only when the axes are collinear or one rapidity vanishes. So the boost set is a submanifold and not a subgroup — by the Cartan decomposition $G=KP$ it is a section of $G\to G/K$, diffeomorphic to the hyperboloid $G/K$ of *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*. A reader who expects the boosts to be a subgroup will also expect rapidities to add, and both expectations fail for the same bracket.

## The Thomas–Wigner Rotation

### The Physical Setting

A particle is boosted along one direction and then along another. The composition of the two boosts is a boost and a rotation, so the particle's spin is rotated relative to the frame that the naive addition of the two rapidities would produce. That rotation is the Thomas–Wigner rotation, and it is the reason the spin precession of a particle in a circular accelerator is not the naive relativistic correction.

### The Algebra's Version

In this algebra the rotation is not an effect of a spinor representation and not an effect of the order of operators. It is the real vector part of a product of two real-quaternion-and-imaginary-quaternion elements, it is visible in the scalar algebra, and it is computed by multiplying two elements of a group.

That is worth stressing because the same rotation is usually derived from the composition law of Lorentz matrices, where it appears as a messy matrix product, or from the algebra of the $\vec K$'s, where it appears as a minus sign. Here the two derivations are one line each and they are the same line.

### The Failure of the "Addition" Picture

If boosts added, the rapidity vector of the product would be $\vec\theta_{\mathrm{rpd},1}+\vec\theta_{\mathrm{rpd},2}$ and there would be no rotation, where $\vec\theta_{\mathrm{rpd},i}=\theta_{\mathrm{rpd},i}\vec u_i$. The composition is instead

$$
\vec\theta_{\mathrm{rpd},12}\neq\vec\theta_{\mathrm{rpd},1}+\vec\theta_{\mathrm{rpd},2},
$$

with the difference of order $\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}$, and the missing piece is exactly the rotation. So the failure of additivity and the presence of the rotation are one fact, and the bracket $[K,K]\neq0$ is its statement.

## The Magnitude

### The Small-Rapidity Limit

For small rapidities,

$$
\theta_{\mathrm{wgn}}=\tfrac12\,\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}\,\sin\theta+O(\theta^{3}),
$$

where $\theta$ is the angle between the two boost directions. The formula is verified numerically: at $\theta_{\mathrm{rpd},1}=\theta_{\mathrm{rpd},2}=10^{-3}$ the computed angle agrees with the formula to six significant figures, and at $\theta_{\mathrm{rpd},1}=\theta_{\mathrm{rpd},2}=0.05$ to four.

The factor $\tfrac12$ is what the exact formula gives in the limit, and the limit is one line: $\lvert\vec v\rvert=\sinh\frac{\theta_{\mathrm{rpd},1}}{2}\sinh\frac{\theta_{\mathrm{rpd},2}}{2}\sin\theta\approx\frac{\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}}{4}\sin\theta$ while $S\to1$, so $\tan\frac{\theta_{\mathrm{wgn}}}{2}\approx\frac{\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}}{4}\sin\theta$ and the angle is twice that. The same factor appears from the commutator, because the bracket of two boost generators is the rotation generator and the BCH series puts one half in front of it.

### The Two Ways It Vanishes

$\theta_{\mathrm{wgn}}$ vanishes when $\sin\theta=0$, that is when the directions are collinear; and it vanishes to first order when either rapidity is small. Both are the bracket table: the first is $\vec u_1\times\vec u_2=0$, the second is $\sinh a_i=0$.

### The Large-Rapidity Limit

For equal large rapidities the angle tends to the angle between the directions:

$$
\theta_{\mathrm{wgn}}\longrightarrow\theta\qquad(\theta_{\mathrm{rpd},1}=\theta_{\mathrm{rpd},2}\to\infty).
$$

This is exact in the limit and approached quickly: at $\theta_{\mathrm{rpd},1}=\theta_{\mathrm{rpd},2}=10$ the computed angle is $1.570615$ against $\pi/2=1.570796$, and at rapidity $50$ the ratio $\theta_{\mathrm{wgn}}/\theta$ is one to sixty digits. So the rotation saturates at the geometric angle and cannot exceed $\pi$, which it cannot anyway because it is an angle.

The two limits do not commute. If one rapidity is held small while the other grows, the angle tends to the small rapidity itself times a geometric factor, not to $\theta$: with $\theta_{\mathrm{rpd},1}=50$, $\theta_{\mathrm{rpd},2}=0.1$, $\theta=\pi/2$, the computed angle is $0.09983$. So "the large-rapidity limit" is a statement about both rapidities growing together, and a reader who takes one limit at a time gets a different answer.

### Why the Order Matters

Exchanging the two boosts does not give the inverse rotation; it gives a rotation about the same axis with a different angle, because the composition law is not symmetric. So "the Thomas–Wigner rotation of $B_1$ followed by $B_2$" and "of $B_2$ followed by $B_1$" are different rotations, and a formula that treats the pair as unordered is wrong. The asymmetry is visible in the product formula: the imaginary vector part weights the two directions by $\sinh a_1\cosh a_2$ and $\cosh a_1\sinh a_2$, and swapping the labels swaps the weights.

## Summary

The bracket table has three blocks; the third, $[K_a,K_b]=-\epsilon_{abc}J_c$, is the statement that two boosts compose to a boost times a rotation. The table follows from the single identity $[\vec a,\vec b]=2\vec a\times\vec b$ plus the factor $i$ in the boost generators. The product of two boosts has a real scalar part, an imaginary vector part that is the new boost direction, and a real vector part proportional to $\vec u_1\times\vec u_2$ that is the rotation. That rotation is the Thomas–Wigner rotation; its axis is along $\vec u_1\times\vec u_2$, its exact angle is fixed by $\tan\frac{\theta_{\mathrm{wgn}}}{2}=\lvert\vec v\rvert/S$ with $\vec v$ the product's real vector part and $S$ its scalar part, and to leading order $\theta_{\mathrm{wgn}}=\tfrac12\theta_{\mathrm{rpd},1}\theta_{\mathrm{rpd},2}\sin\theta$. Boosts fail to add because the bracket of two boost generators is a rotation, and the failure is not small.

## Summary of Notation

| symbol | meaning |
|---|---|
| $J_\eta=\tfrac12\vec e_\eta$ | rotation generator |
| $K_\eta=\tfrac12 i\vec e_\eta$ | boost generator |
| $\epsilon_{abc}$ | the alternating symbol |
| $a_i=\tfrac12\theta_{\mathrm{rpd},i}$ | half-rapidity of the $i$-th boost |
| $\vec u_i$, $\theta$ | boost direction and angle between the two directions |
| $\theta_{\mathrm{wgn}}$ | the Thomas–Wigner rotation angle |
| $S$, $\vec v$, $\vec w$ | scalar, real vector and imaginary vector parts of the product |
| $\theta_{\mathrm{rpd},12}$ | rapidity of the product |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley, 1999, §11.7 — the Thomas precession derived from the composition of Lorentz transformations, with the sign convention of the rotation made explicit.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.4 and §5.5 — the Wigner rotation in the representation theory of the Lorentz group.
- L. H. Thomas, "The motion of the spinning electron", *Nature* 117 (1926) 514 — the original observation that the composition of boosts is not a boost.
- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the rotation that appears when a boost is followed by another.
- *The Six Generators and Their Commutators* — the table's derivation and signs.
- *When the Axes Commute: The Normal Transformations* — the exact vanishing condition.
