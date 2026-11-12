# __The Polar Form of the Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac equation of this corpus is one element of $\mathbb{B}$ acting on another by left multiplication. *The Dirac Equation in Biquaternionic Form* writes it as the chiral pair

$$
\tilde\nabla_\Phi\tilde\Xi_{R}=k_m\,\tilde\Xi_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=k_m\,\tilde\Xi_{R},
$$

and the same article states what the pair does not need: no column, no anticommuting array, no separate state space, no minimal left ideal, no Peirce decomposition, no chiral projector, no Clifford algebra. The field is the element, the operator is the element, and the multiplication is the algebra's own. The subscript `sp` is the corpus's caret for the spinor role, beside `scl` for the scalar role and `fop` for the field operator, as the caret table of *Algebra and Element Conventions* fixes it.

This article substitutes a parametrisation of that one element into that one equation and reads what comes out. The parametrisation is the polar word of *The Polar Decomposition of an N-Regular Biquaternion*, in the exponential form it takes in *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*:

$$
\tilde\Xi=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

The four factors are a positive real scale, a central angle, a Hermitian positive boost and a real rotor. The word has eight real parameters against the element's eight real components, and on its domain it is a bijection: it adds no object and drops no datum.

**The domain is the whole of the first qualification of this article.** In the corpus's vocabulary, an element is $N$-regular when $N\neq0$ and $N$-degenerate when $N=0$, and $N$ is the determinant (*The Meaning of N-Regularity and Degeneracy*). The word is a parametrisation of the group of units, so

$$
\boxed{\;\text{the polar word of }\tilde\Xi\text{ exists}\iff N(\tilde\Xi)\neq0\iff\tilde\Xi\text{ is }N\text{-regular},\;}
$$

and it fails on every $N$-degenerate element. There is no third case and no extension of the word to $N=0$. Every statement of this article is therefore a statement about the $N$-regular field, and a field that reaches the zero-divisor cone has no polar form at all. §*Where the Word Ends* says which fields those are and what survives there.

Two points of discipline come first, because both are ways of losing the alignment.

**The word is not a split of the field.** It is a re-coordinatisation of the element. Every factor is read from the element and the product is the element. Nothing is put into a slot.

**The word brings nothing in behind it.** No module, no ideal, no projector, no column, no state space stands behind the four factors. Whatever the word is used for, the object it parametrises is still one element of $\mathbb{B}$, and the equation it is put into is still one element acting on another.

What the article establishes is short, and each item is one sentence:

- the momentum is the gradient of the word's angle;
- the velocity is the word's boost;
- the mass is not a number in the word but the four-vector factor the boost supplies;
- the mass shell is the statement that the boost is a boost;
- the current reads the scale and the boost, the spin reads the scale and the rotor, and neither reads the angle;
- the word fails exactly on the zero divisors, and the zero divisors that matter physically are the one-sided fields.

The last item repays care, and it is stated in §*Where the Word Ends*.

## The Field and the Word

### One Element, Two Parts

The field is one element $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ of $\mathbb{B}$. It carries four complex coefficients, that is eight real numbers. The two subscripts name two parts of that one element.

They do not name two values. The value is a letter returned by one multiplication, $\tilde X\vec e_z=-i\tilde X$ for $L$ and $\tilde X\vec e_z=+i\tilde X$ for $R$, and the parent article fixes that the letters of the pair name the two **factors** of the factorisation $\tilde\Xi_{L}=\frac{i}{k_m}\tilde K_{\Phi}\tilde\Xi_{R}$ and not the two values. The polar form gives that ruling a second reason, and the reason is one of domain.

*Proposition.* Let $\tilde X\neq0$ carry a definite value, that is $\tilde X\vec e_z=-i\tilde X$ or $\tilde X\vec e_z=+i\tilde X$. Then $N(\tilde X)=0$.

*Proof.* The central $i$ passes through the element, so $\tilde X\vec e_z=-i\tilde X$ may be written $\tilde X\vec e_z+i\tilde X=\tilde X(\vec e_z+ie_t)=0$, and the other value gives $\tilde X(\vec e_z-ie_t)=0$. The element $\vec e_z\pm ie_t$ is not zero, so $\tilde X$ is a zero divisor. A zero divisor has $N=0$, because the units are exactly the elements of nonzero norm.

**What the proposition settles.** The word's domain is $N\neq0$. A part of definite value is a zero divisor, so it lies outside the domain and has no word at all. The letters therefore cannot name the two values: a split of the field into two definite-value parts would be a split into two objects on which the word is undefined. The word is stated once, for the whole element, and the two letters name its two parts.

That is the whole of the alignment, and it is one line of algebra. Nothing in it needs a subspace, an idempotent, a projector or a basis.

### The Word

The four factors and their types are those of *The Polar Decomposition of an N-Regular Biquaternion*, and this article repeats none of their theory.

| # | factor | range | type |
| --- | --- | --- | --- |
| 1 | $r$ | $r>0$ | real central scale |
| 2 | $e^{i\alpha}$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | central phase |
| 3 | $\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | $\theta_{\mathrm{rpd}}\ge0$, $\vec u_{\mathrm b}$ a real unit vector | Hermitian positive, $N=1$ |
| 4 | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}$ a real unit vector | real unit quaternion, $N=1$ |

The count closes. The scale is one real number, the angle one, the boost a rapidity and a unit axis, three, and the rotor an angle and a unit axis, three. That is $1+1+3+3=8$ against four complex coefficients.

**The boost is the square root of the frame.** Squaring it gives

$$
\tilde U_{\Psi,\mathrm b}^{2}=\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}
=\mathcal B_{\Psi}^{-1},
$$

so the exponent inside the boost is half the rapidity of the frame it produces. The rapidity $\theta_{\mathrm{rpd}}$ is the kinematic one throughout: $\gamma=\cosh\theta_{\mathrm{rpd}}$ and $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ are read from $\tilde U_{\Psi,\mathrm b}^{2}$ and never from $\tilde U_{\Psi,\mathrm b}$ itself. Every factor of two in this article comes from that square and from nowhere else.

Two factors have norm one and two are central, and that sentence carries the whole of the next section. The two norms of the word are not a property of the four factors taken together: they are the statement that two of them are units and two are central, and the split of the four into those two pairs is where the two norms come from.

### The Two Norms

*Proposition.* For $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with the factors as above,

$$
\langle\tilde\Xi\rangle_{\natural}=\rho\,e^{2i\alpha},
\qquad
\tilde\Xi\tilde\Xi^{*}=\rho\,\tilde U_{\Psi,\mathrm b}^{2},
\qquad
\langle\tilde\Xi\rangle_{*}=\gamma\rho,
\qquad
\rho=r^{2},\quad \gamma=\cosh\theta_{\mathrm{rpd}}.
$$

*Proof.* The quaternion conjugation $\natural$ acts on the $\mathbb{H}$ factor, so it leaves the central $i$ alone, inverts the real rotor and inverts the Hermitian boost. The rotor and the boost cancel against their own inverses, the central part squares, and $\langle\tilde\Xi\rangle_{\natural}=r^{2}e^{2i\alpha}$. The star conjugation is the coefficient conjugation composed with $\natural$; it fixes a Hermitian factor, conjugates the central $i$ and inverts the rotor, so the phases cancel, the rotors cancel, and $\tilde\Xi\tilde\Xi^{*}=r^{2}\tilde U_{\Psi,\mathrm b}^{2}$. Squaring the boost gives $\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$, whose scalar part is $\cosh\theta_{\mathrm{rpd}}$.

The two norms read different things, and the whole of the physics of the density is in which one is used.

| quantity | value | real? | what it reads |
| --- | --- | --- | --- |
| $\rho$ | $r^{2}$ | real, positive | the density |
| $\langle\tilde\Xi\rangle_{\natural}$ | $\rho\,e^{2i\alpha}$ | complex | the density and twice the angle |
| $\tilde\Xi\tilde\Xi^{*}$ | $\rho\,\tilde U_{\Psi,\mathrm b}^{2}$ | neither | the density and the boost |
| $\langle\tilde\Xi\rangle_{*}$ | $\gamma\rho$ | real | the density of a boosted state |

**The density is the modulus of the quaternionic norm and not the square root of the Hermitian one.** The Hermitian norm is $\gamma$ times the density, so it is the density with the motion's time dilation applied. Under a Lorentz transformation, that is $\tilde\Xi\mapsto\tilde M\tilde\Xi$ with $\tilde M$ a unit, the quaternionic norm is carried into itself, because it is central, while the Hermitian norm of the transformed field is $\operatorname{Sc}(\tilde M\tilde\Xi\tilde\Xi^{*}\tilde M^{*})$, which is not the original. That is the standard situation of a field of this type: the Hermitian square is the time component of a four-vector, and only the quaternionic norm is a scalar. The word says which of the two is the scalar, and the answer is $\rho$, the modulus of the quaternionic norm.

**The factor of two in the angle is not decoration.** The field carries $e^{i\alpha}$ and the norm carries $e^{2i\alpha}$, so every bilinear built from the norm runs at twice the rate of the field's own phase. Two consequences follow and both are used below: the density is insensitive to the sign of $\alpha$, and a superposition of two branches beats at twice the difference of their angles.

## The Equation in Polar Variables

### The Pair

The equation is the chiral pair of the introduction. For a plane wave the field is $\tilde\Xi=\tilde\Xi_{0}\exp(i\theta)$ with $\theta=\vec k_\Phi\cdot\vec r-k_{t}^{\prime}r'_t$, the gradient acts as left multiplication by $i\tilde K_{\Phi}$ and its conjugate as left multiplication by $i\tilde K_{\Phi}^{\natural}$, and the pair becomes the momentum-space system

$$
i\tilde K_{\Phi}\tilde\Xi_{0}^{R}=k_m\tilde\Xi_{0}^{L},
\qquad
i\tilde K_{\Phi}^{\natural}\tilde\Xi_{0}^{L}=k_m\tilde\Xi_{0}^{R},
\qquad
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2},
$$

which the parent derives. Nothing in this section is new: the three relations are the parent's, and the polar form says only what the quantities in them are.

### The Logarithmic Derivative

Substituting the word into a first-order equation means differentiating it, and the derivative separates into four terms with no remainder.

*Proposition.* For $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$,

$$
\frac{\partial\tilde\Xi}{\partial R_\mu}
=\tilde\Xi\left[\frac{1}{2}\frac{\partial\ln\rho}{\partial R_\mu}
+i\frac{\partial\alpha}{\partial R_\mu}
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu}\right].
$$

*Proof.* Differentiate the product and divide by it. The two central factors give the first two brackets. The derivative of the boost is $\tilde U_{\Psi,\mathrm b}(\tilde U_{\Psi,\mathrm b}^{-1}\partial\tilde U_{\Psi,\mathrm b})$ and the derivative of the rotor is $\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}(\tilde u_{\mathrm r}^{-1}\partial\tilde u_{\mathrm r})$; the boost cancels against itself in the first and passes the rotor in the second, which gives the two frame terms as written.

The four brackets are of four different types, and that is the content of the display.

| term | type | zero when |
| --- | --- | --- |
| $\tfrac12\partial_\mu\ln\rho$ | real central scalar | the density is constant |
| $i\partial_\mu\alpha$ | central imaginary | the angle is constant |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the boost is constant |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | the rotor is constant |

A plane wave is the case in which the last three vanish: the frame is constant and the density is constant, so the derivative is the phase term alone. Then $\partial_\mu\tilde\Xi=i(\partial_\mu\alpha)\tilde\Xi$, and the equation becomes algebraic in the frame. That is why a plane wave can be solved exactly and why the general case cannot be read off it.

Note what the first bracket is not. The scale enters the derivative only through $\ln\rho$, so a constant density contributes nothing and a field of uniform density carries no scale term at all. The scale is a multiplier, not a source.

### The Phase Gradient Is the Four-Momentum

The second bracket is the momentum, and the algebra states it without a rule. Since $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$ on the material sector,

$$
\tilde\nabla_\Phi\alpha
=e_t\frac{\partial\alpha}{\partial R_t}+\sum_\eta\vec e_\eta\frac{\partial\alpha}{\partial R_\eta}
=-i\frac{\partial\alpha}{\partial r'_t}e_t+\nabla\alpha
=i\frac{E}{\hbar c}e_t+\frac{\vec p}{\hbar}
=\tilde K_{\Phi},
$$

with $\vec p=\hbar\nabla\alpha$ and $E=-\hbar c\,\partial\alpha/\partial r'_t$. The temporal slot of the gradient is $-i\partial\alpha/\partial r'_t$ and the temporal slot of the wavevector is $iE/(\hbar c)$, so the two match slot by slot and no factor is inserted by hand. The factor $c$ is the algebra's own statement: $r'_t$ is a length, so a derivative in $r'_t$ is a rate over a length, and an energy is a rate times an action.

The reading is exact for a plane wave, where the angle is linear and the gradient is the wavevector. For a general field it is the eikonal reading, and it defines the momentum at each event. The proof uses only that the angle is real and that the gradient is the algebra's derivative, so it applies to a general field unchanged.

### The Boost Is the Four-Velocity

The third factor is the velocity.

*Proposition.* With $\tilde U_{\Psi,\mathrm b}$ the word's boost,

$$
\tilde V_{\Phi}=ic\,\tilde U_{\Psi,\mathrm b}^{-2}=\gamma\bigl(ic\,e_t+\vec v\bigr),
\qquad
\tilde P_{\Phi}=imc\,\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
\qquad
\gamma=\cosh\theta_{\mathrm{rpd}}.
$$

*Proof.* Squaring the boost gives $\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$, so its inverse is $\cosh\theta_{\mathrm{rpd}}\,e_t-i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$. Multiplying by $ic$ gives $ic\cosh\theta_{\mathrm{rpd}}+c\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$, which is $\gamma(ic\,e_t+\vec v)$ with the two identifications written.

The inverse square is not decoration. The velocity of this field is bilinear in the field, so the frame appears in it twice: once in the boost the word deposits, and once again when the four-vector is formed. The conventions name that factor $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$ and record the factor of two as the commonest error in the corpus (*Norm and Pairing Conventions*, §*The Four Objects Called a Boost*). A reader who takes the frame for the velocity finds a four-velocity of half the rapidity.

The norm of the velocity is the unit of the algebra times $-c^{2}$, in one line,

$$
\langle\tilde V_{\Phi}\rangle_{\natural}=i^{2}c^{2}\,\tilde U_{\Psi,\mathrm b}^{-2}\tilde U_{\Psi,\mathrm b}^{2}=-c^{2},
$$

because the natural conjugation inverts a unit. The four-velocity of the word is therefore a unit timelike element for every field, not only for a plane wave: the boost is a unit by construction and the density is a separate factor.

### The Mass Term Is the Four-Vector Factor

The mass term of the pair is off-diagonal in the parts, and in polar variables the operator that relates the parts is not a number. Substituting $\tilde K_{\Phi}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ into the first line of the momentum-space system gives

$$
\boxed{\;\tilde\Xi_{0}^{L}=-\mathcal B_{\Psi}\,\tilde\Xi_{0}^{R},
\qquad \mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}\;}
$$

and the second line is then satisfied identically, since $i\tilde K_{\Phi}^{\natural}\tilde\Xi_{0}^{L}=i\,ik_m\tilde U_{\Psi,\mathrm b}^{2}(-\mathcal B_{\Psi}\tilde\Xi_{0}^{R})=k_m\tilde\Xi_{0}^{R}$, the natural conjugation leaving the central $i$ alone and inverting a unit.

**What the display says.** The relation between the two parts carries no $k_m$. The scalar cancels against the momentum it multiplies, and what is left is the frame factor, $\tilde\Xi_{0}^{L}=-\mathcal B_{\Psi}\tilde\Xi_{0}^{R}$. In this chart the mass term is an operator on the parts and not a number written in front of them, and the operator is the four-vector factor that the velocity also carries.

**The scale is not lost with it.** It sits in the momentum, $\tilde K_{\Phi}=ik_m\mathcal B_{\Psi}$, and $\mathcal B_{\Psi}$ has unit natural norm, so $k_m$ is exactly the norm of $\tilde K_{\Phi}$ and nothing besides. The two readings are one identity: the coefficient and the frame factor are interchangeable because the frame factor carries no amplitude.

**The standard reading, and what this adds.** In the standard Dirac theory the mass is a scalar coupling the two chiral parts, and the coupling is the same in every frame because the scalar is invariant. Nothing here denies that. What the chart adds is where the scalar goes in a moving frame: the rest-frame sign is carried along by the boost, and the momentum already carries the same boost, so the pair relation divides it out. The sentence that the mass **is** a frame factor is a statement about the chart and not a claim that the mass depends on the frame. The strongest objection is exactly that one, that a frame factor would make an invariant frame-dependent, and the answer is the norm: $\mathcal B_{\Psi}$ contributes no scale, and the scale is $k_m$, which no boost touches.

**At rest the factor is the identity.** With $\theta_{\mathrm{rpd}}=0$ the boost is $e_t$, the factor is $e_t$, and the relation reduces to the plain sign $\tilde\Xi_{0}^{L}=-\tilde\Xi_{0}^{R}$. The whole of the mass term's structure is then the sign, and the whole of its motion dependence is the boost.

**Why the four-vector factor and not the frame.** The word's frame factor is the boost $\tilde U_{\Psi,\mathrm b}$ and the mass term needs $\tilde U_{\Psi,\mathrm b}^{-2}$. The reason is the one given with the word. The boost $\tilde U_{\Psi,\mathrm b}$ is the square root of $\mathcal B_{\Psi}$, and $\mathcal B_{\Psi}$ is the element that carries the time axis to the four-velocity, $\tilde V_{\Phi}=\mathcal B_{\Psi}\,(ic\,e_t)$. A four-vector is bilinear in the field and so carries $\mathcal B_{\Psi}$ and not its square root; the mass relates two parts of the field and carries the same $\mathcal B_{\Psi}$ as the velocity.

### The Mass Shell, Read as the Frame's Unitarity

The third relation of the momentum-space system is the dispersion relation, and in the word it is not an independent equation.

*Proposition.* Let $\tilde K_{\Phi}=ik_m\tilde M$ with $N(\tilde M)=1$. Then $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$. Conversely, every $\tilde K_{\Phi}$ with $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$ is of that form, with $\tilde M=\tilde K_{\Phi}/(ik_m)$.

*Proof.* For the first part, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=i^{2}k_m^{2}\tilde M\tilde M^{\natural}=-k_m^{2}$, the natural conjugation leaving the central $i$ alone. For the second, $N\bigl(\tilde K_{\Phi}/(ik_m)\bigr)=\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}/(-k_m^{2})=e_t$.

**What the proposition says.** The mass shell is the statement that the four-wavevector divided by $k_m$ is a unit element, that is, the image of the time axis under a Lorentz transformation. In the word, with $\tilde K_{\Phi}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$, it holds identically.

**The strongest objection.** The proposition is a restatement and not a result. Its hypothesis defines $\tilde K_{\Phi}$ as $ik_m$ times a unit, so the two halves of the hypothesis are the same half, and the conclusion repeats the definition. The objection is correct, and the article claims no more than the identity: what the proposition fixes is the direction of the reading, since the same line can be read from the momentum to the frame or from the frame to the momentum.

**What is standard in it.** The geometric content is the textbook one. The normalized four-momentum $\tilde P_{\Phi}/(mc)$ is a point of the unit hyperboloid, that hyperboloid is the Lorentz orbit of the time axis, and in the spinor language the orbit is the space of boosts. The corpus names a point of that orbit by an element of the algebra. The naming is its own and the orbit is not.

That is why the plane-wave system closes. The relation $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$ looks like a fourth equation on the same data and is not one; it is the statement that the boost in the word is a boost. A reader who counts four relations against three frame parameters has found the identity just written.

### What the General Field Leaves Open

The four brackets of the logarithmic derivative are fixed in a plane wave and free in a general field, and the polar form does not close the general case by itself.

The reason is structural. The pair relates two parts by a central coefficient, and the word is one word for the whole element. Substituting it produces a coupled system for the four brackets, with no canonical rule that fixes one bracket from another. What the polar form settles is therefore the plane-wave case exactly and the general case partially. Exactly: the momentum is the phase gradient, the velocity is the boost, the mass is the four-vector factor, the mass shell is the frame's unitarity. Partially: the density and the two frame directions are what the equation constrains, and the connection terms are what a general solution supplies.

The scalar companion closes its general case because there the equation is second order in one central function and separates into two real equations. Here the equation is first order in an element, and the separation into four brackets is the closest the algebra comes to a closed system.

## The Current and the Spin

### The Current Is the Density Times the Velocity

The current of the field is the density times the four-velocity of the word,

$$
\boxed{\;\tilde J_{\Phi}=\rho\,\tilde V_{\Phi}=ic\gamma\rho\,e_t+\rho\gamma\vec v\;}
$$

and the display contains four of the eight parameters. The density multiplies and the boost supplies the rapidity and the direction. The angle is absent, and the rotor is absent as well.

The temporal slot is the charge density and the spatial part is the current density. The current is therefore not an independent object: the word already carries the velocity, and the current is the density times it.

### The Bilinear That Is Not the Current

The obvious candidate for the current is the algebra's own bilinear $i\tilde\Xi\tilde\Xi^{*}$, which is invariant under the central phase. The word evaluates it in one line. By the norm proposition $\tilde\Xi\tilde\Xi^{*}=\rho\tilde U_{\Psi,\mathrm b}^{2}$, so

$$
i\tilde\Xi\tilde\Xi^{*}=i\rho\bigl(\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}\bigr)
=\rho\bigl(i\cosh\theta_{\mathrm{rpd}}\,e_t-\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}\bigr).
$$

Compare the two displays term by term. The temporal slots agree in sign. The spatial parts are opposite. The bilinear is the current of the mirror image of the motion, up to the factor $c$ that the four-velocity carries and the product of the field does not.

**Why the sign is reversed, in one line.** The star conjugation fixes the boost and inverts the rotor, so applied to the field it leaves the boost in place and cancels the rotor; the bilinear therefore carries the velocity twice and the spin not at all. The outer factor $i$ then reverses the spatial part, because a real spatial vector times $i$ is imaginary while the temporal slot is already imaginary.

The current needs the velocity once and a fixed timelike direction once, and the fixed direction is the odd element the even algebra does not contain. That is the polar form of the negative result of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, where the non-conservation of $i\tilde\Xi\tilde\Xi^{*}$ is exhibited on an exact solution and the conserved current is left open. The word says why: the algebra's product of the field with its conjugate cancels the frame, and a current is a frame.

Nothing here denies that the standard theory has a conserved current. It says which object of the algebra is it, and the answer is: none, without the odd element. The current of the standard theory is $\rho\tilde V_{\Phi}$, and the word displays it as the density times a frame factor.

### The Spin Is the Density Times the Rotor

The spin is carried by the rotor, in the same way that the current is carried by the boost:

$$
\tilde S_{\Psi,\mathrm{sp}}=\rho\,\frac{\hbar}{2}\,i\,\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\,\vec e_z\,\tilde u_{\mathrm r}^{\natural},
\qquad
\hat s^{2}=-e_t.
$$

The direction is the image of the declared axis under the rotor, and $\hat s$ is a real unit vector because the rotor is real and unitary: $\hat s^{2}=\tilde u_{\mathrm r}\vec e_z^{2}\tilde u_{\mathrm r}^{-1}=-e_t$. The magnitude is the one spin of the field, the density multiplies, and the central $i$ puts the element in the Hermitian sector.

**The axis is not a new choice.** The direction $\vec e_z$ is the frame's third direction and it is already declared: it is the direction the value test uses, $\tilde X\vec e_z=\pm i\tilde X$. The spin therefore costs no declaration the equation did not already make, and this is the honest answer to the objection that a spin axis singles out a direction the physics does not contain. The algebra declares one direction in order to read the value; the spin is the image of that same direction under the field's own rotor. What is physical is $\hat s$, and $\hat s$ is not $\vec e_z$: it is where the field has carried it.

**The spin is a direction and not a plane.** The element is a multiple of one real unit vector. A reader who expects the word to carry the spin plane will not find it there: the plane is what the algebra supplies once the vector is named, and it is the same plane for every field. What the word carries is which direction in that plane is the field's.

### What the Frame Separates

Three absences are exact and they are the point of the section. The angle $\alpha$ is absent from the current and from the spin. The boost is absent from the spin, because a boost does not change a direction transverse to itself in the rest frame, and the word respects that by putting the spin in the factor the boost leaves alone. The rotor is absent from the current, because a rotation does not change a velocity.

So the frame separates the eight parameters into two triples with a shared scale:

| observable | reads | does not read |
| --- | --- | --- |
| $\tilde J_{\Phi}$ | $\rho$, $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | $\alpha$, $\theta$, $\vec u_{\mathrm r}$ |
| $\tilde S_{\Psi,\mathrm{sp}}$ | $\rho$, $\theta$, $\vec u_{\mathrm r}$ | $\alpha$, $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ |
| $\langle\tilde\Xi\rangle_{\natural}$ | $\rho$, $2\alpha$ | the two frames |

The angle therefore lives in exactly one place, the argument of the quaternionic norm. Nothing in the current and nothing in the spin reads it, which is why the angle can be moved between the factors of the word without consequence. That is the precise sense in which the field carries an angle no bilinear of the algebra sees.

## Where the Word Ends

### The Cone

The word exists where $\langle\tilde\Xi\rangle_{\natural}\neq0$ and nowhere else; in the qualified vocabulary of the corpus, that is the $N$-regular set and nothing else. The condition is one complex equation on eight real components, so its zero set has real dimension six: the word's domain is the complement of a real hypersurface of codimension two, and the excluded set is the whole of the $N$-degenerate sector.

On that set every factor fails together. $\rho=0$, so there is no scale; the boost and the rotor are read by dividing by $\rho$, so there is neither; and the angle is the argument of zero, so there is no angle. The failure is not one parameter running out. It is the chart ceasing to apply.

### The One-Sided Fields

The $N$-degenerate set would be a curiosity if nothing physical lay on it. Two families do, and both take one line. They are the Dirac fields for which the polar form does not exist.

**A part of definite value.** By the proposition of §*One Element, Two Parts*, an element with $\tilde X\vec e_z=\pm i\tilde X$ is a zero divisor and has $N=0$. A definite-value part therefore lies on the cone at every amplitude and at every point of space and time.

**A plane-wave part.** A one-sided plane wave satisfies $\tilde K_{\Phi}\tilde\Xi_{0}=0$ with $\tilde K_{\Phi}$ null, and then $\tilde\Xi_{0}$ is a zero divisor, so $N(\tilde\Xi_{0})=0$. The argument is the same line: a nonzero element annihilated by a nonzero element is a zero divisor, and the zero divisors are the elements of vanishing norm.

**Why this is not the nodal set.** For a central field the two sets coincide: with $B^{2}=0$ identically, $\langle\tilde\Xi\rangle_{\natural}=A^{2}e^{2i\theta}$ and the norm vanishes exactly where the amplitude does. Here they separate, and the separation is the whole difference between the scalar companion and this article. A one-sided plane wave is nowhere zero and has $N=0$ everywhere, so the word fails on a field of uniform, nonzero density. The failure is a failure of the chart's range and not of the field's size.

### What the Failure Does Not Mean

Three statements are worth separating, because they are easily run together.

**The field is not zero.** $N=0$ says nothing about the density. Measured on the cone, the Hermitian norm $\operatorname{Sc}(\tilde\Xi\tilde\Xi^{*})$ is positive and of order one. What vanishes is the quaternionic norm, and with it the scale of the word.

**Masslessness does not put the field on the cone.** The pieces of a massless field are one-sided, and each piece is a zero divisor. The sum generally is not: with the two pieces taken from the two kernels of the gradient, the sum is a unit and the cross term is what carries the nonzero norm. A massless field with both parts therefore has a polar word, and a one-sided field has none. The word's failure tracks the parts of the field and not its mass. This is the same cross term that *The Hamilton Pairing* records in the mass of a sum, seen from the side of the domain.

**The equation does not stop.** What fails is the parametrisation and not the physics. The pair, the current and the spin are equations on the element and need no word. What is lost is the reading of the element in eight named coordinates.

### What Survives on the Cone

A two-factor decomposition survives, and it is worth a paragraph because it is often mistaken for the word's failure.

Every element factors as $\tilde\Xi=\tilde\Xi_{H}\tilde\Xi_{0}$ with $\tilde\Xi_{H}$ Hermitian positive semidefinite and $\tilde\Xi_{0}$ a partial isometry; off the cone the second factor is unitary and on the cone it is not. The Hermitian factor loses rank and the isometry loses unitarity, and the two statements are one statement. This is the matrix polar decomposition, and it is defined on every element (*The Polar Decomposition of an N-Degenerate Biquaternion*).

So the contrast is not that the word exists off the cone and nothing exists on it. It is that the two-factor decomposition is available always and the four-factor word only on the units, because the word is a parametrisation of the group of units. The two answer different questions — *what is this element, as a positive factor times an isometry* against *which unit is this* — and only the second needs a unit.

### The Boundary Value

The word has boundary values on the cone. A family with $r=Re^{-\psi/2}$ and boost rapidity $\theta_{\mathrm{rpd}}=\psi$ has a limit as $\psi\to\infty$, and the limit is nonzero: the collapsing scale and the diverging boost cancel, leaving the direction $e_t+i\vec u_{\mathrm b}$ of the boost. The stratum the limit reaches is decided by the rotor: the idempotent stratum where the scalar part of the limit is nonzero, the nilpotent stratum where it vanishes (*The Massless Limit as a Boundary Value of the Polar Word*).

Two things follow, and the second is the important one. The element has a limit, so the cone is reachable and the degenerate case is a boundary of the same theory and not a different one. The generator has no limit, and the limit is path-dependent, so the boundary value is not a value of the word: it is what the word does when its domain is exhausted.

## The Non-Relativistic Limit

### The Rest Phase

A slow state is one whose boost is small and whose angle is dominated by the rest phase. Write

$$
\alpha=-k_m r'_t+\sigma,
\qquad
k_m r'_t=\frac{mc^{2}}{\hbar}\,t,
$$

so that the field's own phase advances at $mc^{2}/\hbar$ and the norm's angle at $2mc^{2}/\hbar$. The angle is a number of radians and not an energy; $\hbar$ is what makes it so, and the same $\hbar$ makes $\sigma$ dimensionless.

**The factor of two is the whole of zitterbewegung.** The trembling of a state of this kind is a bilinear effect: the density and the current oscillate, and every bilinear is built from the norm, whose angle is twice the field's. The trembling frequency is therefore twice the rest frequency, $2mc^{2}/\hbar$, and no further computation is needed to see why. The numbers are the standard ones: $1.55269\times10^{21}\ \mathrm{rad\,s^{-1}}$ for the rest frequency and $193.1\ \mathrm{fm}$ for half the reduced Compton wavelength.

What the polar form adds is the location. The frame is untouched by the trembling: a single branch has a constant boost and a constant rotor, and the oscillation appears only when two branches are superposed. A reader who expects the frame to rotate at the trembling frequency will not find it rotating there.

### The Frame Loses Its Boost

At small rapidity the boost departs from the identity at first order,

$$
\tilde U_{\Psi,\mathrm b}=e_t+\frac{\theta_{\mathrm{rpd}}}{2}\,i\vec u_{\mathrm b}+\cdots,
\qquad
\tilde V_{\Phi}=ic\,e_t+\vec v+\cdots,
$$

so the word becomes $r\,e^{i\alpha}\tilde u_{\mathrm r}$: a scale, a phase and a rotor. That is the non-relativistic word, and it is the whole polar content of the two-component description.

The velocity's first correction is second order, since $\cosh\theta_{\mathrm{rpd}}=1+\theta_{\mathrm{rpd}}^{2}/2$ and $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}=c\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$; the temporal slot therefore departs from $ic$ at order $\theta_{\mathrm{rpd}}^{2}/2$, which is the kinetic energy over $mc^{2}$. The boost is the relativistic correction and the rotor is the part that survives at every speed.

The mass term follows the same pattern. In the word its factor is $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$, and at small rapidity $\mathcal B_{\Psi}=e_t-i\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}+\cdots$, so the relation becomes $\tilde\Xi_{0}^{L}=-\tilde\Xi_{0}^{R}$ at leading order and the corrections are the boost. The limit keeps its leading term.

### The Rotor Precesses

The rotor is the spin frame, so the spin's motion is the rotor's motion. In a magnetic field the rotor's angle advances at the Larmor rate, and the rate carries $g=2$, because the same frame factor that carries the velocity also carries the magnetic coupling. The identification is that of *The Classical Origin of $g=2$ in Biquaternionic Form*, and the eikonal and transport equations that accompany it are those of *Relativistic Mechanics from the Dirac Wave*, where the spin term is located at order one and not at order zero.

The polar form states the same ordering in one sentence. The current is the scale and the boost, the spin is the scale and the rotor, and the eikonal is the phase, which is central. A central element commutes with the spin frame, so the leading order cannot act on the spin: the spin cannot enter at leading order for the reason that the leading order is central.

## What the Polar Form Does and Does Not Add

The objection has to be stated before it is answered. The decomposition is not new. It is the Yvon–Takabayasi–Hestenes decomposition of a field of this type into a density, an angle and a Lorentz frame, and the split of the frame into a boost and a rotation is the polar decomposition of a Lorentz transformation. No solution is added and no number changes.

Four things are nevertheless not a relabelling.

**The two norms are separated and the density is identified.** $\langle\tilde\Xi\rangle_{\natural}=\rho e^{2i\alpha}$ and $\langle\tilde\Xi\rangle_{*}=\gamma\rho$ are two different objects, and for a central field they coincide. The identification of $\rho$ as the modulus of the quaternionic norm, and of the Hermitian norm as its time-dilated image, is a statement about which quantity a density is built from.

**The count closes.** Eight slots against eight components, with a bijection and no spare parameter. A decomposition whose parameters can vary is a description of the field; one whose parameters cannot is a description of a subspace.

**The equation's content is named.** The momentum is the phase gradient, the velocity is the boost, the mass term is the four-vector factor with its scale in $k_m$, and the mass shell is the frame's unitarity. The last is the sharpest: the solvability condition on the momentum is the statement that the boost is a boost. Each of the four is a reading of the chart and not a new equation, and the chart's domain is the $N$-regular field.

**The failing bilinear is explained in one line.** The algebra's $i\tilde\Xi\tilde\Xi^{*}$ is the current with its direction reversed, because the star conjugation fixes the boost and cancels the rotor. That is a fact about the two conjugations, and it is why the conserved current needs the odd element.

What the polar form does **not** add is the point of this article. It adjoins no object: no column, no array, no module, no ideal, no projector, no state space, no basis. The field was one element and the word is a parametrisation of it, so the equation is exactly the parent's equation and nothing is carried in behind the four factors. The only thing the polar form adds is a qualification, and the qualification is one condition: every statement of this article holds for the $N$-regular field and for no other.

## Open Questions

1. **The conserved current.** The current the word supplies is $\rho\tilde V_{\Phi}$, and the algebra's own bilinear is its mirror image. Which object of the algebra is conserved on solutions remains open, as the minimal-coupling article records. The polar form explains the failure and does not repair it.

2. **The angle's status.** The angle is read by no bilinear, and it is a gauge angle under the central phase symmetry. Whether it is observable through an interference of two branches, where the norm's argument enters the beat, is not settled here.

3. **The connection terms.** The logarithmic derivative carries a boost connection and a rotor connection. Whether their combination has a geometric reading — a connection on the frame bundle of the algebra, with the mass term as curvature — is not attempted here.

4. **The two-sided form.** The parent writes a second form of the equation in which the mass acts on the right, $\tilde\Xi_{R}\mapsto\tilde\Xi_{R}\,i\vec v$, and the letters then name the two values. What the polar form is in that display is not written. There the two parts are on the cone by the proposition of §*One Element, Two Parts*, so the word would be stated for the sum and not for the parts, and the reading of the frame in that display is open.

5. **The general field.** The four brackets are constrained by the pair but not closed by it. Whether a second structure — a transport equation for the rotor, of the kind the classical-spin literature carries — closes them is not settled.

## Summary

The polar form of the Dirac field of this corpus is $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$ the scale, $\alpha$ the central angle, $\tilde U_{\Psi,\mathrm b}$ a Hermitian positive boost and $\tilde u_{\mathrm r}$ a real rotor. The parameters are eight and the components are eight, so the word is a bijection, and its domain is the $N$-regular set: the polar form exists exactly where $N\neq0$ and fails on every $N$-degenerate field.

The field is one element and the two letters of the pair name its two parts. They are not two values, and the polar form gives the reason: an element of definite value satisfies $\tilde X(\vec e_z\pm ie_t)=0$, so it is a zero divisor and has $N=0$, which places it outside the word's domain. A split into definite-value parts would be a split into two objects on which the word is undefined.

The two norms separate. The quaternionic norm is $\langle\tilde\Xi\rangle_{\natural}=\rho e^{2i\alpha}$ and the Hermitian norm is $\langle\tilde\Xi\rangle_{*}=\gamma\rho$, the difference being that the star conjugation fixes the Hermitian boost while the natural conjugation inverts it and leaves the central $i$ alone. The density is the modulus of the first and it is the Lorentz scalar; the Hermitian norm is its time-dilated image. The norm's argument is twice the word's angle, and the doubling is the factor of two behind zitterbewegung.

The derivative of the word separates into four brackets: a scale term, a phase term, a boost connection and a rotor connection. The phase term is the four-momentum, $\tilde\nabla_\Phi\alpha=\tilde K_{\Phi}$; the boost is the four-velocity, $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic\,e_t+\vec v)$ with $\vec v=c\tanh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ and $\gamma=\cosh\theta_{\mathrm{rpd}}$. The inverse square appears because a four-vector is bilinear in the field. Its natural norm is $-c^{2}$, so the word's velocity is a unit timelike element for every field.

The mass term is a frame factor, and its scale is the scalar $k_m$. In polar variables the pair reads $\tilde\Xi_{0}^{L}=-\mathcal B_{\Psi}\tilde\Xi_{0}^{R}$ with $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$, because $k_m$ cancels against the momentum it multiplies; at rest the factor is the identity and the relation is the plain sign. The factor has unit norm, so the scalar reappears in the mass shell, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$, which is the frame's unitarity and not a fourth equation. Both sentences are readings of the chart, and the invariant is $k_m$.

The current is $\tilde J_{\Phi}=\rho\tilde V_{\Phi}$ and the spin is $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ with $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, where $\vec e_z$ is the frame's third direction, already declared by the value test and not a new choice. The current reads the scale and the boost, the spin reads the scale and the rotor, and neither reads the angle.

The word fails on the zero divisors and nowhere else, that is on the $N$-degenerate elements and on no others. Two families lie there: the parts of definite value, and the one-sided plane waves, each by the one line that a nonzero element annihilated by, or annihilating, a nonzero element is a zero divisor. This is not the nodal set: a one-sided plane wave is nowhere zero and has $N=0$ everywhere. Masslessness does not put the field on the cone, because the sum of two one-sided parts is generally a unit and the cross term carries the norm. What survives on the cone is the two-factor decomposition, not the four-factor word.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$; $\vec e_z$ is the frame's third direction |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ | The field, one element of $\mathbb{B}$; the letters name the two parts |
| $\tilde\nabla_\Phi,\ (\tilde\nabla_\Phi)^{\natural}$ | Biquaternionic gradient and its quaternion conjugate, $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$ |
| $\tilde R_\Phi=i r'_te_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ | Four-position |
| $r'_t=c\,t^{\prime}$ | Material time, a length |
| $k_m=mc/\hbar$ | Mass wave number; the reciprocal reduced Compton length |
| $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word |
| $r>0$, $\rho=r^{2}$ | Scale and density; real and central |
| $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | The word's angle; the norm's argument is $2\alpha$ |
| $\tilde U_{\Psi,\mathrm b}=\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ | Boost; Hermitian positive, $N=1$; rapidity $\theta_{\mathrm{rpd}}\ge0$, unit axis $\vec u_{\mathrm b}$; $\tilde U_{\Psi,\mathrm b}^{2}=\mathcal B_{\Psi}^{-1}$ |
| $\tilde u_{\mathrm r}$ | Rotor; real unit quaternion, $N=1$; angle $\theta$, unit axis $\vec u_{\mathrm r}$ |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; on the field $\rho e^{2i\alpha}$ |
| $\langle\tilde Q\rangle_{*}=\operatorname{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm; on the field $\gamma\rho$ |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor of the frame |
| $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ | Velocity of the frame |
| $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-vector factor; $\cosh\theta_{\mathrm{rpd}}\,e_t-i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ |
| $\tilde V_{\Phi}=ic\,\mathcal B_{\Psi}$ | Four-velocity of the word; $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ |
| $\tilde P_{\Phi}=imc\,\mathcal B_{\Psi}$, $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=\tilde\nabla_\Phi\alpha$ | Four-momentum and four-wavevector; $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$ |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, $\hat s^{2}=-e_t$ | Spin direction |
| $\tilde J_{\Phi}=\rho\tilde V_{\Phi}$ | Current |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | Spin element |
| $i\tilde\Xi\tilde\Xi^{*}=\rho(i\cosh\theta_{\mathrm{rpd}}e_t-\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b})$ | The bilinear that is the mirror of the current |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | Norm; zero exactly on the zero divisors |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the eight-parameter polar variables of the spin-$\tfrac12$ field, which this article reads as the word of the algebra. The scalar companion's pair is the spin-$0$ case of the same programme.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the decomposition of the field into density, angle and rotor, and for the reading of the Dirac equation as a condition on that rotor.
- Jacques Yvon, "Équations matricielles du champ spinoriel," *Journal de Physique et le Radium* **1** (1940) 18–26, for the bilinears whose argument is the angle this article writes $2\alpha$.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic polar variables, the spin transport they carry, and the difficulties recorded in §*Open Questions*.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac equation, its current and the structure the pair reproduces.
- Claude Daviau, "Équations de Dirac et de Maxwell en algèbre de Clifford," *Annales de la Fondation Louis de Broglie* **39** (2014), for a field read as an element with eight real parameters, which is the count this article uses.
