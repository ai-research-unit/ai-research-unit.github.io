# __The Matrix Model: What It Sees and What It Hides__

## Introduction

The $2\times2$ matrix model is the working instrument of this block. Every numerical claim in it is checked there, every determinant is read there, and the two walls of the algebra are easiest to see there. But the instrument has a fixed field of view, and the first task of this article is to draw its boundary before any physics is read through it.

The boundary is drawn in one paragraph and it decides everything after it. The determinant of the image is the algebra's own complex quadratic form, $N=Q_t^{2}+B^{2}$, and it is **not** the Minkowski interval. The interval is what the same determinant becomes on a particular real slice of the algebra, where the image is Hermitian and the determinant reads $q_t^{2}-\lvert\vec q\rvert^{2}$.

This article states that convention box first, proves it, and then asks two questions of the model. What does it see? It sees the trace, the determinant, the singular values and the spectrum, and those four read off the time, the modulus, the two scales and the two weights. What does it hide? It hides the separation of the scale from the central phase, because both are one modulus, and it hides the interior of each wall, because each wall collapses to one condition on the image.

The article assumes *The Isomorphisms and Their Dimensions* for the map $\mathsf{M}_2$ and *Norm and Pairing Conventions* for the norm $N$ and the modulus $\Rho$. It leans on *The Lorentz Transformation as a Biquaternionic Rotation* for the physical meaning of the boost, and on *Paravectors and the Geometry of Spacetime* for the Hermitian slice.

## The Convention Box

### The Map

The isomorphism is fixed in *The Isomorphisms and Their Dimensions*:

$$
\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z & -iQ_x-Q_y\\
-iQ_x+Q_y & Q_t+iQ_z
\end{pmatrix},
\qquad \tilde Q=Q_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\quad Q_\mu\in\mathbb{C}.
$$

Two readings of this array must be distinguished from the start. The **entries** are complex numbers determined by the four coefficients. The **element** is a biquaternion. The map relates them, and no statement about one is a statement about the other until it is translated.

### The Determinant Is the Complex Form

$$
\det\mathsf{M}_2(\tilde Q)=(Q_t-iQ_z)(Q_t+iQ_z)-(-iQ_x-Q_y)(-iQ_x+Q_y)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=N(\tilde Q).
$$

With the notation of *Norm and Pairing Conventions* for the vector part,

$$
B^{2}:=Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad N(\tilde Q)=Q_t^{2}+B^{2}.
$$

The form $N$ is complex. It is the algebra's quadratic form, it is multiplicative, $N(\tilde Q\tilde P)=N(\tilde Q)N(\tilde P)$, and it vanishes exactly on the zero divisors.

### The Interval Is a Different Function

The Minkowski interval is not $N$. It is what $N$ becomes when the four-vector's real coordinates are put into the algebra in the way *Frame and Metric Conventions* fixes:

$$
\text{the four-vector }(q_t,\vec q)\ \longmapsto\ \tilde Q=q_t+\sum_{\eta}iq_\eta\vec e_\eta,
\qquad q_t,q_\eta\in\mathbb{R}.
$$

On that set the coefficients are $Q_t=q_t$ real and $Q_j=iq_j$ imaginary, and the image is

$$
\mathsf{M}_2(\tilde Q)=q_tI_2+q_x\sigma_x+q_y\sigma_y+q_z\sigma_z
=
\begin{pmatrix}
q_t+q_z & q_x-iq_y\\
q_x+iq_y & q_t-q_z
\end{pmatrix},
$$

which is Hermitian. Its determinant is

$$
\det\mathsf{M}_2(\tilde Q)=q_t^{2}-\lvert\vec q\rvert^{2},
$$

the Minkowski interval, and $N$ takes the same value there because $B^{2}=(iq_x)^{2}+(iq_y)^{2}+(iq_z)^{2}=-\lvert\vec q\rvert^{2}$.

The two facts together are worth a display of their own, because they are the whole convention box:

$$
\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)\ \text{for every }\tilde Q,
\qquad
\det\mathsf{M}_2(\tilde Q)=q_t^{2}-\lvert\vec q\rvert^{2}\ \text{on the Hermitian slice}.
$$

### Why the Two Must Not Be Confused

The confusion is not pedantic, because the two forms disagree in sign on a large set and disagree in kind on all of it.

Take $\tilde Q=e_t+\vec e_x$. Then $N=1+1=2$, while the four-vector that has these coefficients is not on the Hermitian slice at all, and the nearest four-vector, $q_t=1$, $q_x=-i$ times $i$, is not real. The element is not a displacement.

Take $\tilde Q=e_t+i\vec e_x$, which *is* the image of the four-vector $(1,1,0,0)$. Then $N=1-1=0$ and $\det\mathsf{M}_2=0$; the four-vector is null; both stories agree, and this is the case where a reader who confuses the two forms gets the right answer for the wrong reason.

Take $\tilde Q=2e_t+i\vec e_x$. Then $N=4-1=3$ and the interval is $3$: here they agree again, because the slice is Hermitian and the coefficients are real and imaginary in the fixed pattern. The disagreement appears the moment a coefficient breaks the pattern: $\tilde Q=2e_t+\vec e_x$ has $N=5$ and no interval at all.

**The rule.** Every sentence of this block that says "the determinant is the interval" means the determinant on the Hermitian slice. Every sentence that says "$N$" means the complex form. A computation that mixes them will produce a positive-definite metric where the physics has a Lorentzian one.

### The Verification

The claims of this section are checked numerically on the slice. On a hundred random real four-vectors, the image is Hermitian to $10^{-15}$, the determinant equals $N$, and the determinant equals $q_t^{2}-\lvert\vec q\rvert^{2}$. Off the slice, on a hundred random complex elements, the determinant equals $N$ and equals neither of the other two expressions in general.

## What the Matrix Sees

### The Trace as Twice the Time

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t .
$$

On the Hermitian slice this is twice the time coordinate. The trace is therefore the one linear datum of the model, and its factor of two is not a normalisation: it comes with $\mathsf{M}_2(e_t)=I_2$ and cannot be divided out without changing the map. On the four-vector representation, which is the congruence action of *The Two Actions of One Group: Adjoint and Congruence*, the corresponding trace is twice the trace here, and a reader comparing the two must keep the factor.

The trace carries the time and nothing else. It is blind to the vector part, and therefore blind to the direction of motion, to the axis of rotation, and to the modulus.

### The Determinant as the Modulus Squared

By *Norm and Pairing Conventions* the modulus $\Rho$ is a chosen square root of $N$, and the unit factor is $\tilde U=\tilde Q/\Rho$. So

$$
\det\mathsf{M}_2(\tilde Q)=\Rho^{2},
$$

and the determinant of the matrix is the square of the modulus. This is the reason the model computes every norm in the series: the determinant is multiplicative, so the modulus of a product is the product of the moduli, and the whole polar machinery of *The Complete Polar Decomposition on the N-Regular Sector* runs on one determinant.

### The Singular Values as the Two Scales

The singular values of $\mathsf{M}_2(\tilde Q)$ are the square roots of the eigenvalues of $\mathsf{M}_2\mathsf{M}_2^{\dagger}$. On the group of invertibles, with $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ a boost of rapidity $\theta_{\mathrm{rpd}}$ times a rotation, the two singular values are

$$
s_{\pm}=e^{\pm\theta_{\mathrm{rpd}}/2},
$$

and in general, with modulus $\Rho$,

$$
s_{\pm}=\Rho\,e^{\pm\theta_{\mathrm{rpd}}/2}.
$$

**The check.** For $\theta_{\mathrm{rpd}}=1.7$ and $\theta_{\mathrm{axr}}=0.9$, the two singular values of the image are $2.33964685$ and $0.42741493$, against $e^{0.85}=2.33964685$ and $e^{-0.85}=0.42741493$. Their product is $1$, the modulus is $1$, and the rotation contributes nothing: singular values are invariant under the unitary factor, so they see the boost and only the boost.

That last sentence is the physical content. The singular values of a frame transformation are its two scales, and the two scales are fixed by the rapidity. A rotation changes the matrix and leaves the two singular values alone.

### The Spectrum

The eigenvalues are

$$
\lambda_{\pm}=Q_t\pm iB,
$$

and they are the subject of *The Two Eigenvalues Are the Two Weyl Weights*. The model does not only display them; it displays the eigenlines, because an eigenvector of $\mathsf{M}_2(\tilde Q)$ is a spinor and the eigenline is a point of the projective line. That is the one place where the matrix model shows more than the four scalar data of $\operatorname{Tr}$ and $\det$.

## The Images of the Two Walls

### The Null Cone

The null cone is $N=0$. Its image is

$$
\{\mathsf{M}_2(\tilde Q):\det\mathsf{M}_2(\tilde Q)=0\},
$$

the singular matrices, which is one complex hypersurface of the four-dimensional space of matrices. The algebra and the matrix agree exactly here: the zero divisors are the singular matrices, and no information is lost in the condition itself. What is lost is everything else — see below.

### The Spectral Wall

The spectral wall is $B^{2}=0$ with $N\neq0$. The discriminant of the characteristic polynomial is

$$
(\operatorname{tr}M)^{2}-4\det M=4Q_t^{2}-4N=-4B^{2},
$$

so the wall's image is the set of matrices with a repeated eigenvalue, and the condition is

$$
(\operatorname{tr}M)^{2}=4\det M,\qquad \det M\neq0 .
$$

On the group of invertibles the repeated eigenvalue is $\pm1$: the wall elements are the unipotent ones, and the model shows them as matrices similar to a Jordan block with eigenvalue $1$ or $-1$. *The Rest Frame and the Exceptional Point* reads that stratum physically, and *The Four Kinds of Frame Transformation* places it among the four kinds.

### One Image Each

So each wall has **one** image, and each image is a single condition on the elementary symmetric functions of the matrix:

| wall | algebraic condition | condition on the image |
|---|---|---|
| null cone | $N=0$ | $\det M=0$ |
| spectral wall | $B^{2}=0$, $N\neq0$ | $(\operatorname{tr}M)^{2}=4\det M$, $\det M\neq0$ |

Two numbers decide which wall an element is on, and they are $\operatorname{tr}M$ and $\det M$. That is the whole of what the model shows about the walls.

## What the Matrix Hides

### The First Hidden Thing: The Interior of Each Wall

The condition says *that* an element is on the wall. It does not say *where*. The null cone is a three-dimensional cone and its image is a three-dimensional hypersurface; the map is injective, so no element is lost, but no scalar reading of the image distinguishes two points of the wall either. A reader who wants to know which null direction an element carries must look at the matrix's null space, and a reader who wants the phase along the wall must look at the entries.

The practical form of the warning: a computation that classifies a frame transformation by $\operatorname{tr}$ and $\det$ alone classifies it only up to the two walls. Two different frames with the same trace and determinant are indistinguishable to that computation, and *The Spectrum Does Not Determine the Frame* is the sharp statement of how much is lost.

### The Second Hidden Thing: Scale and Phase Are Both a Modulus

The central factor of a biquaternion is written $re^{i\theta_{\mathrm{pha}}}$: a positive real scale and a unit complex phase. In the matrix model it enters only through the determinant,

$$
\det\mathsf{M}_2(\tilde Q)=r^{2}e^{2i\theta_{\mathrm{pha}}},
$$

so the model sees one complex number where the algebra has two real data. The scale and the phase are **both a modulus**, and the matrix cannot separate them.

Two consequences follow, and both are used later.

- The four-factor word $(r,\theta_{\mathrm{pha}},\tilde U_{\mathrm b},\tilde u_{\mathrm r})$ of *A Frame Is a Boost Times a Rotation: The Cartan Word* has seven named data; the determinant sees two of them, $r$ and $\theta_{\mathrm{pha}}$, as one complex number, and therefore sees neither separately.
- Two elements that differ by $r\to-r$ and $\theta_{\mathrm{pha}}\to\theta_{\mathrm{pha}}+\pi$ have the same matrix, because $(-r)e^{i(\theta_{\mathrm{pha}}+\pi)}=re^{i\theta_{\mathrm{pha}}}$. The coordinate description of the group is therefore two-to-one even where the group map is one-to-one, which is the redundancy that the same article proves from the intersection $\mathbb{C}^{\times}\cap SL(2,\mathbb{C})=\{\pm I\}$.

### What the Model Does Show Completely

It would be wrong to end on the losses. The map is an isomorphism of associative algebras, so it shows the multiplication, the inverses, the group, the group of invertibles, the spectrum, the eigenlines and the involutions once those are translated. Nothing about the algebra is lost. What is lost is what a *scalar* reading of the image can recover: the trace and the determinant see two numbers out of the eight real data of an element, and the singular values and the spectrum see four more. The remaining two are the relative angle of the two axes, which no scalar of the matrix can carry, and that is the subject of *The Spectrum Does Not Determine the Frame*.

## Summary

The matrix model's determinant is the algebra's complex form, $\det\mathsf{M}_2(\tilde Q)=N=Q_t^{2}+B^{2}$, and it is not the interval. The interval is the same determinant on the Hermitian slice $Q_t=q_t$ real, $Q_j=iq_j$ real, where the image is Hermitian and the determinant reads $q_t^{2}-\lvert\vec q\rvert^{2}$. The trace is twice the time. The determinant is the modulus squared. The singular values are the two scales $re^{\pm\theta_{\mathrm{rpd}}/2}$, and they see the boost and not the rotation. Each of the two walls has one image, given by one condition on $\operatorname{tr}M$ and $\det M$, and the interior of each wall is invisible to any scalar reading. The scale and the phase are both a modulus, so the matrix cannot separate them, and the coordinate description of the group is two-to-one for that reason.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_2(\tilde Q)$ | the $2\times2$ image of the element |
| $N(\tilde Q)=Q_t^{2}+B^{2}$ | the complex quadratic form, equal to $\det\mathsf{M}_2$ |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the squared modulus of the vector part |
| $\Rho$ | a chosen square root of $N$, the modulus |
| $q_t,\vec q$ | real four-vector coordinates, on the Hermitian slice |
| $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ | angle and axis of the rotation |
| $r$, $\theta_{\mathrm{pha}}$ | scale and central phase |
| $s_{\pm}$ | the two singular values |

## Further Reading

- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012 — singular values, the determinant and trace as elementary symmetric functions, and the discriminant of the characteristic polynomial.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — the $2\times2$ matrix representation of the biquaternions and its relation to the Minkowski form.
- *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation* — the map printed here and the Hermitian slice in the corpus's own notation.
- *Norm and Pairing Conventions* — the norm $N$, the modulus $\Rho$ and the vector part $B$.
- *Frame and Metric Conventions* — the assignment of a real four-vector to an element, which is what makes the Hermitian slice the physical one.
- *The Isomorphisms and Their Dimensions*, *The Two Eigenvalues Are the Two Weyl Weights*, *The Spectrum Does Not Determine the Frame* — the articles that use this model and the ones that state its limits.
