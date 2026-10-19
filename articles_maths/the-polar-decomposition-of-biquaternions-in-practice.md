# __The Polar Decomposition of Biquaternions in Practice__

## Introduction

**The polar decomposition of biquaternions** is the procedure that produces the four factors of the polar word. In the matrix picture it is the polar decomposition of $\mathrm{GL}(2,\mathbb{C})$, and it restricts to $\mathrm{SL}(2,\mathbb{C})$ on the unit-norm elements: $\tilde U_{\mathrm b}$ is the positive definite Hermitian factor of $\mathsf{M}_2(\tilde{Q})$, $\exp(i\alpha)\tilde u_{\mathrm r}$ its unitary factor, and the scale and the phase are the split of the complex modulus $\rho = r\exp(i\alpha)$ off the two (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The name of the article is the name of that matrix procedure.

The reference article of the series, *The Polar Element Representation of Biquaternions*, proves the representation $\tilde{Q} = r\,\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and fixes its uniqueness; the present article does not restate it.

**The approach.** The article records the procedure. It gives the two numbers that are read off the element and that fix three of the four factors' data, the five steps in the order in which they are forced, each factor as a closed expression in the four complex coordinates, the exponent of each factor with its position in the algebra, and three worked examples: one element given by its coordinates, one element already in polar form, and one element built from its four factors and decomposed back.

**Conventions.** The symbols and the conventions are those of the corpus and of the reference article (*Conventions in Mathematics*; *The Polar Element Representation of Biquaternions*). The subspaces $\mathbb{M}_+$, $\mathbb{M}_-$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{C}_{\mathbb{B}}$ are those of *Introduction to the Remarkable Subspaces*.

No physics is invoked. Every numerical value displayed below was recomputed in double precision.

## The Two Invariants

### The Norm and the Euclidean Square

Two numbers are read off the four complex coordinates $Q_t,Q_x,Q_y,Q_z$, and the whole procedure turns on them:

$$
N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}\in\mathbb{C} , \qquad E^{2} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2}\in\mathbb{R} .
$$

The first is the biquaternion norm of the polar series; the second is the Hermitian form whose square root is the Euclidean norm $\lVert\tilde{Q}\rVert_{E}$. The two are two of the four forms of the algebra (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*). The first is complex and central, the second is a sum of non-negative terms and is therefore real and non-negative. They are tied by

$$
E^{2}\ \ge\ \lvert N\rvert ,
$$

with equality exactly when the vector part of $\tilde{Q}\tilde{Q}^{*}$ vanishes, that is, when the boost is trivial: the inequality is Cauchy–Schwarz on the complex vector $(Q_t,Q_x,Q_y,Q_z)$.

**Comment.** The inequality is what makes the square roots of the procedure harmless. It gives $E^{2}+\lvert N\rvert > 0$ for every element of the domain, so no denominator below can vanish; it gives $\cosh\psi = E^{2}/\lvert N\rvert \ge 1$, so the rapidity read off the element is a real number; and it gives $\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} \ge 0$, so the boost axis is defined whenever the vector part is nonzero; the equality case is the trivial boost, where the axis is undefined, and it is the only degenerate case that the two numbers can detect.

### The Hermitian Product and Its Vector Part

The vector part of the Hermitian product is the only quantity of the procedure that needs the phases of the coordinates against one another,

$$
\tilde{Q}\tilde{Q}^{*} = E^{2}\,e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) , \qquad \lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} , \qquad
W_k = \operatorname{Im}\Bigl[\overline{Q_t}\,Q_k - Q_t\,\overline{Q_k} - (\vec Q\times\overline{\vec Q})_k\Bigr] , \quad k = 1,2,3 .
$$

Every bracket is purely imaginary, so each $W_k$ is real. The scalar part of the Hermitian product is the Euclidean square, the norm of the Hermitian product is $\lvert N\rvert^{2}$, and the last identity is the multiplicativity of the norm read on that product.

**Comment.** The three sources of the vector part are the phase of $Q_t$ against the phases of the vector coordinates, in the first two terms of the bracket, and the phases of the vector coordinates against one another, in the cross product. The boost axis is $\vec u_{\mathrm b} = \mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert$, so this is where the direction of the boost is decided.

### What the Two Invariants Fix and What They Cannot

The pair $(N,E^{2})$ fixes the scale, the phase and the rapidity. The norm $\langle\cdot\rangle_{\natural}$ gives the modulus, hence the scale $r = \lvert N\rvert^{1/2}$ and the phase $\alpha = \tfrac12\arg N$; the ratio $E^{2}/\lvert N\rvert$ gives the rapidity through $\cosh\psi = E^{2}/\lvert N\rvert$.

The pair cannot give the two directions. Conjugating by a real unit quaternion $R$, so that $\vec Q\mapsto R\vec Q R^{-1}$ and $Q_t$ is unchanged, leaves both $\langle\cdot\rangle_{\natural}$ and $E^{2}$ unchanged, since a real rotation preserves $\sum_kQ_k^{2}$ and $\sum_k\lvert Q_k\rvert^{2}$, and carries $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ to $R\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})R^{-1}$, so the axis turns while the pair stands still. Over $100$ random elements and random rotations the pair was invariant to $1.1\times10^{-14}$, the vector part reproduced the rotated vector to $4.4\times10^{-15}$, and the axis itself moved by more than $0.3$ in $99$ of the $100$ draws.

The count is the same statement. The four complex coordinates carry eight real numbers. The pair $(N,E^{2})$ accounts for three of them, the scale, the phase and the rapidity, and the remaining five are the two numbers of the boost axis, the two numbers of the rotor axis, and the rotation angle. The two axes come from the phases of the coordinates, through $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ and through the real parts of $Q_\mu \exp(-i\alpha)$.

## The Procedure

### The Five Steps

Given $\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$:

1. Compute the biquaternion norm $N = \sum_\mu Q_\mu^2 \in \mathbb{C}$.
2. Take its principal square root: write $N = |N|\exp(i\varphi)$ with $\varphi\in(-\pi,\pi]$, and put $\rho = \sqrt{|N|}\exp(i\varphi/2)$, so that $r = \sqrt{|N|}$ and $\alpha = \varphi/2$.
3. Put $U = \tilde{Q}/\rho$, of unit norm.
4. Compute the Hermitian element $UU^{*}$, and write it as $\mathrm{Sc}(UU^{*}) e_t + i\mathrm{Vec}(UU^{*})$ with $\mathrm{Sc}(UU^{*})\in\mathbb{R}$, $\mathrm{Vec}(UU^{*})\in\mathbb{R}^3$; then put
   $\tilde U_{\mathrm b} = \sqrt{\frac{1+\mathrm{Sc}(UU^{*})}{2}}\,e_t + \frac{i\mathrm{Vec}(UU^{*})}{\sqrt{2(1+\mathrm{Sc}(UU^{*}))}}$, and read the rapidity and axis off by $\cosh\psi = \mathrm{Sc}(UU^{*})$, $\vec u_{\mathrm b} = \mathrm{Vec}(UU^{*})/|\mathrm{Vec}(UU^{*})|$; when $\mathrm{Vec}(UU^{*})=0$ the boost is $\tilde U_{\mathrm b}=e_t$ and no axis is read.
5. Put $\tilde u_{\mathrm r} = U(\sqrt{U^{*}U})^{-1} = \tilde U_{\mathrm b}^{\natural}U$, the unitary factor of the right polar decomposition of $U$, and verify that its coefficients are real and that $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$.

The factors so obtained satisfy $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ identically.

**Comment on step 1.** Step 1 is a test before it is a computation. If $N = 0$ the element is zero or a zero divisor, no factor of the word exists, and the procedure stops. The domain of the representation is the complement of the null cone, and the test is the first thing to perform.

**Comment on step 2.** Step 2 is the only step that requires a convention, and it carries the whole of it: the branch of the square root is fixed once and for all by $\alpha\in(-\pi/2,\pi/2]$, the closed right half plane. The other root $-\rho$ has angle $\alpha\pm\pi$ and is outside the interval. Every other step is forced.

**Comment on step 3.** Step 3 is a division by a complex number, that is, a multiplication by its inverse, and it costs nothing: $1/\rho = \exp(-i\alpha)/r$. Its only role is to put the element on the unit-norm sphere, so that the remaining content of the decomposition is the split of a unit element into a boost and a rotor.

**Comment on step 4.** Step 4 is the only step that is not rational in the coordinates: it needs the positive square root of the Hermitian element $UU^{*}$, and the closed form above is that square root written in the algebra. The element $UU^{*}$ is Hermitian and positive definite, of unit norm, hence $\mathrm{Sc}(UU^{*})^{2}-\lvert\mathrm{Vec}(UU^{*})\rvert^{2} = 1$ and $\mathrm{Sc}(UU^{*})\ge1$, and the two Hermitian square roots of $UU^{*}$ are $\pm\tilde U_{\mathrm b}$; the positive one is taken. The rapidity and the axis are read off the two data of $UU^{*}$: $\cosh\psi = \mathrm{Sc}(UU^{*})$ and, when $\mathrm{Vec}(UU^{*})\neq0$, $\vec u_{\mathrm b} = \mathrm{Vec}(UU^{*})/\lvert\mathrm{Vec}(UU^{*})\rvert$; when the vector part vanishes the boost is $e_t$ and the axis is undefined.

**Comment on step 5.** Step 5 is a subtraction in disguise, and it needs no square root. The rotor is what is left of the unit element after the Hermitian positive part is divided out, and it is real because the division cancels the Hermitian part exactly: $U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$, and the rotor has as many real parameters as the boost has imaginary coefficients.

### What to Do First

The procedure opens with a test and not with a computation: form the biquaternion norm $\langle\cdot\rangle_{\natural}$. If $N = 0$ the element is zero or a zero divisor, no factor of the word exists, and the whole of the above is empty; the domain of the representation is the complement of the null cone, which is the first thing to establish. If $N\neq0$ the order is forced and has no freedom left: the modulus $\rho$ comes first, because it is the only step that needs the branch choice; the normalised element $U$ comes second, because every later step divides by $\rho$ or by a function of it; the Hermitian element $UU^{*}$ comes third, because the boost is its root; and the rotor comes last, as the unitary factor of the right polar decomposition of $U$. No step can be moved, and no step needs a second convention.

### Each Factor in a Sentence

| # | factor | what it is | where it lies |
|---|---|---|---|
| 1 | $r$ | the positive real absolute value of the modulus, central and non-compact | the positive real line, in the centre |
| 2 | $\exp(i\alpha)$ | the central phase, the only compact central factor | the unit circle of the centre |
| 3 | $\tilde U_{\mathrm b}$ | the Hermitian positive unit element, the Lorentz boost | $\mathbb{M}_+$ |
| 4 | $\tilde u_{\mathrm r}$ | the unit real quaternion, the spatial rotation | $\mathbb{H}_{\mathbb{B}}$ |

The dimensions are $1+1+3+3 = 8$, which is the real dimension of the algebra: the decomposition is a change of coordinates on the complement of the null cone, with as many real parameters as the ambient algebra has, and the same count as the real dimension of $\mathrm{GL}(2,\mathbb{C})$ in the matrix picture.

### The Factors in the Coordinates of $\tilde{Q}$

The five steps are formulas, and each factor is a closed expression in the four complex coordinates $Q_t,Q_x,Q_y,Q_z$. The expressions use **two numbers read off the coordinates**: the biquaternion norm $\langle\cdot\rangle_{\natural}$ and the Euclidean square $E^{2}$ of §*The Two Invariants*.

| factor | in the coordinates of $\tilde{Q}$, the norm $\langle\cdot\rangle_{\natural}$ and the Euclidean square $E^{2}$ |
|---|---|
| modulus | $\rho = \sqrt{N} = r\,\exp(i\alpha)$, the principal square root |
| scale | $r = \lvert N\rvert^{1/2}$ |
| phase | $\alpha = \tfrac12\arg N$, with $\arg N \in (-\pi,\pi]$, so $\alpha \in \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ |
| normalised element | $U_\mu = \dfrac{Q_\mu}{\rho} = \dfrac{Q_\mu\,\exp(-i\alpha)}{r}$ |
| boost, scalar part | $\cosh\dfrac{\psi}{2} = \sqrt{\dfrac{E^{2}+\lvert N\rvert}{2\,\lvert N\rvert}}$ |
| boost, vector part | $\sinh\dfrac{\psi}{2}\,\vec u_{\mathrm b} = \dfrac{\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})}{\sqrt{2\,\lvert N\rvert\,(E^{2}+\lvert N\rvert)}}$ |
| rapidity | $\cosh\psi = \dfrac{E^{2}}{\lvert N\rvert}$, and the speed $\tanh\dfrac{\psi}{2} = \sqrt{\dfrac{E^{2}-\lvert N\rvert}{E^{2}+\lvert N\rvert}}$ |
| rotor | $\tilde u_{\mathrm r,\mu} = \sqrt{\dfrac{2}{E^{2}+\lvert N\rvert}}\;\operatorname{Re}\!\bigl(Q_\mu\,\exp(-i\alpha)\bigr)$, $\mu\in\{t,x,y,z\}$ |

The vector part of the boost is read off the Hermitian product $\tilde{Q}\tilde{Q}^{*}$, which is the quantity $r^{2}UU^{*}$ of step 4,

$$
\tilde{Q}\tilde{Q}^{*} = E^{2}\,e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) , \qquad
\tilde{U}_{\mathrm b} = \sqrt{\frac{E^{2}+\lvert N\rvert}{2\,\lvert N\rvert}}\;e_t + \frac{i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})}{\sqrt{2\,\lvert N\rvert\,(E^{2}+\lvert N\rvert)}} , \qquad
\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} .
$$

The rapidity datum $\mathrm{Sc}(UU^{*})$ of §*The Closed Form* under §*The Boost* of the companion article is the ratio $\mathrm{Sc}(UU^{*}) = E^{2}/\lvert N\rvert$, and the boost datum $\mathrm{Vec}(UU^{*})$ of that section is $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert N\rvert$.

**Comment.** The table is the algorithm in one glance: two rows are read off $\langle\cdot\rangle_{\natural}$ alone, the two boost rows are read off $E^{2}$ against $\lvert N\rvert$ and off $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$, and the last row is the projection of the coordinates on the phase direction. Every entry is a closed expression, so no iteration, no search and no series occurs anywhere in the procedure except in the one square root of $\rho$ that step 2 fixes by convention.

**Check on the first example below.** For $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$ the pair is $N = 5+2i$ and $E^{2} = 7$, so the table gives $\lvert N\rvert = \sqrt{29} = 5.385164807$, $r = 2.320595787$, $\alpha = 0.190253189$, $\mathrm{Sc}(UU^{*}) = E^{2}/\lvert N\rvert = 1.299867367$, speed $\sqrt{(7-\sqrt{29})/(7+\sqrt{29})} = 0.361088126$ and boost scalar $\sqrt{(7+\sqrt{29})/(2\sqrt{29})} = 1.072349609$, all of them the values computed step by step; the Hermitian product is $\tilde{Q}\tilde{Q}^{*} = 7\,e_t - 2i\,\vec e_x - 4i\,\vec e_y$, of vector part $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) = (-2,-4,0)$, and the rotor coefficients $\sqrt{2/(7+\sqrt{29})}\,\operatorname{Re}(Q_\mu \exp(-i\alpha))$ are $0.470592172$, $0.394599292$, $0.789198585$ and $0$.

## The Exponents of the Factors

### The Table of the Exponents

Each of the four factors is the exponential of a single element of the algebra, and the exponent of each is a real parameter times a root of $-e_t$, $0$ or $+e_t$: the generator of a one-parameter group (*Conventions in Mathematics*, §*The Root Convention*). The four rows restate the table of §*The Polar Word* of *The Polar Element Representation of Biquaternions*; the comment on each row, the character table and the half-angle dictionary below are what this article adds to it.

| factor | exponent | where the exponent lies |
|---|---|---|
| $r$ | $\ln r$ | the real line $\mathbb{R}e_t$ |
| $\exp(i\alpha)$ | $i\alpha$ | the imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$ |
| $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, traceless |
| $\tilde u_{\mathrm r}$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions |

**Comment on the scale.** Its exponent, $\ln r$, is real, and it is the only exponent whose root is the algebra unit $e_t$ itself. It lives on the real line, the non-compact positive direction of the algebra, and it is the only exponent that has no direction attached to it: the whole of the one-parameter group is the line. The factor is positive by construction, since the modulus carries the branch.

**Comment on the phase.** Its exponent lies in the centre, on the central imaginary line. It is therefore the only exponent that commutes with the other three, which is why the phase may be written anywhere in the word without changing it, and why the word is unambiguous as soon as the relative order of the two non-central factors is fixed. Its root is the central $i$, of square $-e_t$.

**Comment on the boost.** Its exponent lies in the Hermitian subspace $\mathbb{M}_+$ and is traceless: the scalar part of the exponent vanishes, so the exponent is exactly the three real numbers of $i(\psi/2)\vec u_{\mathrm b}$, and the trace in the matrix picture is twice that vanishing scalar part. Its root $i\vec u_{\mathrm b}$ squares to $+e_t$, and among the roots that are not the unit $e_t$ it is the only one that does. The parameter $\psi$ runs over $[0,\infty)$ and the axis over the axis sphere $\mathcal{A}$.

**Comment on the rotor.** Its exponent lies in $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions, which is the real vector block $\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ of the block decomposition of the subspaces. Its root $\vec u_{\mathrm r}$ is a unit vector, of square $-e_t$, and the parameter is the rotation angle $\theta$ read modulo $2\pi$. Its one-parameter group is compact, the circle of the real plane spanned by $e_t$ and $\vec u_{\mathrm r}$, and the central phase is the only other exponent for which this happens.

**Comment on the pair of non-central exponents.** The two central exponents commute with everything and with each other; the two non-central exponents do not commute unless the two axes coincide or one of the factors is trivial. The example below witnesses the size: for the element built there, $\tilde U_{\mathrm b}\tilde u_{\mathrm r} - \tilde u_{\mathrm r}\tilde U_{\mathrm b} = 0.72\,i\,\vec e_x - 0.54\,i\,\vec e_y$ with perpendicular axes, and the two exponentials cannot be fused. This is why the table has four rows and not three, and why the order of the last two rows is part of the word.

### The Character of the Exponential

The character of each exponential is fixed by the square of its root, and the rule is the same in every algebra of the polar series:

| factor | exponent | root | square of the root | character |
|---|---|---|---|---|
| $r$ | $\ln r$ | $e_t$ | $+e_t$ | hyperbolic, degenerate |
| $\exp(i\alpha)$ | $i\alpha$ | $i$ | $-e_t$ | trigonometric |
| $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $+e_t$ | hyperbolic |
| $\tilde u_{\mathrm r}$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $-e_t$ | trigonometric |

The closed forms follow from the character: the trigonometric row gives the unit circle in the plane of its root, $\exp(\theta\vec u/2) = \cos(\theta/2)e_t + \sin(\theta/2)\vec u$, and the hyperbolic row gives the hyperbola in the plane of its root, $\exp(i\psi\vec u/2) = \cosh(\psi/2)e_t + i\sinh(\psi/2)\vec u$. The parabolic case, a nilpotent root, truncates the series to $e_t$ plus the exponent and produces no factor of this representation.

### The Two Half-Angles

The exponents of the two non-central factors carry **half** of the parameter of the transformation they produce. The boost exponent is $i(\psi/2)\vec u_{\mathrm b}$ with $\psi$ the rapidity, and the conjugation by the boost produces a Lorentz transformation of rapidity $\psi$; the rotor exponent is $(\theta/2)\vec u_{\mathrm r}$ with $\theta$ the rotation angle, and the conjugation by the rotor produces a rotation by $\theta$. The doubling is the double cover of the two groups, and it is why the parameters of §*The Two Invariants* come back with a factor two: the dictionary of the half-angles is

$$
\cosh\frac{\psi}{2} = \sqrt{\frac{1+\mathrm{Sc}(UU^{*})}{2}} , \qquad \sinh\frac{\psi}{2} = \frac{\lvert\mathrm{Vec}(UU^{*})\rvert}{\sqrt{2(1+\mathrm{Sc}(UU^{*}))}} , \qquad \cos\frac{\theta}{2} = u_{\mathrm r,0} , \qquad \sin\frac{\theta}{2} = \lvert\mathrm{Vec}(\tilde u_{\mathrm r})\rvert ,
$$

with $\mathrm{Sc}(UU^{*}) = E^{2}/\lvert N\rvert$ and $\mathrm{Vec}(UU^{*}) = \mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert N\rvert$ the data of $UU^{*}$. The last two are read off the rotor itself: the scalar coefficient of a unit real quaternion is the cosine of the half-angle, and the length of its vector part the sine.

## Worked Example: an Element Given by Its Coordinates

Take

$$
\tilde{Q} = (1+i)e_t + \vec e_x + 2\vec e_y ,
$$

whose coefficients are $Q_t = 1+i$, $Q_x = 1$, $Q_y = 2$, $Q_z = 0$.

*Step 1.* The biquaternion norm is $N = (1+i)^2+1^2+2^2+0 = 2i+5 = 5+2i$, of modulus $|N| = \sqrt{29} = 5.385164807$ and argument $\arg N = 0.380506377$ rad.

*Step 2.* The modulus is $\rho = \sqrt{5.385164807}\,\exp(0.190253189\,i) = 2.278723854 + 0.438842117 i$, hence

$$
r = 2.320595787 , \qquad \alpha = 0.190253189\ \text{rad} \approx 10.9007^\circ .
$$

*Step 3.* Dividing, $U = \tilde{Q}/\rho$ has coefficients

$$
U_t = 0.504639332+0.341657461i, \quad U_x = 0.423148397-0.081490935i, \quad U_y = 0.846296793-0.162981871i, \quad U_z = 0 ,
$$

and $\langle U,U\rangle_{\natural} = 1$ as required.

*Step 4.* The Hermitian element $UU^{*}$ is

$$
UU^{*} = 1.299867367\,e_t - 0.371390676\,i\,\vec e_x - 0.742781353\,i\,\vec e_y ,
$$

so $\mathrm{Sc}(UU^{*}) = 1.299867367$, $\mathrm{Vec}(UU^{*}) = (-0.371390676, -0.742781353, 0)$ and $|\mathrm{Vec}(UU^{*})| = 0.830454799$; the identity $\mathrm{Sc}(UU^{*})^2-|\mathrm{Vec}(UU^{*})|^2 = 1$ holds to $7\times10^{-16}$. The boost is therefore

$$
\tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y ,
$$

with rapidity $\psi = 2\operatorname{arccosh}(1.072349609) = 0.756273220$, corresponding to the speed $\tanh(\psi/2) = 0.361088126$ in units $c = 1$, and axis $\vec u_{\mathrm b} = -(1,2,0)/\sqrt{5}$. The verification $\tilde U_{\mathrm b}^2 = UU^{*}$ was carried out to $2.2\times10^{-16}$ in the coefficients.

*Step 5.* The rotor is

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U = 0.470592172\,e_t + 0.394599292\,\vec e_x + 0.789198585\,\vec e_y ,
$$

all of whose coefficients are real, with $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$; its rotation angle is $\theta = 2.161669$ rad about the axis $(1,2,0)/\sqrt{5}$.

The reconstruction $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ was verified in double precision and agrees with $\tilde{Q}$ to $1.6\times10^{-16}$ in each coefficient. Note that the boost axis and the rotation axis are opposite in this example, which is a coincidence of the element and not a structural relation: no relation between the two axes is imposed by the decomposition, and a random element generally has them unrelated.

*The four exponents of this example.* The four factors are exponentials, and their exponents to the nine decimals used above are

$$
\ln r = 0.841823957 , \qquad \alpha = 0.190253189 , \qquad \frac{\psi}{2} = 0.378136610 , \qquad \frac{\theta}{2} = 1.080834539 ,
$$

the boost about $\vec u_{\mathrm b} = -(1,2,0)/\sqrt5$ and the rotor about $\vec u_{\mathrm r} = (1,2,0)/\sqrt5$, so that the word is the ordered product of four exponentials

$$
\tilde{Q} = \exp(0.841823957)\,\exp(0.190253189\,i)\,\exp\bigl(i\,0.378136610\,\vec u_{\mathrm b}\bigr)\,\exp\bigl(1.080834539\,\vec u_{\mathrm r}\bigr) .
$$

Rebuilding $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ from the last two exponents reproduces the factors of Steps 4 and 5; the full parameters are the rapidity $\psi = 0.756273220$ and the rotation angle $\theta = 2.161669078$, each twice its stored half.

## Worked Example: an Element Already in the Polar Form

Take the Lorentz boost biquaternion of the physics articles with speed $0.6c$ along $\vec e_x$,

$$
\tilde U = \cosh\frac{\psi}{2}\,e_t + i\sinh\frac{\psi}{2}\,\vec e_x , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

so that $\tilde U = 1.060660172\,e_t + 0.353553391\,i\,\vec e_x$. Its biquaternion norm is $N = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1$, a positive real, so the modulus is $\rho = 1$, the scale is $r = 1$ and the phase is $\alpha = 0$. The remaining construction returns $U = \tilde U$, $UU^{*} = \tilde U^2$, $\tilde U_{\mathrm b} = \tilde U$ and $\tilde u_{\mathrm r} = e_t$, so that the four-factor form collapses to

$$
\tilde U = 1\cdot \exp(i\cdot0)\cdot\tilde U\cdot e_t .
$$

The example is the reason the representation is a strict refinement of the physics convention: a Lorentz rotor is already in polar form, with two of its four factors trivial. In the language of the two invariants, the norm is real positive, so the phase vanishes, and the Hermitian product is already its own square root in the sense of step 4.

## Worked Example: an Element Built from Its Four Factors

The last example runs the procedure in the other direction. The four factors are chosen first, with rational data, the element is multiplied out, and the algorithm is then asked to recover the factors it was given. Take

$$
r\,\exp(i\alpha) = 2+i , \qquad \tilde U_{\mathrm b} = \frac54\,e_t + \frac{9}{20}\,i\,\vec e_x + \frac35\,i\,\vec e_y , \qquad \tilde u_{\mathrm r} = \frac45\,e_t + \frac35\,\vec e_z .
$$

The data are those of the exponentials: $\rho = 2+i$ has $r = \sqrt5 = 2.236067977$ and $\alpha = \operatorname{atan}\tfrac12 = 0.463647609$; the boost has $\cosh\frac{\psi}{2} = \frac54$ and $\sinh\frac{\psi}{2} = \frac34$ about the axis $\vec u_{\mathrm b} = (3,4,0)/5 = (0.6,0.8,0)$, so $\frac{\psi}{2} = \operatorname{arcosh}\frac54 = \ln 2$ and the rapidity is $\psi = 2\ln2 = 1.386294361$; the rotor has $\frac{\theta}{2} = \operatorname{atan}\frac34$, so $\theta = 1.287002218$ about $\vec u_{\mathrm r} = \vec e_z$. Both non-central factors are unit elements, and the two axes are perpendicular, the case in which the two non-central exponents commute least.

Multiplying the factors gives

$$
\tilde{Q} = (2+i)e_t + \left(-\tfrac{18}{25}+\tfrac{36}{25}i\right)\vec e_x + \left(-\tfrac{21}{100}+\tfrac{21}{50}i\right)\vec e_y + \left(\tfrac32+\tfrac34 i\right)\vec e_z ,
$$

that is $Q_t = 2+i$, $Q_x = -0.72+1.44i$, $Q_y = -0.21+0.42i$, $Q_z = 1.5+0.75i$. Now apply the algorithm to this element, forgetting how it was made.

*Step 1.* The norm is

$$
N = (2+i)^2 + \left(-\tfrac{18}{25}+\tfrac{36}{25}i\right)^2 + \left(-\tfrac{21}{100}+\tfrac{21}{50}i\right)^2 + \left(\tfrac32+\tfrac34 i\right)^2 = 3+4i ,
$$

of modulus $\lvert N\rvert = 5$ and argument $\arg N = \operatorname{atan}\tfrac43 = 0.927295218$. The imaginary part is not accidental: it is the phase of the central factor, and it returns in step 2.

*Step 2.* The modulus is $\rho = \sqrt5\,\exp(0.463647609\,i) = 2+i$, exactly the central factor that was used to build the element, since $N = (2+i)^2$. Hence

$$
r = \sqrt5 = 2.236067977 , \qquad \alpha = \operatorname{atan}\tfrac12 = 0.463647609 .
$$

*Step 3.* Dividing, the unit element is

$$
U = \frac{\tilde{Q}}{\rho} = e_t + \frac{18}{25}\,i\,\vec e_x + \frac{21}{100}\,i\,\vec e_y + \frac34\,\vec e_z ,
$$

that is $U_t = 1$, $U_x = 0.72i$, $U_y = 0.21i$, $U_z = 0.75$, and indeed $U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$.

*Step 4.* The Hermitian element is

$$
UU^{*} = \frac{17}{8}\,e_t + \frac98\,i\,\vec e_x + \frac32\,i\,\vec e_y = 2.125\,e_t + 1.125\,i\,\vec e_x + 1.5\,i\,\vec e_y ,
$$

so $\mathrm{Sc}(UU^{*}) = \frac{17}{8} = 2.125$, $\mathrm{Vec}(UU^{*}) = (\frac98,\frac32,0)$ and $\lvert\mathrm{Vec}(UU^{*})\rvert = \frac{15}{8} = 1.875$; the identity $\mathrm{Sc}(UU^{*})^2-\lvert\mathrm{Vec}(UU^{*})\rvert^2 = 1$ is exact, $\frac{289}{64}-\frac{225}{64} = 1$. The boost is

$$
\tilde U_{\mathrm b} = \sqrt{\frac{1+\mathrm{Sc}(UU^{*})}{2}}\,e_t + \frac{i\mathrm{Vec}(UU^{*})}{\sqrt{2(1+\mathrm{Sc}(UU^{*}))}} = \frac54\,e_t + \frac{9}{20}\,i\,\vec e_x + \frac35\,i\,\vec e_y ,
$$

since $\sqrt{(1+\mathrm{Sc}(UU^{*}))/2} = \sqrt{25/16} = \frac54$ and $\lvert\mathrm{Vec}(UU^{*})\rvert/\sqrt{2(1+\mathrm{Sc}(UU^{*}))} = \frac{15}{8}\cdot\frac25 = \frac34$. The rapidity is $\psi = 2\operatorname{arcosh}\frac54 = 2\ln 2 = 1.386294361$, the speed is $\tanh\frac{\psi}{2} = \frac34/\frac54 = 0.6$, and the axis is $\vec u_{\mathrm b} = \mathrm{Vec}(UU^{*})/\lvert\mathrm{Vec}(UU^{*})\rvert = (0.6,0.8,0)$.

*Step 5.* The rotor is

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U = \frac45\,e_t + \frac35\,\vec e_z ,
$$

with real coefficients, of unit norm, and rotation angle $\theta = 2\operatorname{atan}\frac34 = 1.287002218$ about $\vec e_z$.

The procedure has returned the four factors that were used to build the element, with no residue: the boost matches to $0$ in every coefficient and the rotor to $1.7\times10^{-16}$, and the reconstruction $r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ agrees with $\tilde{Q}$ to $5.0\times10^{-16}$ in the largest coefficient.

**Comment on the two orders.** The example shows why the word is ordered. With the two perpendicular axes the two non-central factors do not commute, the two orders differ by

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r} - \tilde u_{\mathrm r}\tilde U_{\mathrm b} = \frac{18}{25}\,i\,\vec e_x - \frac{27}{50}\,i\,\vec e_y ,
$$

of largest coefficient $0.72$, and the two non-central exponents, $X = i\frac{\psi}{2}\vec u_{\mathrm b}$ and $Y = \frac{\theta}{2}\vec u_{\mathrm r}$, have the non-vanishing bracket

$$
[X,Y] = XY-YX = i\,\ln 2\,\operatorname{atan}\tfrac34\left(\tfrac85\,\vec e_x - \tfrac65\,\vec e_y\right) = 0.713665567\,i\,\vec e_x - 0.535249175\,i\,\vec e_y .
$$

The shortcut of replacing the product of the two exponentials by the exponential of their sum fails accordingly: $\lVert\exp(X+Y)-\exp(X)\exp(Y)\rVert = 0.350671030$ in the largest coefficient, while $\exp(X)\exp(Y)$ is $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ to $2.2\times10^{-16}$. The four exponents of this element are

$$
\ln r = 0.804718956 , \qquad \alpha = 0.463647609 , \qquad \frac{\psi}{2} = 0.693147181 , \qquad \frac{\theta}{2} = 0.643501109 ,
$$

and the word is

$$
\tilde{Q} = \exp(0.804718956)\,\exp(0.463647609\,i)\,\exp\bigl(i\,0.693147181\,\vec u_{\mathrm b}\bigr)\,\exp\bigl(0.643501109\,\vec u_{\mathrm r}\bigr) ,
$$

the product now taken in the order in which the four rows of the exponent table stand.

## Summary of Notation

| symbol | set | meaning |
|---|---|---|
| $N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ | $\mathbb{C}$, central | the biquaternion norm, the first invariant |
| $E^{2} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^{2}$ | $\mathbb{R}$, $E^{2}\ge\lvert N\rvert$ | the Euclidean square, the second invariant |
| $\tilde{Q}\tilde{Q}^{*} = E^{2}e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ | $\mathbb{M}_+$ | the Hermitian product, whose vector part carries the boost axis |
| $\rho = \sqrt{N} = r\exp(i\alpha)$ | $\mathbb{C}\setminus\{0\}$ | the complex modulus, the principal square root |
| $r$, $\alpha$ | $\mathbb{R}$, $r>0$; $(-\pi/2,\pi/2]$ | the scale and the phase |
| $U = \tilde{Q}/\rho$ | unit norm | the unit-norm part, $U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| $UU^{*} = \mathrm{Sc}(UU^{*})\,e_t + i\,\mathrm{Vec}(UU^{*})$ | $\mathbb{M}_+$, $\langle UU^{*}\rangle_{\natural}=e_t$ | the Hermitian positive element, $\mathrm{Sc}(UU^{*}) = E^{2}/\lvert N\rvert$, $\mathrm{Vec}(UU^{*}) = \mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert N\rvert$ |
| $\tilde U_{\mathrm b} = \sqrt{UU^{*}}$ | $\mathbb{M}_+$, unit norm | the boost |
| $\tilde u_{\mathrm r} = U(\sqrt{U^{*}U})^{-1} = \tilde U_{\mathrm b}^{\natural}U$ | $\mathrm{Sp}(1)$ | the rotor, the unitary factor of the right polar decomposition |
| $\ln r$, $i\alpha$, $i\frac{\psi}{2}\vec u_{\mathrm b}$, $\frac{\theta}{2}\vec u_{\mathrm r}$ | see the exponent table | the four exponents |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | subspaces | the Hermitian and the anti-Hermitian subspaces |
| $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | subspaces | the vector subspace, the real quaternions, the centre |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the theorem, its existence and uniqueness, the branch of the modulus, the domain, the exponential trichotomy and the published form.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the two invariants $\langle\cdot,\cdot\rangle_{\natural}$ and $E^{2}$, the Hermitian form and the Euclidean norm.
- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the definiteness of the algebraic norm of $\langle\cdot\rangle_{*}$ and the multiplicativity of $\langle\cdot\rangle_{\natural}$, which are the two properties the inequality $E^{2}\ge\lvert N\rvert$ and the identity $\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2}$ rest on.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces in which the four exponents lie.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the coordinate blocks, the incidence of the exponents with the subspaces and the polar data each subspace carries.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the two-factor grouping $\tilde{Q} = HU$ that the matrix picture of the introduction reads.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the determinant, and the matrix polar decomposition that this procedure performs.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation whose trigonometric factor is the rotor and whose hyperbolic factor is the boost about the rotor-conjugated axis, and for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$.
