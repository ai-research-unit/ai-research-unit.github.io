# __The Polar Representation of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the algebra of the Lorentz group, of the four-vector, and of the spinor of the corpus. This article reads the **polar representation**

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} , \qquad r\in\mathbb{R}_{>0}, \quad \alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right], \quad B\in\mathbb{M}_+, \quad \hat{q}\in\mathrm{Sp}(1) ,
$$

from the physics side. The algebra, the existence, the uniqueness and the domain of the representation are proved in the companion article *Biquaternion Polar Representation* of the maths menu; nothing algebraic is reproved here. What this article does is identify each of the four factors with an object that the physics articles of the corpus already use, and show that the Cartan decomposition of the Lorentz group, the determinant of the $2\times2$ and $4\times4$ matrix representations, and the interval of a four-vector are the four factors seen one at a time.

The dictionary is as follows, and each line is established in a section below.

| factor | physics reading |
|---|---|
| $r$ | the scale: the square root of the absolute value of the determinant, equal to the proper length of a four-vector |
| $e^{i\alpha}$ | the central phase: the $U(1)$ of the framework, which realises the $ict$ of the material sector as the angle $\pi/2$ |
| $B$ | the Lorentz boost rotor, in the positive-definite normalisation |
| $\hat{q}$ | the spatial rotation, the subgroup $SU(2)$, and the Thomas–Wigner rotation when two boosts are composed |

Two consequences of the algebraic theorem are physical, and they frame the article. First, a Lorentz rotor of unit norm form has $r = 1$ and $\alpha = 0$, so the representation reduces on the Lorentz group to the Cartan decomposition $\tilde{\Lambda} = \tilde{B}\tilde{R}$, which is therefore a **special case** of the four-factor representation and not a separate theorem. Second, the norm form is the determinant of the $2\times2$ representation, so the modulus of the representation is the square root of a determinant, and the four factors are respectively the absolute value of a determinant, an argument of a determinant, a positive Hermitian matrix, and a unitary matrix. The physics of the representation is the physics of combining four objects under one multiplication, and the algebra of the representation is the matrix polar decomposition of $GL(2,\mathbb{C})$.

The conventions are those of *Conventions in the Biquaternion Universe* as used by *The Four-Vector Representation of Biquaternions*, *The 2×2 Matrix Representation of Biquaternions* and *The 4×4 Regular Matrix Representation of Biquaternions*: the scalar imaginary is $i$, central; the units satisfy $e_k^2 = -e_0$ and $e_1e_2 = e_3$; the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$; $\mathbb{H}_{\mathbb{B}}$, the fixed space of complex conjugation, is the real quaternion subspace, the home of the rotations, meeting the informational sector in $\mathbb{R}e_0$ and the material sector in the pure-vector space; the informational sector $\mathbb{M}_+$ is the Hermitian subspace, the home of the boosts; and the material sector $\mathbb{M}_-$ is the anti-fixed space of quaternion conjugation, with $Q_0 = iq'_0$ and $Q_k = q_k$ real, the home of the four-vectors, with the interval $N = -c^2t^2+\mathbf{x}^2$. Every numerical value below was recomputed in double precision.

## The Scale and the Determinant

### The Modulus Is a Determinant

In the $2\times2$ matrix representation the norm form is the determinant,

$$
\det\Phi(\tilde{Q}) = N(\tilde{Q}) = \sum_\mu Q_\mu^2 ,
$$

and in the $4\times4$ regular representation the determinant is its square and the trace is four times the scalar part,

$$
\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2 , \qquad \operatorname{Tr}\rho_L(\tilde{Q}) = 4Q_0 .
$$

The modulus of the polar representation is $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$, so the scale and the phase are the polar form of the determinant:

$$
r = \left|\det\Phi(\tilde{Q})\right|^{1/2}, \qquad \alpha = \tfrac12\arg\det\Phi(\tilde{Q}) .
$$

Every statement about the modulus is therefore a statement about the determinant of the matrix representative, and the failure of the representation at $N(\tilde{Q}) = 0$ is the failure of the matrix representative to be invertible. In the four-vector reading, $N(\tilde{Q}) = 0$ is the light cone: the polar representation of a biquaternion is available exactly on the nonzero elements off the light cone.

### The Unit-Norm Slice Is the Lorentz Group

For a Lorentz rotor $\tilde{\Lambda}$ the norm form is the unit, $N(\tilde{\Lambda}) = e_0$, so $r = 1$ and $\alpha = 0$ and the representation collapses to two factors,

$$
\tilde{\Lambda} = B\,\hat{q} , \qquad B\in\mathbb{M}_+,\quad \hat{q}\in\mathrm{Sp}(1) .
$$

This is the **Cartan decomposition** of the Lorentz group as the companion article *The Lorentz Group in Biquaternionic Form* states it: every unit-norm biquaternion is a boost times a spatial rotation, unique when the boost is required to have positive-definite matrix image. The polar representation therefore supplies a proof and a normalisation of the Cartan decomposition at once: the boost is the Hermitian positive square root of $\tilde{\Lambda}\tilde{\Lambda}^\dagger$, and the positivity is exactly the condition that removes the sign ambiguity of the Cartan factorisation.

### What the Two Extra Factors Mean

For a general element of the algebra, and not only for a Lorentz rotor, the modulus is not the unit and cannot be discarded. The group of units of $\mathbb{B}$ is $GL(2,\mathbb{C})$, whose polar representation carries a positive scale and a unitary phase in addition to the positive Hermitian factor and the unitary factor, and the two extra factors are the two extra real dimensions $1+1$ of the modulus. In the four-vector reading they are the two numbers that specify a four-vector rather than a Lorentz transformation: its **length** and the sector in which it lives.

## The Central Phase and the Two Sectors

### The Phase of a Four-Vector Is the $ict$

Take a four-position on a world line of velocity $\mathbf{v} = \beta c\,\hat{\mathbf{u}}$, with time component $ct$. In the material sector it is

$$
\tilde{X} = i\,ct\,e_0 + \beta c t\,\hat{\mathbf{u}} ,
$$

and its norm form is the interval

$$
N(\tilde{X}) = -c^2t^2 + \beta^2c^2t^2 = -c^2t^2\left(1-\beta^2\right) ,
$$

a **negative** real for a timelike displacement. The principal square root of a negative real is positive imaginary, so

$$
\rho = \sqrt{N(\tilde{X})} = i\,ct\sqrt{1-\beta^2} , \qquad r = c t\sqrt{1-\beta^2} = c\tau , \qquad \alpha = \frac{\pi}{2} ,
$$

where $\tau$ is the proper time: the scale is $c$ times the proper time, and the phase is $\pi/2$. The phase is thus the object that makes the time component imaginary, and it takes the value $\pi/2$ exactly on the timelike four-vectors. For a spacelike displacement, whose interval is positive, the modulus is real and the phase vanishes, $\alpha = 0$. The two values $\alpha = 0$ and $\alpha = \pi/2$ are the two sectors: the sector exchange $i\mathbb{M}_- = \mathbb{M}_+$ of the four-vector article is the multiplication by the phase factor at its two distinguished angles.

For the four-velocity and the four-momentum the same computation gives the standard constants. With $u^\mu = \gamma c(1,\boldsymbol\beta)$ the interval is $N = -c^2$, so the scale is $c$ itself; with $p^\mu = \gamma m c(1,\boldsymbol\beta)$ the interval is $N = -m^2c^2$, so the scale is $mc$. In each case the phase is $\pi/2$, and the boost and rotation factors carry the frame.

### The Phase as the Central Circle

The phase factor $e^{i\alpha}$ is central, so it commutes with every element of the algebra and may be written on either side of the other three factors. The corpus reads this circle as the framework's internal symmetry: it is the central $U(1)$ of the gauge structure, the phase of the mass term that bosonizes to a shift of the boson field, the weighting of the $\theta$ vacuum, and the circle of the $\mathrm{Spin}^c$ structure of the spinor module. The polar representation adds to those readings one statement that is purely algebraic: the phase is determined by the element as half the argument of its determinant, so for a **Lorentz rotor** it vanishes identically, and a nonzero phase is the obstruction to an element of the algebra being a Lorentz transformation.

### The Phase Cannot Be Removed by a Lorentz Transformation

The norm form is invariant under the rotor conjugation $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ with $N(\tilde{\Lambda}) = e_0$, and the modulus inherits the invariance:

$$
N\left(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger\right) = N(\tilde{\Lambda})N(\tilde{Q})N\left(\tilde{\Lambda}^\dagger\right) = N(\tilde{Q}) .
$$

Hence $r$ and $\alpha$ are invariants of the orbit of $\tilde{Q}$ under the Lorentz group, and the phase is not a gauge artefact of the frame: two elements with different phases cannot be carried into one another by a Lorentz transformation. The phase is an invariant of the element, and it is the only one of the four factors that the algebra's own symmetry group cannot move.

## The Boost and the Two Rotor Normalisations

### The Boost Factor Is a Square

The boost factor of the polar representation of a four-vector is the **square** of the boost rotor that the physics articles use, taken in the normalisation that carries the rest frame to the lab frame, and the reason is the structure of the action. A Lorentz rotor $\tilde{\Lambda}$ acts on a four-vector by conjugation, $X\mapsto\tilde{\Lambda}X\tilde{\Lambda}^\dagger$, so the rotor appears twice. With the corpus's convention $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $\hat{\mathbf{u}} = \mathbf{v}/|\mathbf{v}|$, the rotor carries the four-position of a particle of velocity $\mathbf{v}$ into its rest four-position,

$$
\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger = ic\tau\,e_0 ,
\qquad\text{hence}\qquad
\tilde{X} = \tilde{\Lambda}^\dagger\left(ic\tau e_0\right)\tilde{\Lambda} = ic\tau\,\tilde{\Lambda}^{\dagger 2} = ic\tau\,\bar{\tilde{\Lambda}}^2 ,
$$

where the last step uses the Hermitian character of a pure boost rotor, $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}$. The comparison with the representation of the same four-position,

$$
\tilde{X} = c\tau\,e^{i\pi/2}\,B , 
$$

identifies the boost factor with the square of the **conjugate** rotor, the rotor of rapidity $-\psi$ which carries the rest frame to the lab frame: $B = \bar{\tilde{\Lambda}}^2$, or equivalently

$$
\bar{\tilde{\Lambda}} = B^{1/2} ,
$$

the **unique positive-definite square root** of the boost factor. The same factor is the four-velocity in the Hermitian normalisation: with $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ the four-velocity of the corpus,

$$
B = \bar{\tilde{\Lambda}}^2 = -\frac{i}{c}\tilde{U} = \gamma e_0 - i\gamma\frac{\mathbf{v}}{c} ,
$$

which is the corpus's own relation $\tilde{\Lambda}^2 = -\frac{i}{c}\bar{\tilde{U}}$ read with the rotor conjugated. This is the normalisation that the Cartan decomposition of the corpus describes by requiring the matrix image of the boost to be positive definite, and it is the reason the polar representation has no $\pm$ ambiguity: the two square roots of $B$ are $\bar{\tilde{\Lambda}}$ and $-\bar{\tilde{\Lambda}}$, one positive definite and one negative definite, and the representation selects the first.

Numerical verification, with $ct = 1$ and the velocity $\mathbf{v}$ in units of $c$:

| $\mathbf{v}/c$ | interval $N$ | $r$ | $\alpha$ | $B$ | $\bar{\tilde{\Lambda}}$ |
|---|---|---|---|---|---|
| $(0.6,0,0)$ | $-0.64$ | $0.8$ | $\pi/2$ | $1.25 - 0.75\,ie_1$ | $1.060660172 - 0.353553391\,ie_1$ |
| $(0.6,0.4,0)$ | $-0.48$ | $0.692820323$ | $\pi/2$ | $1.443375673 - 0.866025404\,ie_1 - 0.577350269\,ie_2$ | $1.105299885 - 0.391760379\,ie_1 - 0.261173586\,ie_2$ |
| $(0.3,-0.5,0.6)$ | $-0.30$ | $0.547722558$ | $\pi/2$ | $1.825741858 - 0.547722558\,ie_1 + 0.912870929\,ie_2 - 1.095445115\,ie_3$ | $1.188642473 - 0.230398362\,ie_1 + 0.383997270\,ie_2 - 0.460796724\,ie_3$ |

In each row $B = \bar{\tilde{\Lambda}}^2$ to $3.3\times10^{-16}$, the scale equals $ct\sqrt{1-\beta^2}$, the phase is $\pi/2$, and the rotor $\hat{q}$ is the identity to $7\times10^{-16}$. The rotor in the last column is $\bar{\tilde{\Lambda}}$, the conjugate of the corpus's boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ with $\tanh\psi = \beta$ and $\hat{\mathbf{u}} = \mathbf{v}/|\mathbf{v}|$; it is the rotor of the inverse boost, of rapidity $-\psi$, so the sign of its vector part is opposite to the sign of $\mathbf{v}$.

### The Rotor and the Thomas–Wigner Rotation

The fourth factor is the unit real quaternion, the element of $\mathrm{Sp}(1) = SU(2)$, and it is the spatial rotation of the frame. It is not optional even for a pure boost, because the boosts do not close: the product of two non-collinear boost rotors has a non-hermitian part, and the Cartan decomposition of that product exhibits it as the **Thomas–Wigner rotation**, which is the rotor factor of the polar representation of the product. The algebraic mechanism is the non-commutativity of the boost factor with the rotor, taken up with its numbers in the section *The Order of the Factors* below. The composition law, the angle of the Wigner rotation, and the information content of the boost are the subjects of the companion articles *The Lorentz Group in Biquaternionic Form*, *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form* and *Exercise: The Thomas Precession*.

The rotor of the representation of a four-vector has a direct kinematic reading. A four-position on a world line with velocity $\mathbf{v}$ has $B = \bar{\tilde{\Lambda}}^2$ and $\hat{q} = e_0$ in the frame in which $\mathbf{v}$ is the velocity, as the table shows: the boost factor is the square of the rotor that carries the rest frame to the lab frame, and the rotor is trivial because a single boost needs no rotation. The rotor becomes nontrivial whenever the element is not a pure boost of a coordinate direction, and it is then the rotation that the residual frame carries.

## Worked Examples

### A Boost Rotor of the Physics Corpus

Take the boost rotor at speed $0.6c$ along $e_1$ used in the physics articles,

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}e_1 , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

that is, $\tilde{\Lambda} = 1.060660172\,e_0 + 0.353553391\,ie_1$. Its norm form is $N(\tilde{\Lambda}) = \cosh^2\frac{\psi}{2} - \sinh^2\frac{\psi}{2} = 1$, so the modulus is $\rho = 1$, the scale is $r = 1$, the phase is $\alpha = 0$, and the representation returns

$$
\tilde{\Lambda} = 1\cdot e^{i\cdot0}\cdot B\cdot\hat{q} , \qquad B = \tilde{\Lambda} , \qquad \hat{q} = e_0 ,
$$

with $B = \tilde{\Lambda}$, since a Hermitian positive-definite element is its own positive-definite factor and the rotor is then $\hat{q} = \bar{B}\tilde{\Lambda} = N(\tilde{\Lambda})e_0 = e_0$. The example is the one the maths companion article uses, and it is the reason the physics corpus works with two factors instead of four: on the Lorentz group the first two are trivial.

### A Four-Position and Its Proper Time

Take $\tilde{X} = i\,e_0 + 0.6\,e_1$, the four-position of a particle at $ct = 1$ moving at $0.6c$ along $e_1$. Then

$$
N(\tilde{X}) = -1+0.36 = -0.64 , \qquad r = 0.8 = c\tau , \qquad \alpha = \frac{\pi}{2} ,
$$

so the scale is the proper time and $B = 1.25e_0 - 0.75ie_1$, the square of the conjugate of the rotor of the previous example, $B = \bar{\tilde{\Lambda}}^2 = -(i/c)\tilde{U}$ with $\tilde{U} = \gamma(ie_0+0.6e_1)$ the four-velocity; the three rows of the table above are the rest of this family. The four-position is the proper time times the imaginary unit times that square, applied twice because the rotor acts by conjugation on both sides.

### A General Element of the Algebra

Take $\tilde{Q} = (1+i)e_0 + e_1 + 2e_2$, the element the maths companion uses. It is not a Lorentz rotor and not a four-vector: its scalar coefficient has both a real and an imaginary part. Its determinant in the $2\times2$ representation is

$$
\det\Phi(\tilde{Q}) = N(\tilde{Q}) = 5+2i ,
$$

with modulus $\sqrt{29} = 5.385164807$, so $r = 2.320595787$ and $\alpha = 0.190253189$ rad; its determinant in the $4\times4$ representation is $N^2 = 21+20i$, whose square root has modulus $29$ and argument $2\alpha$, and its $4\times4$ trace is $4Q_0 = 4+4i$. The boost factor is

$$
B = 1.072349609\,e_0 - 0.173166789\,ie_1 - 0.346333577\,ie_2 ,
$$

of rapidity $0.756273220$ about the axis $-(1,2,0)/\sqrt5$, and the rotor is

$$
\hat{q} = 0.470592172\,e_0 + 0.394599292\,e_1 + 0.789198585\,e_2 ,
$$

a rotation of $2.161669$ rad about $(1,2,0)/\sqrt5$. The element is a scale, a phase, a boost and a rotation, and no Lorentz transformation can remove the phase, since it is an invariant of the orbit.

### A Null Four-Vector

Take $\tilde{X} = i\,e_0 + e_1$, a displacement on the light cone, since $N(\tilde{X}) = -1+1 = 0$. The polar representation does not exist: the modulus is zero, the element is a zero divisor, and every one of the four factors fails. The physics is the standard one: a null four-vector has no proper length, so there is no scale to extract, and the algebra's zero divisors and the light cone are the same set, as the companion articles on zero divisors and on causality state.

## The Four Factors in One Table

| factor | algebra | determinant | physics |
|---|---|---|---|
| $r$ | positive real | $|\det\Phi|^{1/2}$ | length: $c\tau$ for a four-position, $c$ for a four-velocity, $mc$ for a four-momentum |
| $e^{i\alpha}$ | central circle $U(1)$ | $\tfrac12\arg\det\Phi$ | the $ict$ and the sector; $\pi/2$ timelike, $0$ spacelike; the central gauge phase |
| $B$ | Hermitian positive, $N(B) = 1$ | $\det\Phi(B) = 1$ | the Lorentz boost in positive-definite normalisation, $B = \bar{\tilde{\Lambda}}^2 = -(i/c)\tilde{U}$ |
| $\hat{q}$ | unit real quaternion | $\det\Phi(\hat{q}) = 1$ | the spatial rotation; the Thomas–Wigner rotation in a product of boosts |

The four rows are the four factors, and the determinant column shows what each contributes to the determinant of the element: the first two give the determinant, the last two have determinant one and contribute nothing to it. That is the precise sense in which the scale and the phase are the modulus and the boost and the rotor are the normalised transformation.

## The Order of the Factors

**The order of the four factors is physical, because $B$ does not commute.** In the physics reading the word $e^{i\alpha}B\hat{q}$ is the order of the operations: the transfer of $ict$, then the boost, then the rotation. The boost factor and the rotor do not commute with one another, so a boost followed by a rotation is not the same displacement as that rotation followed by that boost. With $B$ the boost of $\beta = 0.6$ along $\hat{\mathbf{x}}$ and $\hat{q}$ a rotation of $0.5$ rad about $\hat{\mathbf{z}}$,

$$
\left\|B\hat{q} - \hat{q}B\right\| = 0.339005 ,
$$

where $\|\cdot\|$ denotes the largest modulus among the coefficient differences, and the two products carry the same four-vector to different places. There is no way to write one for the other except by conjugation, $\hat{q}B = (\hat{q}B\hat{q}^{-1})\hat{q}$, which rotates the boost axis and leaves the rapidity alone.

The same holds for two boosts, and there the physics is the Thomas–Wigner rotation. With $\beta = 0.6$ along $\hat{\mathbf{x}}$ and $\beta = 0.6$ along $\hat{\mathbf{y}}$,

$$
\tilde{\Lambda}_1\tilde{\Lambda}_2 \neq \tilde{\Lambda}_2\tilde{\Lambda}_1 , \qquad \left\|\tilde{\Lambda}_1\tilde{\Lambda}_2 - \tilde{\Lambda}_2\tilde{\Lambda}_1\right\| = 0.25 ,
$$

and the two polar representations of the two products have the same unit modulus ($r = 1$, $\alpha = 0$), the same rapidity, the same Wigner angle $0.221314442$ rad, and opposite Wigner axis:

| order | $B$ | $\hat{q}$ |
|---|---|---|
| $\tilde{\Lambda}_1\tilde{\Lambda}_2$ | $1.131923142 + 0.414118223\,ie_1 + 0.331294578\,ie_2$ | $0.993883735 - 0.110431526\,e_3$ |
| $\tilde{\Lambda}_2\tilde{\Lambda}_1$ | $1.131923142 + 0.331294578\,ie_1 + 0.414118223\,ie_2$ | $0.993883735 + 0.110431526\,e_3$ |

Reversing the order exchanges the two components of the boost and mirrors the residual rotation through the plane of the two boosts. Both products are boosts up to a rotation, which is the non-closure of the boosts stated in the representation: the rapidity of a product of boosts is not the sum of the rapidities, and the difference is carried by the rotor.

The central phase is the one factor that may be moved. It is central, so $e^{i\alpha}$ commutes with $B$ and with $\hat{q}$, and the $ict$ transfer can be performed before or after the boost and the rotation alike; that freedom is what makes the phase the internal symmetry factor of the representation. Reading the four factors as "the $ict$, then the boost, then the rotation" is a reading of one word, not a licence to reorder it.

**The published word is the same element, with the boost referred to the rotated axis.** Sangwine & Hitzer prove the polar factorisation in the reversed word, angle first,

$$
\tilde{Q} = |\tilde{Q}|\,e^{\alpha\theta_t}\,e^{I\beta\theta_h},
$$

with a complex modulus in place of the corpus's scale and phase. Their trigonometric factor is the rotor $\hat{q}$ of this section exactly, and their hyperbolic factor is the boost about the rotor-conjugated axis, $\hat{q}^{-1}B\hat{q}$, of the same rapidity and the same norm form; recomputed on their own example the two factors multiply to the corpus word, since $\hat{q}\,(\hat{q}^{-1}B\hat{q}) = B\hat{q}$. Their reversed order is therefore not the reversed physical order of this section and must not be read as an identification of $\hat{q}B$ with $B\hat{q}$: the hyperbolic factor they write is not $B$ but its conjugate, the conjugation being the one already displayed above, which rotates the boost axis and leaves the rapidity alone. The same element is described by the two words, once with the boost in the original frame and once with the boost in the rotated one.

The non-commutativity of $B$ is a property of the algebra and not of the representation, and its infinitesimal form is in the brackets of the companion article *The Lorentz Group in Biquaternionic Form*: with the rotation generators $J_k = e_k$ and the boost generators $K_k = ie_k$, the brackets read $[J_j,K_k] = 2\varepsilon_{jkl}K_l$ and $[K_j,K_k] = -2\varepsilon_{jkl}J_l$. The rotations and the boosts do not commute, and the boosts do not close: the bracket of two boost generators is a rotation generator, which is the Lie-algebraic origin of the rotor in the polar representation of a product of boosts. The two extremes are the ones where the order ceases to matter: two boosts along the same line commute, compose into a boost, and leave the rotor trivial, and a rotation about the axis of a boost commutes with it, so that the word is a single boost-rotation about that axis.

## Summary

The polar representation of a biquaternion is $r e^{i\alpha}B\hat{q}$, and in the physics of the corpus its four factors are the scale, the central phase, the Lorentz boost and the spatial rotation. On the Lorentz group, where the norm form is one, the scale and the phase are trivial and the representation is the Cartan decomposition $\tilde{\Lambda} = \tilde{B}\tilde{R}$, with the positivity of the boost factor supplying the normalisation. The modulus is $\sqrt{\det\Phi(\tilde{Q})}$, the scale is its modulus and the phase is half its argument, and both are invariants of the Lorentz orbit, since the determinant is multiplicative and the rotor conjugation multiplies by $N(\tilde{\Lambda})N(\tilde{\Lambda}^\dagger) = 1$. The boost factor of a four-vector is the square of the physics boost rotor in the rest-to-lab normalisation, $B = \bar{\tilde{\Lambda}}^2 = -(i/c)\tilde{U}$, so that rotor is the unique positive-definite square root of the representation's boost; for a four-position on a world line the scale is $c$ times the proper time and the phase is $\pi/2$, the angle that makes the time coordinate imaginary. The rotor is the Thomas–Wigner rotation when two boosts are composed, and it is the algebraic expression of the non-closure of the boosts. The representation fails exactly on the light cone, where the determinant vanishes, the element is a zero divisor, and the four-vector has no proper length.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a biquaternion, $Q_\mu\in\mathbb{C}$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ | the norm form, the determinant of the $2\times2$ representative |
| $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$, $\operatorname{Tr}\rho_L(\tilde{Q}) = 4Q_0$ | determinant and trace of the $4\times4$ regular representative |
| $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$ | the complex modulus |
| $r$ | the scale, $|\det\Phi|^{1/2}$ |
| $e^{i\alpha}$ | the central phase, $\alpha = \tfrac12\arg\det\Phi$ |
| $B\in\mathbb{M}_+$ | the boost factor, Hermitian positive, $N(B) = 1$ |
| $\hat{q}\in\mathbb{H}_{\mathbb{B}}$, $N(\hat{q}) = 1$ | the rotor, a unit real quaternion |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $\hat{\mathbf{u}} = \mathbf{v}/|\mathbf{v}|$ | the physics boost rotor; for a four-position $B = \bar{\tilde{\Lambda}}^2 = -(i/c)\tilde{U}$ |
| $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ | the four-velocity |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the informational and material sectors; four-vectors live in $\mathbb{M}_-$ |
| $\tilde{X} = ict\,e_0+\mathbf{x}$ | a four-position, interval $N = -c^2t^2+\mathbf{x}^2$ |

## Further Reading

- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the theorem, the four factors, the algorithm and the uniqueness.
- *Biquaternion Partial Polar Representations* (`articles_maths/biquaternion-partial-polar-representations.md`), for the Hamilton, complex and Cartan representations as the three pairings of the four factors.
- *The 2×2 Matrix Representation of Biquaternions* (`articles_physics/the-2x2-matrix-representation-of-biquaternions.md`), for $\det\Phi(\tilde{Q}) = N(\tilde{Q})$ and the matrix polar decomposition.
- *The 4×4 Regular Matrix Representation of Biquaternions* (`articles_physics/the-4x4-regular-matrix-representation-of-biquaternions.md`), for the squared determinant, the trace $4Q_0$ and the two chiralities.
- *The Four-Vector Representation of Biquaternions* (`articles_physics/the-four-vector-representation-of-biquaternions.md`), for the informational and material sectors, the interval and the real restrictions of the norm form.
- *The Lorentz Group in Biquaternionic Form: Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Cartan decomposition, the non-closure of the boosts and the Thomas–Wigner rotation.
- *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* (`articles_physics/the-two-sheeted-cover-and-the-topology-of-boosts-in-biquaternionic-form.md`), for the $\pm e_0$ kernel and the sign normalisation of the rotor.
- *Spin, Entropy and the Lorentz Group in Biquaternionic Form* (`articles_physics/spin-entropy-and-the-lorentz-group-in-biquaternionic-form.md`), for the reading of the central circle and the boost parameters as information.
- *Complex Polar Representation* (`articles_maths/complex-polar-representation.md`) and *Split-Complex Polar Representation* (`articles_maths/split-complex-polar-representation.md`), for the two-dimensional members of the series, where the exponential $e^{\alpha\theta}$ of each factor is classified by the trichotomy $\nu^2 = -1, 0, +1$.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential word discussed in the section on the order of the factors, whose hyperbolic factor is the boost referred to the rotor-rotated axis.
