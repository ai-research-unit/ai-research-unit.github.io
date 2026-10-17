# __The Polar Element Representation of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the algebra of the Lorentz group, of the four-vector, and of the spinor of the corpus. This article reads the **polar representation** from the physics side: the word

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\bigl(-i\psi\vec u_{\mathrm b}\bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) ,
\qquad r\in\mathbb{R}_{>0}, \quad \alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right], \quad \psi\ge0, \quad \theta\in[0,2\pi] ,
$$

a positive real and three exponentials. The corpus writes the same ordered product compactly as $r\exp(i\alpha)B\tilde q$, with

$$
B = \exp\bigl(-i\psi\vec u_{\mathrm b}\bigr) , \qquad \tilde q = \exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) ,
$$

and it is this compact writing that names the two physical factors, the boost $B$ and the rotation $\tilde q$.

The algebra, the existence, the uniqueness and the domain of the representation are established here.

What the article does with them is identify each of the four factors with an object that the physics articles of the corpus already use, and show that the Cartan decomposition of the Lorentz group, the determinant of the $2\times2$ and $4\times4$ matrix representations, and the interval of a four-vector are the four factors seen one at a time.

The dictionary is as follows, and each line is established in the section on its factor below.

| factor | physics interpretation |
|---|---|
| $r$ | the scale: the square root of the absolute value of the determinant, equal to the proper length of a four-vector |
| $\exp(i\alpha)$ | the central phase: the $\mathrm{U}(1)$ of the framework, which realises the $ict$ of the material sector as the angle $\pi/2$ |
| $B$ | the boost factor of the four-vector, the **square** of the boost rotor $\tilde{\Lambda}^{\natural} = \exp\bigl(-i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)$, in the positive-definite normalisation |
| $\tilde q$ | the spatial rotation, the subgroup $\mathrm{Sp}(1) = SU(2)$, and the Thomas–Wigner rotation when two boosts are composed |

Two consequences of the algebraic theorem are physical, and they frame the article.

First, a Lorentz rotor of unit norm has $r = 1$ and $\alpha = 0$, so the representation reduces on the Lorentz group to the Cartan decomposition $\tilde{\Lambda} = \tilde{B}\tilde U$, which is therefore a **special case** of the four-factor representation and not a separate theorem.

Second, the biquaternion norm is the determinant of the $2\times2$ representation, so the modulus of the representation is the square root of a determinant, and the four factors are respectively the absolute value of a determinant, an argument of a determinant, a positive Hermitian matrix, and a unitary matrix.

The physics of the representation is the physics of combining four objects under one multiplication, and the algebra of the representation is the matrix polar decomposition of $GL(2,\mathbb{C})$.

The conventions are those of *Conventions in the Biquaternion Universe* as used by *The Four-Vector Element Representation of Biquaternions*, *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

- **The basis.** $e_t = 1$ the algebra unit and $\vec e_x,\vec e_y,\vec e_z$ the quaternion units with $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$, so an element is written $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ with coefficients $Q_\mu \in \mathbb{C}$.
- **The scalar imaginary.** $i$, central, with $i^2 = -1$.
- **The biquaternion norm.** $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$.
- **The quaternion subspace $\mathbb{H}_{\mathbb{B}}$.** The fixed space of complex conjugation, the home of the rotations, whose unit sphere is $\mathrm{Sp}(1) = \{\tilde q \in \mathbb{H}_{\mathbb{B}} : \tilde q\tilde q^{\natural} = 1\}$, the group of unit real quaternions, meeting the informational sector in $\mathbb{R}e_t$ and the material sector in the pure-vector space.
- **The informational sector $\mathbb{M}_+$.** The Hermitian subspace, the home of the boosts.
- **The material sector $\mathbb{M}_-$.** The anti-fixed space of quaternion conjugation, with $Q_t = iq'_t$ and $Q_k = q_k$ real, the home of the four-vectors, with the interval $N = -c^2t^2+x^2+y^2+z^2$.

An element is **unitary** when it preserves the form, $\tilde{Q}\tilde{Q}^{*}=e_t$, and the unitary elements form the group $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$; the condition is narrower than norm one, the norm-one group being $\mathbb{B}^{\times}_1=\{N=e_t\}\cong SL(2,\mathbb{C})$ (*Conventions in the Biquaternion Universe*, §*The Unitary Convention*), and the rotor of a Lorentz transformation is the norm-one unitary element.

## The Polar Word

The word is the ordered product of a positive real and three exponentials of single elements of the algebra,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\bigl(-i\psi\vec u_{\mathrm b}\bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) ,
$$

and the four sections that follow read the four factors off the element one at a time. Three objects are shared by them and are fixed here once.

**The four factors in one table.** The physics normalisation is the one in which the boost factor is $B = \exp(-i\psi\vec u_{\mathrm b})$ with $\psi$ the rapidity of the frame.

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis | determinant | physics |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $r$ | hyperbolic | $r$ | $\ln r \in \mathbb{R}$, $r > 0$ | $\mathbb{R}e_t$, the real line | $\lvert\det\mathsf{M}_2\rvert^{1/2}$ | length: $c\tau$, $c$, $mc$ |
| 2 | $\exp(i\alpha)$ | central phase | $1$ | $\exp(i\alpha)$ | trigonometric | $\cos\alpha\,e_t + i\sin\alpha$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$ | $\tfrac12\arg\det\mathsf{M}_2$ | the $ict$ and the sector; $\pi/2$ timelike, $0$ spacelike |
| 3 | $B$ | boost factor | $3$ | $\exp(-i\psi\vec u_{\mathrm b})$ | hyperbolic | $\cosh\psi\,e_t - i\sinh\psi\,\vec u_{\mathrm b}$ | rapidity $\psi \in \mathbb{R}$, $\psi \ge 0$ | $\mathbb{M}_+$, traceless; $\vec u_{\mathrm b} \in \mathcal{A}$ | $1$ | the Lorentz boost, $B = (\tilde{\Lambda}^{\natural})^2 = -(i/c)\tilde{V}$ |
| 4 | $\tilde q$ | rotor | $3$ | $\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2}\,e_t + \sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$ | rotation angle $\theta \in [0,2\pi]$ | $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$; $\vec u_{\mathrm r} \in \mathcal{A}$ | $1$ | the spatial rotation; the Thomas–Wigner rotation |

The determinant column shows what each factor contributes to the determinant of the element: the first two give the determinant, the last two have determinant one and contribute nothing to it. That is the precise sense in which the scale and the phase are the modulus and the boost and the rotor are the normalised transformation.

**The trichotomy of the exponent.** Each of the three exponents is a parameter times a root of $-e_t$, $0$ or $+e_t$, and the character of its exponential is the square of that root. For an element $\nu$ and a real $t$, the series $\exp(\nu t)=\sum_{n\ge0}\nu^nt^n/n!$ collapses according to the square of $\nu$:

- the trigonometric case $\nu^2 = -e_t$ gives $\cos t\,e_t + \nu\sin t$;
- the parabolic case $\nu^2 = 0$ gives the truncation $e_t + \nu t$;
- the hyperbolic case $\nu^2 = +e_t$ gives $\cosh t\,e_t + \nu\sinh t$.

| factor | parameter | root | its square | case |
|---|---|---|---|---|
| $r$ | $\ln r$ | $e_t$ | $+e_t$ | hyperbolic, degenerate |
| $\exp(i\alpha)$ | $\alpha$ | $i$ | $-e_t$ | trigonometric, central |
| $B$ | $\psi$ | $-i\vec u_{\mathrm b}$ | $+e_t$ | hyperbolic |
| $\tilde q$ | $\tfrac{\theta}{2}$ | $\vec u_{\mathrm r}$ | $-e_t$ | trigonometric |

The parabolic row carries no factor of this representation, although the algebra has nilpotents on which it is occupied. The three exponent types distribute as the table shows: the boost factor has a Hermitian root of $+e_t$ and is hyperbolic, the rotor and the central phase have roots of $-e_t$ and are trigonometric, and the scale is the degenerate hyperbolic factor, the only one written without an exponential.

**The two axes and the frame.** The boost factor carries the frame's velocity, and the rotor the frame's rotation. The rapidity is $\psi \in \mathbb{R}$, $\psi \ge 0$, the velocity is $\vec v \in \mathbb{R}^3$ with $\tanh\psi = \lvert\vec v\rvert/c$, and the boost axis is the unit direction $\vec u_{\mathrm b} = \vec v/\lvert\vec v\rvert \in \mathcal{A}$; the rotation angle is $\theta \in [0,2\pi]$ about the unit axis $\vec u_{\mathrm r} \in \mathcal{A}$, a pure real quaternion of norm one. Here $\mathcal{A}$ is the axis sphere, the set of unit vectors of $\mathbb{R}^3$. The physics boost rotor of the corpus is the square root of the boost factor,

$$
\tilde{\Lambda} = \exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u_{\mathrm b} , \qquad \tilde{\Lambda}^{\natural} = B^{1/2} = \exp\Bigl(-i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr) ,
$$

and §*The Boost* below constructs the positive-definite square root and fixes which of the two square roots the representation selects.

**The order of the word.** The word $\exp(i\alpha)B\tilde q$ is the ordered product of its factors, and the order is the physical order of the operations, because $\exp(-i\psi\vec u_{\mathrm b})$ and $\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ do not commute. §*The Order of the Factors* measures the failure; here it fixes the reading, which is the transfer of the $ict$, then the boost, then the rotation.

## The Scale

**The scale is the square root of the determinant.** In the $2\times2$ matrix representation the biquaternion norm is the determinant,

$$
\det\mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2 ,
$$

and in the $4\times4$ regular representation the determinant is its square and the trace is four times the scalar part,

$$
\det\mathsf{M}_4(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}^2 , \qquad \operatorname{Tr}\mathsf{M}_4(\tilde{Q}) = 4Q_t .
$$

The modulus of the polar representation is $\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$, so the scale and the phase are the polar form of the determinant,

$$
r = \left|\det\mathsf{M}_2(\tilde{Q})\right|^{1/2} , \qquad \alpha = \tfrac12\arg\det\mathsf{M}_2(\tilde{Q}) ,
$$

and the scale in particular is the modulus of the determinant. Every statement about the scale is therefore a statement about the determinant of the matrix representative, and the failure of the representation at $\langle\tilde{Q}\rangle_{\natural} = 0$ is the failure of the matrix representative to be invertible. In the four-vector interpretation, $\langle\tilde{Q}\rangle_{\natural} = 0$ is the light cone: the polar representation of a biquaternion is available exactly on the nonzero elements off the light cone.

**The condition, and why it is mild.** The representation of $\tilde{Q}$ exists if and only if $\tilde{Q}$ lies outside the light cone,

$$
\langle\tilde{Q}\rangle_{\natural}\neq0 ,
$$

and the excluded elements are exactly the zero divisors, of which the null four-vector of the worked examples below is the physics instance. The condition is one complex equation, hence two real equations, $\mathrm{Re}\,N = 0$ and $\mathrm{Im}\,N = 0$, so the light cone has real codimension two in the algebra: with $\dim_{\mathbb{R}}\mathbb{B} = 8$ the cone has real dimension $6$, while the group of units and the algebra itself both have real dimension $8$. Removing the cone therefore leaves an eight-dimensional domain, the same dimension as the algebra, and every failure of the representation is the failure of invertibility on that cone. The count is that of the algebra, where the four coefficients are complex; restricted to the four-dimensional slice of physical four-vectors, whose first coefficient is $ict$ and whose last three are real, the same equation is the familiar light cone of codimension one in that slice, of real dimension three.

### The Scale Is the Proper Length

Take a four-position on a world line of velocity $\vec v = \beta c\,\vec u_{\mathrm b}$, with time component $ct$. In the material sector it is

$$
\tilde{Q} = i\,ct\,e_t + \beta c t\,\vec u_{\mathrm b} ,
$$

and its biquaternion norm is the interval

$$
\langle\tilde{Q}\rangle_{\natural} = -c^2t^2 + \beta^2c^2t^2 = -c^2t^2\left(1-\beta^2\right) ,
$$

a **negative** real for a timelike displacement. The principal square root of a negative real is positive imaginary, so the modulus is $\rho = i\,ct\sqrt{1-\beta^2}$, and its modulus gives the scale

$$
r = c t\sqrt{1-\beta^2} = c\tau ,
$$

where $\tau$ is the proper time: the scale is $c$ times the proper time. For a spacelike displacement, whose interval is positive, the modulus is real and the scale is the ordinary length $\sqrt{N}$.

For the four-velocity and the four-momentum the same computation gives the standard constants. With $v^\mu = \gamma c(1,\vec\beta)$ the interval is $N = -c^2$, so the scale is $c$ itself; with $p^\mu = \gamma m c(1,\vec\beta)$ the interval is $N = -m^2c^2$, so the scale is $mc$. In each case the boost and rotation factors carry the frame, and the phase is fixed (§*The Central Phase*).

### The Unit-Norm Slice Is the Lorentz Group

For a Lorentz rotor $\tilde{\Lambda}$ the biquaternion norm is the unit, $\langle\tilde{\Lambda}\rangle_{\natural} = e_t$, so $r = 1$ and $\alpha = 0$ and the representation collapses to two factors,

$$
\tilde{\Lambda} = B\,\tilde q , \qquad B\in\mathbb{M}_+,\quad \tilde q\in\mathrm{Sp}(1) .
$$

This is the **Cartan decomposition** of the Lorentz group as the companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations* states it: every unit-norm biquaternion is a boost times a spatial rotation, unique when the boost is required to have positive-definite matrix image. The polar representation therefore supplies a proof and a normalisation of the Cartan decomposition at once: the boost is the Hermitian positive square root of $\tilde{\Lambda}\tilde{\Lambda}^{*}$, and the positivity is exactly the condition that removes the sign ambiguity of the Cartan factorisation. On this slice the scale contributes nothing, and the whole of the physical content is in the pair $(B,\tilde q)$.

### What the Two Extra Factors Mean

For a general element of the algebra, and not only for a Lorentz rotor, the modulus is not the unit and cannot be discarded. The group of units of $\mathbb{B}$ is $GL(2,\mathbb{C})$, whose polar representation carries a positive scale and a unitary phase in addition to the positive Hermitian factor and the unitary factor, and the two extra factors are the two extra real dimensions $1+1$ of the modulus. In the four-vector interpretation they are the two numbers that specify a four-vector rather than a Lorentz transformation: its **length**, the scale, and the **sector** in which it lives, read off the phase.

## The Central Phase

**The phase of a four-vector is the $ict$.** On the world-line element of §*The Scale* the modulus is $i\,ct\sqrt{1-\beta^2}$, a positive imaginary number, so apart from the scale the phase is

$$
\alpha = \frac{\pi}{2} ,
$$

and the phase is thus the object that makes the time component imaginary: it takes the value $\pi/2$ exactly on the timelike four-vectors. For a spacelike displacement, whose interval is positive, the modulus is real and the phase vanishes, $\alpha = 0$. The two values $\alpha = 0$ and $\alpha = \pi/2$ are the two sectors: the sector exchange $i\mathbb{M}_- = \mathbb{M}_+$ of the four-vector article is the multiplication by the phase factor at its two distinguished angles.

### The Phase as the Central Circle

The phase factor $\exp(i\alpha)$ is central, so it commutes with every element of the algebra and may be written on either side of the other three factors. The corpus reads this circle as the framework's internal symmetry: it is the central $\mathrm{U}(1)$ of the gauge structure, the phase of the mass term that bosonizes to a shift of the boson field, the weighting of the $\theta$ vacuum, and the circle of the $\mathrm{Spin}^c$ structure of the spinor module. The polar representation adds to those interpretations one statement that is purely algebraic: the phase is determined by the element as half the argument of its determinant, so for a **Lorentz rotor** it vanishes identically, and a nonzero phase is the obstruction to an element of the algebra being a Lorentz transformation.

### The Phase Cannot Be Removed by a Lorentz Transformation

The biquaternion norm is invariant under the rotor conjugation $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ with $\langle\tilde{\Lambda}\rangle_{\natural} = e_t$, and the modulus inherits the invariance:

$$
N\left(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}\right) = \langle\tilde{\Lambda}\rangle_{\natural}\langle\tilde{Q}\rangle_{\natural}N\left(\tilde{\Lambda}^{*}\right) = \langle\tilde{Q}\rangle_{\natural} .
$$

Hence $r$ and $\alpha$ are invariants of the orbit of $\tilde{Q}$ under the Lorentz group, and the phase is not a gauge artefact of the frame: two elements with different phases cannot be carried into one another by a Lorentz transformation. The phase is an invariant of the element, and it is the only one of the four factors that the algebra's own symmetry group cannot move.

## The Boost

### The Boost Factor Is a Square

The boost factor of the polar representation of a four-vector is the **square** of the boost rotor that the physics articles use, taken in the normalisation that carries the rest frame to the lab frame, and the reason is the structure of the action. A Lorentz rotor $\tilde{\Lambda}$ acts on a four-vector by conjugation, $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, so the rotor appears twice. With the corpus's convention $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$, $\vec u_{\mathrm b} = \vec v/|\vec v|$, the rotor carries the four-position of a particle of velocity $\vec v$ into its rest four-position,

$$
\tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*} = ic\tau\,e_t ,
\qquad\text{hence}\qquad
\tilde{Q} = \tilde{\Lambda}^{*}\left(ic\tau e_t\right)\tilde{\Lambda} = ic\tau\,\tilde{\Lambda}^{*2} = ic\tau\,(\tilde{\Lambda}^{\natural})^2 ,
$$

where the last step uses the Hermitian character of a pure boost rotor, $\tilde{\Lambda}^{*} = \tilde{\Lambda}^{\natural}$. The comparison with the representation of the same four-position,

$$
\tilde{Q} = c\tau\,\exp(i\pi/2)\,B ,
$$

identifies the boost factor with the square of the **conjugate** rotor, the rotor of rapidity $-\psi$ which carries the rest frame to the lab frame: $B = (\tilde{\Lambda}^{\natural})^2$, or equivalently

$$
\tilde{\Lambda}^{\natural} = B^{1/2} ,
$$

the **unique positive-definite square root** of the boost factor. This is the normalisation that the Cartan decomposition of the corpus describes by requiring the matrix image of the boost to be positive definite, and it is the reason the polar representation has no $\pm$ ambiguity: the two square roots of $B$ are $\tilde{\Lambda}^{\natural}$ and $-\tilde{\Lambda}^{\natural}$, one positive definite and one negative definite, and the representation selects the first.

### The Boost Is the Four-Velocity in the Hermitian Normalisation

The same factor is the four-velocity in the Hermitian normalisation: with $\tilde{V} = \gamma(ic\,e_t+\vec v)$ the four-velocity of the corpus,

$$
B = (\tilde{\Lambda}^{\natural})^2 = -\frac{i}{c}\tilde{V} = \gamma e_t - i\gamma\frac{\vec v}{c} ,
$$

which is the corpus's own relation $\tilde{\Lambda}^2 = -\frac{i}{c}\tilde{V}^{\natural}$ read with the rotor conjugated. The boost factor is therefore an element of the Hermitian subspace $\mathbb{M}_+$ of unit biquaternion norm, the four-velocity up to the factor $-i/c$, and its closed form $\cosh\psi\,e_t - i\sinh\psi\,\vec u_{\mathrm b}$ is the four-velocity of rapidity $\psi$ about $\vec u_{\mathrm b}$.

### Numerical Verification

With $ct = 1$ and the velocity $\vec v$ in units of $c$:

| $\vec v/c$ | interval $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde{\Lambda}^{\natural}$ |
|---|---|---|---|---|---|
| $(0.6,0,0)$ | $-0.64$ | $0.8$ | $\pi/2$ | $1.25 - 0.75\,i\vec e_x$ | $1.060660172 - 0.353553391\,i\vec e_x$ |
| $(0.6,0.4,0)$ | $-0.48$ | $0.692820323$ | $\pi/2$ | $1.443375673 - 0.866025404\,i\vec e_x - 0.577350269\,i\vec e_y$ | $1.105299885 - 0.391760379\,i\vec e_x - 0.261173586\,i\vec e_y$ |
| $(0.3,-0.5,0.6)$ | $-0.30$ | $0.547722558$ | $\pi/2$ | $1.825741858 - 0.547722558\,i\vec e_x + 0.912870929\,i\vec e_y - 1.095445115\,i\vec e_z$ | $1.188642473 - 0.230398362\,i\vec e_x + 0.383997270\,i\vec e_y - 0.460796724\,i\vec e_z$ |

In each row $B = (\tilde{\Lambda}^{\natural})^2$ to $3.3\times10^{-16}$, the scale equals $ct\sqrt{1-\beta^2}$, the phase is $\pi/2$, and the rotor $\tilde q$ is the identity to $7\times10^{-16}$. The rotor in the last column is $\tilde{\Lambda}^{\natural}$, the conjugate of the corpus's boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ with $\tanh\psi = \beta$ and $\vec u_{\mathrm b} = \vec v/|\vec v|$; it is the rotor of the inverse boost, of rapidity $-\psi$, so the sign of its vector part is opposite to the sign of $\vec v$. The first row of the table in exponents is the frame of velocity $0.6c$ along $\vec e_x$, of rapidity $\psi = \operatorname{atanh}0.6 = 0.693147181$,

$$
\exp(-i\psi \vec e_x) = \cosh\psi - i\sinh\psi\,\vec e_x = 1.25 - 0.75\,i\vec e_x = B , \qquad \exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr) = 1.060660172 + 0.353553391\,i\vec e_x = \tilde{\Lambda} .
$$

## The Rotor

**The rotor is the spatial rotation.** The fourth factor is the unit real quaternion, the element of $\mathrm{Sp}(1) = SU(2)$, the group of unit real quaternions, and it is the spatial rotation of the frame. It is not optional even for a pure boost, because the boosts do not close: the product of two non-collinear boost rotors has a non-hermitian part, and the Cartan decomposition of that product exhibits it as the **Thomas–Wigner rotation**, which is the rotor factor of the polar representation of the product. The algebraic mechanism is the non-commutativity of the boost factor with the rotor, taken up with its numbers in §*The Order of the Factors* below. The composition law, the angle of the Wigner rotation, and the information content of the boost are the subjects of the companion articles *The Lorentz Group in Biquaternionic Form — Structure and Representations*, *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form* and *Exercise: The Thomas Precession*.

The rotor of the representation of a four-vector has a direct kinematic interpretation. A four-position on a world line with velocity $\vec v$ has $B = (\tilde{\Lambda}^{\natural})^2$ and $\tilde q = e_t$ in the frame in which $\vec v$ is the velocity, as the table of §*The Boost* shows: the boost factor is the square of the rotor that carries the rest frame to the lab frame, and the rotor is trivial because a single boost needs no rotation. The rotor becomes nontrivial whenever the element is not a pure boost of a coordinate direction, and it is then the rotation that the residual frame carries.

### The Rotor and the Thomas–Wigner Rotation

The rotor is the compact factor of the word, and it is what makes the boosts a group only up to a rotation. Two boost rotors of the corpus, of rapidities along different axes, multiply to an element whose Cartan decomposition splits into a boost of the composed rapidity and a rotation: the **Thomas–Wigner rotation**. The rotation is a rotor of the polar representation, and its angle and axis are computable from the two boost data; the worked instance with its numbers is in §*The Order of the Factors* below, where the two orderings of the same pair of boosts are compared. The rotor is also the only compact non-central factor, so it is the factor that carries the topological $\pm e_t$ cover of the corpus (*The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*).

## Worked Examples

### A Boost Rotor of the Physics Corpus

Take the boost rotor at speed $0.6c$ along $\vec e_x$ used in the physics articles,

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}e_t + i\sinh\frac{\psi}{2}\vec e_x , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

that is, $\tilde{\Lambda} = 1.060660172\,e_t + 0.353553391\,i\vec e_x$. Its biquaternion norm is $\langle\tilde{\Lambda}\rangle_{\natural} = \cosh^2\frac{\psi}{2} - \sinh^2\frac{\psi}{2} = 1$, so the modulus is $\rho = 1$, the scale is $r = 1$, the phase is $\alpha = 0$, and the representation returns

$$
\tilde{\Lambda} = 1\cdot \exp(i\cdot0)\cdot B\cdot\tilde q , \qquad B = \tilde{\Lambda} , \qquad \tilde q = e_t ,
$$

with $B = \tilde{\Lambda}$, since a Hermitian positive-definite element is its own positive-definite factor and the rotor is then $\tilde q = \bar{B}\tilde{\Lambda} = \langle\tilde{\Lambda}\rangle_{\natural}e_t = e_t$. The example is the one the maths companion article uses, and it is the reason the physics corpus works with two factors instead of four: on the Lorentz group the first two are trivial.

### A Four-Position and Its Proper Time

Take $\tilde{Q} = i\,e_t + 0.6\,\vec e_x$, the four-position of a particle at $ct = 1$ moving at $0.6c$ along $\vec e_x$. Then

$$
\langle\tilde{Q}\rangle_{\natural} = -1+0.36 = -0.64 , \qquad r = 0.8 = c\tau , \qquad \alpha = \frac{\pi}{2} ,
$$

so the scale is the proper time and $B = 1.25e_t - 0.75i\vec e_x$, the square of the conjugate of the rotor of the previous example, $B = (\tilde{\Lambda}^{\natural})^2 = -(i/c)\tilde{V}$ with $\tilde{V} = \gamma(ie_t+0.6\vec e_x)$ the four-velocity; the three rows of the table above are the rest of this family. The four-position is the proper time times the imaginary unit times that square, applied twice because the rotor acts by conjugation on both sides.

### A General Element of the Algebra

Take $\tilde{Q} = (1+i)e_t + \vec e_x + 2\vec e_y$, the element the maths companion uses. It is not a Lorentz rotor and not a four-vector: its scalar coefficient has both a real and an imaginary part. Its determinant in the $2\times2$ representation is

$$
\det\mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural} = 5+2i ,
$$

with modulus $\sqrt{29} = 5.385164807$, so $r = 2.320595787$ and $\alpha = 0.190253189$ rad; its determinant in the $4\times4$ representation is $N^2 = 21+20i$, whose square root has modulus $29$ and argument $2\alpha$, and its $4\times4$ trace is $4Q_t = 4+4i$. The boost factor is

$$
B = 1.072349609\,e_t - 0.173166789\,i\vec e_x - 0.346333577\,i\vec e_y ,
$$

of rapidity $0.756273220$ about the axis $-(1,2,0)/\sqrt5$, and the rotor is

$$
\tilde q = 0.470592172\,e_t + 0.394599292\,\vec e_x + 0.789198585\,\vec e_y ,
$$

a rotation of $2.161669$ rad about $(1,2,0)/\sqrt5$. The element is a scale, a phase, a boost and a rotation, and no Lorentz transformation can remove the phase, since it is an invariant of the orbit.

### A Null Four-Vector

Take $\tilde{Q} = i\,e_t + \vec e_x$, a displacement on the light cone, since $\langle\tilde{Q}\rangle_{\natural} = -1+1 = 0$. The polar representation does not exist: the modulus is zero, the element is a zero divisor, and every one of the four factors fails. The physics is the standard one: a null four-vector has no proper length, so there is no scale to extract, and the algebra's zero divisors and the light cone are the same set, as the companion articles on zero divisors and on causality state.


## The Order of the Factors

**The order of the four factors is physical, because $B$ does not commute.** In the physics interpretation the word $\exp(i\alpha)B\tilde q$ is the order of the operations: the transfer of $ict$, then the boost, then the rotation. The boost factor and the rotor do not commute with one another, so a boost followed by a rotation is not the same displacement as that rotation followed by that boost. With $B$ the boost of $\beta = 0.6$ along $\vec u_x$ and $\tilde q$ a rotation of $0.5$ rad about $\vec u_z$,

$$
\left\|B\tilde q - \tilde qB\right\| = 0.339005 ,
$$

where $\|\cdot\|$ denotes the largest modulus among the coefficient differences, and the two products carry the same four-vector to different places. There is no way to write one for the other except by conjugation, $\tilde qB = (\tilde qB\tilde q^{-1})\tilde q$, which rotates the boost axis and leaves the rapidity alone.

The same holds for two boosts, and there the physics is the Thomas–Wigner rotation. With $\beta = 0.6$ along $\vec u_x$ and $\beta = 0.6$ along $\vec u_y$,

$$
\tilde{\Lambda}_1\tilde{\Lambda}_2 \neq \tilde{\Lambda}_2\tilde{\Lambda}_1 , \qquad \left\|\tilde{\Lambda}_1\tilde{\Lambda}_2 - \tilde{\Lambda}_2\tilde{\Lambda}_1\right\| = 0.25 ,
$$

and the two polar representations of the two products have the same unit modulus ($r = 1$, $\alpha = 0$), the same rapidity, the same Wigner angle $0.221314442$ rad, and opposite Wigner axis:

| order | $B$ | $\tilde q$ |
|---|---|---|
| $\tilde{\Lambda}_1\tilde{\Lambda}_2$ | $1.131923142 + 0.414118223\,i\vec e_x + 0.331294578\,i\vec e_y$ | $0.993883735 - 0.110431526\,\vec e_z$ |
| $\tilde{\Lambda}_2\tilde{\Lambda}_1$ | $1.131923142 + 0.331294578\,i\vec e_x + 0.414118223\,i\vec e_y$ | $0.993883735 + 0.110431526\,\vec e_z$ |

Reversing the order exchanges the two components of the boost and mirrors the residual rotation through the plane of the two boosts. Both products are boosts up to a rotation, which is the non-closure of the boosts stated in the representation: the rapidity of a product of boosts is not the sum of the rapidities, and the difference is carried by the rotor.

The central phase is the one factor that may be moved. It is central, so $\exp(i\alpha)$ commutes with $B$ and with $\tilde q$, and the $ict$ transfer can be performed before or after the boost and the rotation alike; that freedom is what makes the phase the internal symmetry factor of the representation. Reading the four factors as "the $ict$, then the boost, then the rotation" is an interpretation of one word, not a licence to reorder it.

**The published word is the same element, with the boost referred to the rotated axis.** Sangwine & Hitzer prove the polar factorisation in the reversed word, angle first,

$$
\tilde{Q} = |\tilde{Q}|\,\exp(\alpha\theta_t)\,\exp(I\beta\theta_h),
$$

with a complex modulus in place of the corpus's scale and phase. Their trigonometric factor is the rotor $\tilde q$ of this section exactly, and their hyperbolic factor is the boost about the rotor-conjugated axis, $\tilde q^{-1}B\tilde q$, of the same rapidity and the same biquaternion norm; recomputed on their own example the two factors multiply to the corpus word, since $\tilde q\,(\tilde q^{-1}B\tilde q) = B\tilde q$. Their reversed order is therefore not the reversed physical order of this section and must not be read as an identification of $\tilde qB$ with $B\tilde q$: the hyperbolic factor they write is not $B$ but its conjugate, the conjugation being the one already displayed above, which rotates the boost axis and leaves the rapidity alone. The same element is described by the two words, once with the boost in the original frame and once with the boost in the rotated one.

The non-commutativity of $B$ is a property of the algebra and not of the representation, and its infinitesimal form is in the brackets of the companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*: with the rotation generators $J_k = \vec e_k$ and the boost generators $K_k = i\vec e_k$, the brackets read $[J_j,K_k] = 2\varepsilon_{jkl}K_l$ and $[K_j,K_k] = -2\varepsilon_{jkl}J_l$. The rotations and the boosts do not commute, and the boosts do not close: the bracket of two boost generators is a rotation generator, which is the Lie-algebraic origin of the rotor in the polar representation of a product of boosts. The two extremes are the ones where the order ceases to matter: two boosts along the same line commute, compose into a boost, and leave the rotor trivial, and a rotation about the axis of a boost commutes with it, so that the word is a single boost-rotation about that axis.

## Physical Readings

The polar form reads as the four physical factors of an element: a scale, a central phase, a boost and a rotor. Read on the clock, the central phase is the clock reading, the polar angle being the phase that the exchange rotates, and the scale is the element's norm, so the polar form is where the framework's time and its mass sit in one formula. The boost factor is available only outside the cone, which is the polar interpretation of the mass shell and the reason the polar form is not a parametrisation of everything.

The four factors are read as the **four moduli of a scattering amplitude**: the scale is the magnitude, the phase the global phase, the boost the velocity of the frame and the rotor the spin rotation, so the polar word is the amplitude-rotation decomposition a scattering computation performs. The interpretation is offered as a labelled analogy with *The S-Matrix in Biquaternionic Form* and *Thomson and Compton Scattering: The Biquaternion Polarization Algebra*, where the same four objects appear as the polarisation and phase data of a scattering process. Two further readings of the form can be named.

- **Singular-value interpretation.** The matrix image has the singular-value decomposition $\mathsf{M}_2(\tilde Q)=P\Sigma V^{\dagger}$, and the framework's polar pair is that decomposition read physically: the positive factor is the Hermitian factor, whose eigenvalues are the two singular values $\sigma_1,\sigma_2$, and the unitary factor is the rotor. The scale is the geometric mean of the singular values, $r=\sqrt{\sigma_1\sigma_2}=\sqrt{\lvert \langle\tilde Q\rangle_{\natural}\rvert}$, and the boost is their anisotropy, so a frame change decomposes into a magnitude, a phase, an anisotropy and a turn. Boundary: the boost factor exists only outside the cone, so the interpretation covers the invertible off-cone elements and not the lightlike ones.
- **Rest-frame interpretation.** The boost factor exists only outside the cone, so a lightlike element has no polar form at all: read physically, a null element has **no rest frame**, and the little group of a null direction is the $\mathrm{U}(1)$ of the helicity phase rather than the rotation group of a rest frame, which is the group-theoretic form of the same exclusion. Boundary: the absence of a rest frame for a null four-momentum is owned by *The Null Four-Momentum: What the Cone Derives and What It Does Not*, and the little group and its phase by *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*; the interpretation adds the polar-form statement of the two and no new group.

**Open question — is the scale a field or a gauge choice?** The scale $r$ multiplies the interval without entering any of the four general products as a factor of its own, so the polar form alone does not say what the scale is. **Whether it is a dynamical field, as the conformal interpretation of *Conformal Invariance and the Massless Limit in Biquaternionic Form* proposes, or a gauge choice of the local complex structure, is open**, and it is the same question as whether the local complex structure is a field or a frame (*The Local Complex Structure and the Speed of Light*).

## Summary

The polar representation of a biquaternion is $r \exp(i\alpha)B\tilde q$, and in the physics of the corpus its four factors are the scale, the central phase, the Lorentz boost and the spatial rotation. On the Lorentz group, where the biquaternion norm is one, the scale and the phase are trivial and the representation is the Cartan decomposition $\tilde{\Lambda} = \tilde{B}\tilde U$, with the positivity of the boost factor supplying the normalisation.

The modulus is $\sqrt{\det\mathsf{M}_2(\tilde{Q})}$, the scale is its modulus and the phase is half its argument, and both are invariants of the Lorentz orbit, since the determinant is multiplicative and the rotor conjugation multiplies by $\langle\tilde{\Lambda}\rangle_{\natural}\langle\tilde{\Lambda}^{*}\rangle_{\natural} = 1$. The boost factor of a four-vector is the square of the physics boost rotor in the rest-to-lab normalisation, $B = (\tilde{\Lambda}^{\natural})^2 = -(i/c)\tilde{V}$, so that rotor is the unique positive-definite square root of the representation's boost; for a four-position on a world line the scale is $c$ times the proper time and the phase is $\pi/2$, the angle that makes the time coordinate imaginary.

The rotor is the Thomas–Wigner rotation when two boosts are composed, and it is the algebraic expression of the non-closure of the boosts. The representation fails exactly on the light cone, where the determinant vanishes, the element is a zero divisor, and the four-vector has no proper length.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a biquaternion, $Q_\mu\in\mathbb{C}$ |
| $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2 = \det\mathsf{M}_2(\tilde{Q})$ | the biquaternion norm, the determinant of the $2\times2$ representative |
| $\det\mathsf{M}_4(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}^2$, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q}) = 4Q_t$ | determinant and trace of the $4\times4$ regular representative |
| $\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$ | the complex modulus |
| $r$ | the scale, $|\det\mathsf{M}_2|^{1/2}$ |
| $\exp(i\alpha)$ | the central phase, $\alpha = \tfrac12\arg\det\mathsf{M}_2$ |
| $B\in\mathbb{M}_+$ | the boost factor, Hermitian positive, $\langle B\rangle_{\natural} = 1$ |
| $\tilde q\in\mathrm{Sp}(1)\subset\mathbb{H}_{\mathbb{B}}$, $\langle\tilde q\rangle_{\natural} = 1$ | the rotor, a unit real quaternion |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$, $\vec u_{\mathrm b} = \vec v/|\vec v|$ | the physics boost rotor; for a four-position $B = (\tilde{\Lambda}^{\natural})^2 = -(i/c)\tilde{V}$ |
| $\tilde{V} = \gamma(ic\,e_t+\vec v)$ | the four-velocity |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the informational and material sectors; four-vectors live in $\mathbb{M}_-$ |
| $\tilde{Q} = ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | a four-position, interval $N = -c^2t^2+x^2+y^2+z^2$ |

## Further Reading

- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), for the Hamilton, complex and Cartan representations as the three pairings of the four factors.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for $\det\mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}$ and the matrix polar decomposition.
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_physics/the-4x4-matrix-element-representation-of-biquaternions.md`), for the squared determinant, the trace $4Q_t$ and the two chiralities.
- *The Four-Vector Element Representation of Biquaternions* (`articles_physics/the-four-vector-element-representation-of-biquaternions.md`), for the informational and material sectors, the interval and the real restrictions of the biquaternion norm.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Cartan decomposition, the non-closure of the boosts and the Thomas–Wigner rotation.
- *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* (`articles_physics/the-two-sheeted-cover-and-the-topology-of-boosts-in-biquaternionic-form.md`), for the $\pm e_t$ kernel and the sign normalisation of the rotor.
- *Spin Entropy and the Lorentz Group in Biquaternionic Form* (`articles_physics/spin-entropy-and-the-lorentz-group-in-biquaternionic-form.md`), for the interpretation of the central circle and the boost parameters as information.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the exponential $\exp(\alpha\theta)$ of each factor is classified by the rule $\nu^2 = -1, 0, +1$.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential word discussed in §*The Order of the Factors*, whose hyperbolic factor is the boost referred to the rotor-rotated axis.
