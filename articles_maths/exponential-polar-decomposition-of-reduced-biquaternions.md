# __Exponential Polar Decomposition of Reduced Biquaternions__

## Introduction

This article treats the **exponential polar decomposition** of a unit of the reduced biquaternion algebra: the writing

$$
\breve Q=\exp\breve Q_{\log},
$$

with $\breve Q_{\log}$ the **exponent**, a logarithm of $\breve Q$. The element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$, and its two **circular components** are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$. The exponent is an element of the algebra,

$$
\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown},
\qquad Q_{\log\blacktriangle},Q_{\log\blacktriangledown}\in\mathbb{C},
$$

and its two complex coefficients carry four real components,

$$
Q_{\log\blacktriangle}=\ln\rho+i\alpha,\qquad
Q_{\log\blacktriangledown}=\phi+i\beta,
\qquad \rho>0,\quad \phi,\alpha,\beta\in\mathbb{R}.
$$

The exponent is the sum of the **logarithm of the modulus** and the **angle**:

$$
\breve Q_{\log}=\breve r_{\log}+i\Theta,
\qquad
\breve r_{\log}=\ln\rho+j\phi\in\mathbb{R}\{1,j\},
\qquad
i\Theta=i\alpha+ij\beta\in\mathbb{R}\{i,ij\}.
$$

The modulus is $\breve r=\exp(\breve r_{\log})=\rho(\cosh\phi+j\sinh\phi)$, an element of the cone $P=\{x+jy:x>\lvert y\rvert\}$, and the unit factor is $u=\exp(i\Theta)=e^{i\alpha}e^{ij\beta}$, a point of the torus $T^2=\{u:u\bar u=1\}$. The decomposition is the exponential form of the modulus–unit decomposition $\breve Q=\breve r u$ of *Modulus–Unit Polar Decomposition of Reduced Biquaternions*. Because the algebra is commutative, the two factors are one exponential.

The exponential is computed by the closed form

$$
\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})
=e^{Q_{\log\blacktriangle}}\bigl(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown}\bigr),
$$

and it is a homomorphism from the additive group of the algebra onto the unit group. Every unit has a logarithm, because its two circular components $Q_{+}$ and $Q_{-}$ are non-zero and each has a complex logarithm. The logarithm is not unique: the kernel is the rank-two lattice $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$, and the ambiguity is one integer for each circular component. The principal domain, the product of the real lines $\ln\rho\in\mathbb{R}$ and $\phi\in\mathbb{R}$ with the diamond $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$, is a fundamental domain, and on it the exponential is a bijection onto the unit group.

The exponential form is the transcendental member of the three polar decompositions. The modulus–unit form is global and algebraic, the rational-chart form is rational and local, and the exponential form is global and transcendental, with the group law equal to addition. The comparison is made in §*The Three Polar Decompositions*.

**Conventions.** The algebra is $\mathbb{B}_{\mathrm{r}}$, with basis $1,i,j,ij$, $i^{2}=-1$, $j^{2}=+1$ and $ij=ji$. The element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$; the coefficient $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ is the **scalar part** and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ the **split part**. The **circular components** are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$.

The bar is $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$, the reduced norm is $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$, and the squared Euclidean norm is $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$. The **modulus** is $\breve r=\sqrt{\breve Q\bar{\breve Q}}=\rho(\cosh\phi+j\sinh\phi)$ in $P$, with $\rho>0$, $\phi\in\mathbb{R}$ and circular-component scales $\rho_{\pm}=\lvert Q_{\pm}\rvert=\rho e^{\pm\phi}$. The **unit factor** is $u=\breve r^{-1}\breve Q=e^{i\alpha}e^{ij\beta}$ in $T^2$. The **exponent** is $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ with $Q_{\log\blacktriangle}=\ln\rho+i\alpha$ and $Q_{\log\blacktriangledown}=\phi+i\beta$; its scale part is $\breve r_{\log}=\ln\rho+j\phi$ and its angle part is $i\Theta=i\alpha+ij\beta$. The **group of units** is $\mathbb{B}_{\mathrm{r}}^{\times}$.

**Boundaries.** The modulus, the torus and the uniqueness of the modulus–unit pair are treated in *Modulus–Unit Polar Decomposition of Reduced Biquaternions*; the rational coordinate on the torus is treated in *Rational-Chart Polar Decomposition of Reduced Biquaternions*; the group of units is treated in *The Group of Units of the Algebra of the Reduced Biquaternions*; the exponential and the logarithm as elementary functions are treated in *Reduced Biquaternion Elementary Functions*; the kernel, the covering and the Lie group structure are treated in *Reduced Biquaternion Lie Group and Exponential Structure*. The complex member is *Exponential Polar Decomposition of Complex Numbers*, the split-complex member is *Exponential Polar Decomposition of Split-Complex Numbers*, and the noncommutative counterpart is *Exponential Polar Decomposition of Biquaternions*.

The plan is as follows. The element, the exponent and the four components are defined (§*The Data*), the two factors are read from them (§*The Two Factors*), the single exponential and the group law are recorded (§*One Exponential*, §*The Group Law*), existence and uniqueness are proved (§*Existence and Uniqueness*), the logarithm is described (§*The Logarithm*), examples are computed (§*Worked Examples*), the matrix picture is given (§*The Matrix Picture*), the three decompositions are compared (§*The Three Polar Decompositions*), the coordinates and the volume element are described (§*The Exponential Coordinates*), and the idempotent form is recorded at the end (§*The Idempotent Form*).

Every numerical value displayed below was recomputed in double precision.

## The Decomposition

### The Data

An element of the algebra is written $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$. Its circular components are

$$
Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad
Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown},
$$

and the element is a unit exactly when $Q_{+}Q_{-}=\langle\breve Q\rangle_{\mathrm{ts}}\neq0$.

**Definition.** An **exponential polar decomposition** of a unit $\breve Q$ is a writing

$$
\breve Q=\exp\breve Q_{\log},\qquad \breve Q_{\log}\in\mathbb{B}_{\mathrm{r}},
$$

in which $\breve Q_{\log}$ is the **exponent**. The exponent is a logarithm of $\breve Q$ in the sense of §*The Logarithm*. It is an element of the algebra, not a pair of numbers, and it is written

$$
\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown},
\qquad
Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle},
\qquad
Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}.
$$

The coefficient rule of *Conventions in Mathematics* puts the prime on the imaginary coordinate. The coefficient $Q_{\log\blacktriangle}$ is the **scalar part** of the exponent and $Q_{\log\blacktriangledown}$ its **split part**. The double subscript is a label, not an operation: $q_{\log\blacktriangle}$ is the real part of $Q_{\log\blacktriangle}$, not the logarithm of $Q_{\blacktriangle}$.

The four real components of the exponent are the following.

| component | part | value | role |
|---|---|---|---|
| $q_{\log\blacktriangle}$ | scalar | $\ln\rho$ | logarithmic scale |
| $q'_{\log\blacktriangle}$ | scalar | $\alpha$ | scalar phase |
| $q_{\log\blacktriangledown}$ | split | $\phi$ | boost |
| $q'_{\log\blacktriangledown}$ | split | $\beta$ | split phase |

The two complex coefficients collect them in pairs.

| coefficient | formula | real part | imaginary part |
|---|---|---|---|
| $Q_{\log\blacktriangle}$ | $\ln\rho+i\alpha$ | $q_{\log\blacktriangle}=\ln\rho$ | $q'_{\log\blacktriangle}=\alpha$ |
| $Q_{\log\blacktriangledown}$ | $\phi+i\beta$ | $q_{\log\blacktriangledown}=\phi$ | $q'_{\log\blacktriangledown}=\beta$ |

The parameter $\rho>0$ is the radius of the modulus, so it is not itself a component: the component is its logarithm $\ln\rho$. The parameter $\phi\in\mathbb{R}$ is the boost and is the component $q_{\log\blacktriangledown}$. The parameters $\alpha,\beta\in\mathbb{R}$ are the phases, the components $q'_{\log\blacktriangle}$ and $q'_{\log\blacktriangledown}$.

The phases are not independent. The pairs $(\alpha,\beta)$ and $(\alpha',\beta')$ give the same unit factor exactly when

$$
(\alpha',\beta')-(\alpha,\beta)\in\Lambda
:=\bigl\langle 2\pi(1,0),\ \pi(1,1)\bigr\rangle,
$$

the lattice generated by the scalar period $(2\pi,0)$ and the diagonal period $(\pi,\pi)$. Its covolume is $2\pi^{2}$, and the parameter space of the phases is $\mathbb{R}^{2}/\Lambda\cong T^{2}$.

The exponent splits into a term in the scale plane and a term in the angle plane:

$$
\breve Q_{\log}=\breve r_{\log}+i\Theta,
\qquad
\breve r_{\log}=\ln\rho+j\phi\in\mathbb{R}\{1,j\},
\qquad
i\Theta=i\alpha+ij\beta\in\mathbb{R}\{i,ij\}.
$$

Here $\breve r_{\log}$ is the logarithm of the modulus and $i\Theta$ the angle; the glyph $\breve r_{\log}$ follows the rule of *Conventions in Mathematics* that a logarithm carries the glyph of its element and the subscript $\log$. In the four basis terms,

$$
\breve Q_{\log}=q_{\log\blacktriangle}+jq_{\log\blacktriangledown}+iq'_{\log\blacktriangle}+ijq'_{\log\blacktriangledown}
=\ln\rho+j\phi+i\alpha+ij\beta.
$$

The circular components of the exponent are

$$
Q_{\log+}=Q_{\log\blacktriangle}+Q_{\log\blacktriangledown}=\ln\rho+\phi+i(\alpha+\beta),
\qquad
Q_{\log-}=Q_{\log\blacktriangle}-Q_{\log\blacktriangledown}=\ln\rho-\phi+i(\alpha-\beta),
$$

and they are the logarithms of the circular components $Q_{+}$ and $Q_{-}$ of the element.

### The Two Factors

The modulus is the positive square root of $\breve Q\bar{\breve Q}$ in the cone $P$, and it is exponentiated by the split-complex exponential:

$$
\breve r=\sqrt{\breve Q\bar{\breve Q}}=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)=\exp(\breve r_{\log}),
\qquad
\breve r_{\log}=\ln\rho+j\phi,
$$

with $\rho=\sqrt{\rho_{+}\rho_{-}}>0$ and $\phi=\tfrac12\ln(\rho_{+}/\rho_{-})$. The unit factor is the exponential of the angle:

$$
u=\breve r^{-1}\breve Q=e^{i\alpha}e^{ij\beta}=\exp(i\Theta),
\qquad
i\Theta=i\alpha+ij\beta.
$$

In the two circle components it is

$$
u=\bigl(\cos\alpha+i\sin\alpha\bigr)\bigl(\cos\beta+ij\sin\beta\bigr).
$$

The three Euler formulas are

$$
\exp(i\alpha)=\cos\alpha+i\sin\alpha,\qquad
\exp(ij\beta)=\cos\beta+ij\sin\beta,\qquad
\exp(j\phi)=\cosh\phi+j\sinh\phi.
$$

The first is the scalar circle, the second the $ij$-circle, and the third the hyperbolic boost. The first two generate the unit torus; the third is one of the two positive directions of the cone $P$, the other being $\exp(t)$.

**Proposition (the two scales and the two phases).** The modulus has circular components

$$
\rho_{+}=\rho e^{\phi},\qquad \rho_{-}=\rho e^{-\phi},
$$

and the unit factor has circular components

$$
e^{i(\alpha+\beta)},\qquad e^{i(\alpha-\beta)}.
$$

*Proof.* The circular components of $\breve r=\rho(\cosh\phi+j\sinh\phi)$ are $\rho(\cosh\phi\pm\sinh\phi)=\rho e^{\pm\phi}$, and the circular components of $e^{i\alpha}e^{ij\beta}$ are $e^{i\alpha}e^{\pm i\beta}$.

The four parameters are therefore the two scales and the two phases of the two circular components, written logarithmically:

$$
\rho_{+}=\rho e^{\phi},\quad \rho_{-}=\rho e^{-\phi},\qquad
\theta_{+}=\alpha+\beta,\quad \theta_{-}=\alpha-\beta.
$$

The inverse change is

$$
\rho=\sqrt{\rho_{+}\rho_{-}},\qquad \phi=\tfrac12\ln\frac{\rho_{+}}{\rho_{-}},\qquad
\alpha=\tfrac12(\theta_{+}+\theta_{-}),\qquad \beta=\tfrac12(\theta_{+}-\theta_{-}).
$$

The two factors, their ranges and their logarithms are recorded in one table.

| factor | formula | range | logarithm | parameters |
|---|---|---|---|---|
| modulus | $\breve r=\rho(\cosh\phi+j\sinh\phi)$ | cone $P$ | $\breve r_{\log}=\ln\rho+j\phi$ | $\ln\rho\in\mathbb{R}$, $\phi\in\mathbb{R}$ |
| unit factor | $u=e^{i\alpha}e^{ij\beta}$ | torus $T^{2}$ | $i\Theta=i\alpha+ij\beta$ | $\alpha,\beta$ modulo $\Lambda$ |

The real dimensions are $2$ and $2$, and they add to the real dimension $4$ of the group of units. The modulus is non-compact, the torus is compact, and the product is the group of units.

### One Exponential

Because the algebra is commutative and the two exponents $\breve r_{\log}$ and $i\Theta$ commute,

$$
\breve Q=\exp(\breve r_{\log}+i\Theta)=\breve r\,u
=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)e^{i\alpha}e^{ij\beta}.
$$

The polar word is one exponential, not a product of two independent exponentials with an ordering correction. In full,

$$
\breve Q=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)\bigl(\cos\alpha+i\sin\alpha\bigr)\bigl(\cos\beta+ij\sin\beta\bigr).
$$

The closed form of the exponential of a general element follows from the same commutativity. For $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$,

$$
\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})
=\sum_{n=0}^{\infty}\frac{(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})^{n}}{n!}
=\sum_{k,l}\frac{Q_{\log\blacktriangle}^{k}(jQ_{\log\blacktriangledown})^{l}}{k!\,l!}
=e^{Q_{\log\blacktriangle}}\bigl(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown}\bigr),
$$

because $j^{2}=1$. This is the **reduced Euler formula** of the algebra. It reduces to $\exp(Q_{\log\blacktriangle})$ when $Q_{\log\blacktriangledown}=0$ and to $\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown}$ when $Q_{\log\blacktriangle}=0$.

**Example.** For $\breve Q_{\log}=j\ln2$ the closed form gives

$$
\exp(j\ln2)=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34 j,
$$

that is $1.25+0.75j$. In the four parameters, $\rho=1$, $\phi=\ln2$ and $\alpha=\beta=0$.

### Existence and Uniqueness

**Theorem.** The exponential is a bijection from the **principal domain**

$$
D=\Bigl\{\,\ln\rho+j\phi+i\alpha+ij\beta:\rho>0,\ \phi\in\mathbb{R},\ \lvert\alpha\rvert+\lvert\beta\rvert\le\pi\,\Bigr\}
$$

onto the unit group $\mathbb{B}_{\mathrm{r}}^{\times}$; the boundary of the diamond is taken half-open, so that each pair of arguments $(\theta_{+},\theta_{-})\in(-\pi,\pi]^{2}$ has exactly one representative.

**Existence.** Let $\breve Q$ be a unit. By the modulus–unit theorem it has a unique decomposition $\breve Q=\breve r u$ with $\breve r\in P$ and $u\bar u=1$. Write $\breve r=\rho(\cosh\phi+j\sinh\phi)$ with $\rho=\sqrt{\rho_{+}\rho_{-}}>0$ and $\phi=\tfrac12\ln(\rho_{+}/\rho_{-})$; this writing is unique. The unit $u$ has circular components $e^{i\theta_{+}}$ and $e^{i\theta_{-}}$ with $\theta_{\pm}\in(-\pi,\pi]$; put $\alpha=(\theta_{+}+\theta_{-})/2$ and $\beta=(\theta_{+}-\theta_{-})/2$. Then $u=e^{i\alpha}e^{ij\beta}$ and

$$
\breve Q=\exp(\ln\rho+j\phi+i\alpha+ij\beta),
$$

with $\lvert\alpha\rvert+\lvert\beta\rvert=\max(\lvert\theta_{+}\rvert,\lvert\theta_{-}\rvert)\le\pi$.

**Uniqueness.** Suppose $\exp\breve Q_{\log}=\exp\breve Q_{\log}'$ with $\breve Q_{\log},\breve Q_{\log}'\in D$. Then $\breve Q_{\log}-\breve Q_{\log}'$ lies in the kernel of the exponential, computed in §*The Kernel and the Fibre* as

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

In the coordinates $(\ln\rho,\phi,\alpha,\beta)$ the kernel acts by

$$
(\alpha,\beta)\longmapsto(\alpha+2\pi k+\pi l,\ \beta+\pi l),\qquad k,l\in\mathbb{Z},
$$

that is by the lattice $\Lambda=\langle2\pi(1,0),\pi(1,1)\rangle$, with $\rho$ and $\phi$ fixed. The diamond is a fundamental domain for $\Lambda$: the linear change $(\theta_{+},\theta_{-})\mapsto(\alpha,\beta)$ carries the fundamental square $(-\pi,\pi]^{2}$ of $2\pi\mathbb{Z}^{2}$ bijectively onto it. Two points of the diamond therefore differ by an element of the lattice only if they are equal. Hence $\breve Q_{\log}=\breve Q_{\log}'$.

The theorem is the exact analogue of the principal strip of $\mathbb{C}$: there the exponential is a bijection from $\{\ln r+i\theta:r>0,\ -\pi<\theta\le\pi\}$ onto $\mathbb{C}^{\times}$, and the fundamental domain is a strip. Here the fundamental domain is the product of two strips in the two circular arguments, which is the diamond in the two phases.

### The Group Law

The exponential is a homomorphism from the additive group of the algebra to the multiplicative group of the units:

$$
\exp(\breve Q_{\log}_1+\breve Q_{\log}_2)=\exp\breve Q_{\log}_1\,\exp\breve Q_{\log}_2,\qquad \exp 0=1.
$$

In the four parameters the law is

$$
\rho=\rho_1\rho_2,\qquad \phi=\phi_1+\phi_2,\qquad
(\alpha,\beta)=(\alpha_1+\alpha_2,\ \beta_1+\beta_2)\ \text{modulo}\ \Lambda.
$$

The scales multiply and add in the logarithm, the boost adds, and the phases add on the torus. The group of units is therefore

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{R}^{2}\times T^{2},
$$

with the two real coordinates $\ln\rho$ and $\phi$ and the two torus coordinates $(\alpha,\beta)$ modulo $\Lambda$. The exponential exhibits the group as the quotient of the additive group $\mathbb{R}^{4}$ by the kernel lattice,

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{R}^{4}\big/2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

## The Logarithm

### The General Logarithm

A **logarithm** of a unit $\breve Q$ is an element $\breve Q_{\log}$ with $\exp\breve Q_{\log}=\breve Q$. The definition is an equation, not a formula; the formula is what solving the equation gives.

Write $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ and $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, and put $Q_{\log\pm}=Q_{\log\blacktriangle}\pm Q_{\log\blacktriangledown}$. The equation splits into the two complex equations

$$
e^{Q_{\log\blacktriangle}}\cosh Q_{\log\blacktriangledown}=Q_{\blacktriangle},\qquad e^{Q_{\log\blacktriangle}}\sinh Q_{\log\blacktriangledown}=Q_{\blacktriangledown}.
$$

Adding and subtracting them gives

$$
e^{Q_{\log+}}=Q_{+},\qquad e^{Q_{\log-}}=Q_{-}.
$$

Hence, for any choices of the complex logarithms,

$$
Q_{\log+}=\log(Q_{+}),\qquad Q_{\log-}=\log(Q_{-}),
$$

and therefore

$$
Q_{\log\blacktriangle}=\frac{\log(Q_{+})+\log(Q_{-})}{2},\qquad
Q_{\log\blacktriangledown}=\frac{\log(Q_{+})-\log(Q_{-})}{2}.
$$

In the algebra, the logarithm is therefore

$$
\breve Q_{\log}=\frac{\log(Q_{+})+\log(Q_{-})}{2}
+j\,\frac{\log(Q_{+})-\log(Q_{-})}{2},
$$

the **global formula**, valid on the whole unit group for any choice of branch in each circular component. A logarithm exists exactly when both $Q_{+}$ and $Q_{-}$ are non-zero, that is exactly when $\breve Q$ is a unit. The general solution is

$$
\breve Q_{\log}=\operatorname{Log}\breve Q+2\pi i k+\pi i(1+j)l,\qquad k,l\in\mathbb{Z},
$$

or, in the phases, the principal logarithm plus the lattice $\Lambda$.

By the coefficient rule of *Conventions in Mathematics*, the two complex coefficients of the exponent carry a prime on their imaginary parts,

$$
Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle},\qquad
Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown},
$$

and, for the principal branch, the four real components are:

| component | name | value from $Q_{+},Q_{-}$ | role |
|---|---|---|---|
| $q_{\log\blacktriangle}$ | logarithmic scale | $\tfrac12\ln\lvert Q_{+}Q_{-}\rvert$ | overall size, unique |
| $q'_{\log\blacktriangle}$ | scalar phase | $\tfrac12\bigl(\operatorname{Arg}(Q_{+})+\operatorname{Arg}(Q_{-})\bigr)$ | angle on $T^{2}$ |
| $q_{\log\blacktriangledown}$ | boost | $\tfrac12\ln\lvert Q_{+}/Q_{-}\rvert$ | relative scale, unique |
| $q'_{\log\blacktriangledown}$ | split phase | $\tfrac12\bigl(\operatorname{Arg}(Q_{+})-\operatorname{Arg}(Q_{-})\bigr)$ | angle on $T^{2}$ |

with $\rho=\sqrt{\lvert Q_{+}Q_{-}\rvert}$ and $\operatorname{Arg}$ the principal argument in $(-\pi,\pi]$. Another branch adds a lattice vector to $(\alpha,\beta)$. The exponent is the sum of the four basis terms,

$$
\breve Q_{\log}=q_{\log\blacktriangle}+jq_{\log\blacktriangledown}+iq'_{\log\blacktriangle}+ijq'_{\log\blacktriangledown}
=\ln\rho+j\phi+i\alpha+ij\beta.
$$

**Example.** Take $\breve Q=3+4i+j(1-i)$, so $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. Then $Q_{+}=4+3i$ and $Q_{-}=2+5i$, and the principal complex logarithms are

$$
\operatorname{Log}(4+3i)=1.6094379+0.6435011\,i,\qquad
\operatorname{Log}(2+5i)=1.6836479+1.1902899\,i.
$$

The principal logarithm is

$$
\operatorname{Log}\breve Q=1.6465429+0.9168955\,i-0.0371050\,j-0.2733944\,ij.
$$

Exponentiating it back gives $3+4i+j(1-i)$ up to rounding. In the four parameters, $\ln\rho=1.6465429$, $\phi=-0.0371050$, $\alpha=0.9168955$, $\beta=-0.2733944$.

### The Principal Logarithm

The **principal logarithm** is obtained by choosing the principal complex logarithm in each circular component:

$$
\operatorname{Log}\breve Q=\frac{\operatorname{Log}(Q_{+})+\operatorname{Log}(Q_{-})}{2}
+j\,\frac{\operatorname{Log}(Q_{+})-\operatorname{Log}(Q_{-})}{2},
$$

with the argument of each component in $(-\pi,\pi]$. Its phases are

$$
\alpha=\frac{\operatorname{Arg}(Q_{+})+\operatorname{Arg}(Q_{-})}{2},\qquad
\beta=\frac{\operatorname{Arg}(Q_{+})-\operatorname{Arg}(Q_{-})}{2},
$$

and they satisfy

$$
\lvert\alpha\rvert+\lvert\beta\rvert=\max\bigl(\lvert\operatorname{Arg}(Q_{+})\rvert,\lvert\operatorname{Arg}(Q_{-})\rvert\bigr)\le\pi.
$$

The principal logarithm therefore lies in the principal diamond, and by the theorem of §*Existence and Uniqueness* it is the unique logarithm there. It is defined on the whole unit group.

The principal logarithm is real-analytic on the complement of the two walls

$$
W_{+}=\{\,Q_{+}\in(-\infty,0)\,\},\qquad W_{-}=\{\,Q_{-}\in(-\infty,0)\,\},
$$

each of real dimension three, and it is discontinuous across them. A branch that continued analytically across a wall would have to continue by a period and would not be single-valued. The walls are the exact analogue of the negative real axis of $\mathbb{C}$; there is one wall for each circular component.

The two walls are not the zero divisors. The zero divisors are the two real two-planes $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$, on which one circular component vanishes; they lie in the closures of the walls. The walls are larger: a unit with $Q_{+}=-1$ and $Q_{-}=-2$ lies on both and has a perfectly good logarithm,

$$
\operatorname{Log}\breve Q=\frac{\ln2}{2}+i\pi-\frac{\ln2}{2}j,
$$

because both circular components are negative reals, with principal argument $\pi$.

No continuous single-valued branch exists on the whole unit group, because the unit group has fundamental group $\mathbb{Z}^{2}$; the obstruction is the kernel lattice, not a failure of local invertibility. The exponential is a covering map onto the unit group, and the logarithm is its multivalued inverse.

### The Kernel and the Fibre

The kernel of the exponential is the set of exponents with $\rho=1$, $\phi=0$ and $u=1$, that is the set of $i\alpha+ij\beta$ with $(\alpha,\beta)\in\Lambda$. In the algebra,

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}
=\bigl\{\,\pi i(k(1+j)+l(1-j)):k,l\in\mathbb{Z}\,\bigr\}.
$$

It is a rank-two lattice, generated by

$$
2\pi i\qquad\text{and}\qquad \pi i(1+j).
$$

The scalar period $2\pi i$ and the split period $2\pi ij$ are also in the kernel, but they generate only a sublattice of index two:

$$
2\pi i=\pi i(1+j)+\pi i(1-j),\qquad
2\pi ij=\pi i(1+j)-\pi i(1-j).
$$

The period $2\pi ij$ is therefore not an independent period: half of it, $\pi i(1+j)$, is a period, and the sum and difference of the two half-periods recover the scalar and split periods.

The fibre of the exponential over a unit $\breve Q$ is

$$
\exp^{-1}(\breve Q)=\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^{2}.
$$

In the phases the fibre is the orbit of $(\alpha,\beta)$ under $\Lambda$, and exactly one point of the orbit lies in the half-open diamond. The ambiguity is one integer for each circular component, the exact replacement of the single integer $2\pi i\mathbb{Z}$ of the complex case.

## Worked Examples

### A Generic Element

Take $\breve Q=3+4i+j(1-i)$, with $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. The circular components and their moduli are

$$
Q_{+}=4+3i,\quad \rho_{+}=5,\qquad
Q_{-}=2+5i,\quad \rho_{-}=\sqrt{29}=5.385164807134504.
$$

The modulus parameters are

$$
\rho=\sqrt{\rho_{+}\rho_{-}}=\sqrt{5\sqrt{29}}=5.189009928268833,\qquad
\ln\rho=1.6465429137136687,
$$

and

$$
\phi=\tfrac12\ln\frac{\rho_{+}}{\rho_{-}}=\tfrac12\ln\frac{5}{\sqrt{29}}=-0.03710500127956826.
$$

The phases are

$$
\alpha=\tfrac12\bigl(\operatorname{Arg}(4+3i)+\operatorname{Arg}(2+5i)\bigr)=0.916895529237908,
$$

$$
\beta=\tfrac12\bigl(\operatorname{Arg}(4+3i)-\operatorname{Arg}(2+5i)\bigr)=-0.27339442044462364.
$$

The exponent is

$$
\operatorname{Log}\breve Q=1.6465429137+0.9168955292\,i
-0.0371050013\,j-0.2733944204\,ij,
$$

and the reconstruction is

$$
\exp(\operatorname{Log}\breve Q)=3+4.000000000000000\,i+j(1-i),
$$

with Euclidean error $1.9\times10^{-15}$.

The principal diamond contains the point with room to spare:

$$
\lvert\alpha\rvert+\lvert\beta\rvert=1.1902899497<\pi.
$$

### The Hyperbolic Line and the Phases

For $\breve Q=\exp(j\phi)=\cosh\phi+j\sinh\phi$ the circular components are $e^{\phi}$ and $e^{-\phi}$, both positive, so the phases vanish and the unit factor is $1$:

$$
\operatorname{Log}\bigl(\exp(j\phi)\bigr)=j\phi.
$$

The hyperbolic subgroup is a straight line in the exponent, along $j$, and its image is the future branch of the hyperbola in the plane $\mathbb{R}\{1,j\}$.

For $\breve Q=i$ both circular components are $i$, so $\operatorname{Log}i=i\pi/2$. For $\breve Q=ij$ the components are $i$ and $-i$, so

$$
\operatorname{Log}(ij)=\frac{\pi}{2}ij.
$$

For $\breve Q=j$ the components are $1$ and $-1$, so

$$
\operatorname{Log}j=\frac{\pi}{2}i-\frac{\pi}{2}ij.
$$

This point lies on the boundary of the principal diamond, with $\lvert\alpha\rvert+\lvert\beta\rvert=\pi$: the unit $j$ is the point at which the two phases saturate the diamond.

### A Table of Examples

| $\breve Q$ | $\rho$ | $\phi$ | $\alpha$ | $\beta$ | $\operatorname{Log}\breve Q$ | error |
|---|---|---|---|---|---|---|
| $3+4i+j(1-i)$ | $5.1890099283$ | $-0.0371050013$ | $0.9168955292$ | $-0.2733944204$ | $1.6465429137+0.9168955292i-0.0371050013j-0.2733944204ij$ | $1.9\times10^{-15}$ |
| $1+i$ | $\sqrt2$ | $0$ | $\pi/4$ | $0$ | $0.3465735903+0.7853981634i$ | $2.2\times10^{-16}$ |
| $i$ | $1$ | $0$ | $\pi/2$ | $0$ | $\frac{\pi}{2}i$ | $6.1\times10^{-17}$ |
| $ij$ | $1$ | $0$ | $0$ | $\pi/2$ | $\frac{\pi}{2}ij$ | $6.1\times10^{-17}$ |
| $j$ | $1$ | $0$ | $\pi/2$ | $-\pi/2$ | $\frac{\pi}{2}i-\frac{\pi}{2}ij$ | $8.7\times10^{-17}$ |
| $\exp(j\ln2)$ | $1$ | $\ln2$ | $0$ | $0$ | $j\ln2$ | $0$ |
| $-1$ | $1$ | $0$ | $\pi$ | $0$ | $\pi i$ | $1.2\times10^{-16}$ |

The errors are at machine precision, computed from the double-precision values before the rounding of the displayed entries. The row $\exp(j\ln2)$ has zero reconstruction error in double precision, because the data are the rounded values $\cosh(\ln2)=1.25$ and $\sinh(\ln2)=0.75$.

The zero divisor $1+j$ has $Q_{-}=0$ and no logarithm, so it is absent from the table. The image of the exponential is exactly the unit group; on a zero divisor one circular component is zero and has no preimage under the complex exponential.

### The Kernel and the Branch

The element $-1$ has, among its logarithms, the four corner values

$$
i\pi,\qquad -i\pi,\qquad i\pi j,\qquad -i\pi j,
$$

the vertices of the diamond, all with exponential $-1$; only $i\pi$ lies in the principal diamond. The others are obtained from it by the lattice vectors

$$
i\pi-(-i\pi)=2\pi i,\qquad i\pi-i\pi j=\pi i(1-j),\qquad i\pi-(-i\pi j)=\pi i(1+j),
$$

all in the kernel. Every other logarithm of $-1$ is one of the four plus a lattice period. This is the rank-two non-uniqueness in its simplest form: one integer of ambiguity for each circular component.

In the phases the four corners are

$$
(\pi,0),\qquad (-\pi,0),\qquad (0,\pi),\qquad (0,-\pi),
$$

and the diamond's area is $2\pi^{2}$, the covolume of $\Lambda$.

## The Matrix Picture

### The Exponential of a Block Matrix

In the complex basis $\{1,j\}$ the multiplication by $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ is the block matrix

$$
M_{\breve Q_{\log}}=\begin{pmatrix}Q_{\log\blacktriangle}&Q_{\log\blacktriangledown}\\Q_{\log\blacktriangledown}&Q_{\log\blacktriangle}\end{pmatrix}.
$$

The change of basis $(z,w)\mapsto(z+w,z-w)$ diagonalises it:

$$
M_{\breve Q_{\log}}\longmapsto\begin{pmatrix}Q_{\log\blacktriangle}+Q_{\log\blacktriangledown}&0\\0&Q_{\log\blacktriangle}-Q_{\log\blacktriangledown}\end{pmatrix}
=\begin{pmatrix}\log(Q_{+})&0\\0&\log(Q_{-})\end{pmatrix}.
$$

The exponential of the matrix is therefore

$$
\exp M_{\breve Q_{\log}}=\begin{pmatrix}e^{Q_{\log\blacktriangle}+Q_{\log\blacktriangledown}}&0\\0&e^{Q_{\log\blacktriangle}-Q_{\log\blacktriangledown}}\end{pmatrix}
=\begin{pmatrix}Q_{+}&0\\0&Q_{-}\end{pmatrix},
$$

which is $M_{\breve Q}$ in the same basis. In the original basis,

$$
M_{\breve Q}=\exp M_{\breve Q_{\log}}
=\begin{pmatrix}e^{Q_{\log\blacktriangle}}\cosh Q_{\log\blacktriangledown}&e^{Q_{\log\blacktriangle}}\sinh Q_{\log\blacktriangledown}\\ e^{Q_{\log\blacktriangle}}\sinh Q_{\log\blacktriangledown}&e^{Q_{\log\blacktriangle}}\cosh Q_{\log\blacktriangledown}\end{pmatrix}
=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}.
$$

In the real basis $\{1,i,j,ij\}$ the same identity is the exponential of a $4\times4$ matrix, and its eigenvalues are $Q_{+},\bar Q_{+},Q_{-},\bar Q_{-}$, the two circular components with their conjugates.

**Proposition (the derivative).** The derivative of the exponential at $\breve Q_{\log}$ is left multiplication by $\exp\breve Q_{\log}$:

$$
d\exp_{\breve Q_{\log}}(\breve H)=\exp(\breve Q_{\log})\,\breve H.
$$

Its determinant is

$$
\det d\exp_{\breve Q_{\log}}=\lvert Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}\rvert^{2}=\rho_{+}^{2}\rho_{-}^{2}=\rho^{4},
$$

and its singular values are $\rho_{+},\rho_{+},\rho_{-},\rho_{-}$.

*Proof.* The derivative follows from $\exp(\breve Q_{\log}+t\breve H)=\exp\breve Q_{\log}\,\exp(t\breve H)$ and $\exp(t\breve H)=1+t\breve H+O(t^{2})$. The matrix of left multiplication by $\breve Q$ has complex determinant $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ in the basis $\{1,j\}$, hence real determinant $\lvert Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}\rvert^{2}$; and $\lvert Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}\rvert=\rho_{+}\rho_{-}$. The singular values are those of $M_{\breve r}$, namely $\rho_{+}$ and $\rho_{-}$, each twice.

The exponential is conformal on each circular component, and conformal on the whole algebra exactly when $\rho_{+}=\rho_{-}$, that is when $\phi=0$.

### The Matrix Logarithm and the Derivative

On the principal domain the matrix $M_{\breve Q_{\log}}$ is the principal matrix logarithm of $M_{\breve Q}$: its eigenvalues $\operatorname{Log}(Q_{\pm})$ have imaginary parts in $(-\pi,\pi]$, so they are the principal logarithms of the eigenvalues of $M_{\breve Q}$, and the two matrices are simultaneously diagonalised by the same change of basis.

The logarithm is differentiable on the complement of the walls, and its derivative is left multiplication by $\breve Q^{-1}$:

$$
d\operatorname{Log}_{\breve Q}(\breve H)=\breve Q^{-1}\breve H.
$$

In the circular components,

$$
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_{\pm}=\frac{H_{\pm}}{Q_{\pm}}.
$$

*Proof.* The exponential is a local biholomorphism with derivative left multiplication by $\exp\breve Q_{\log}=\breve Q$; the inverse function theorem gives the derivative of the inverse as left multiplication by $\breve Q^{-1}$.

The formula is the exact analogue of $\operatorname{Log}'Q=1/Q$ in $\mathbb{C}$, applied twice. The logarithm is holomorphic in each circular component, and the two Wirtinger derivatives with respect to the conjugates of the components annihilate it.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $\breve Q=\breve r u$ | $\breve r\in P$, $u\in T^{2}$ | all units | unique | square roots | $P\times T^{2}$ |
| rational-chart | $\breve Q=\breve r\,u(s_{1},s_{2})$ | $\breve r\in P$, $(s_{1},s_{2})\in\mathbb{R}^{2}$ | units with $Q_{\pm}\notin(-\infty,0]$ | unique on the chart | rational | four charts on $T^{2}$ |
| exponential | $\breve Q=\exp\breve Q_{\log}$ | $\breve Q_{\log}$ modulo $\ker\exp$ | all units | unique in the principal domain | exponential and logarithm | $\mathbb{B}_{\mathrm{r}}/\ker\exp$ |

### The Modulus–Unit Form

The modulus–unit form of *Modulus–Unit Polar Decomposition of Reduced Biquaternions* is the same decomposition with the exponent split as

$$
\breve Q_{\log}=\breve r_{\log}+i\Theta,\qquad
\breve r_{\log}=\ln\rho+j\phi\in\mathbb{R}\{1,j\},\qquad i\Theta=i\alpha+ij\beta\in\mathbb{R}\{i,ij\}.
$$

The logarithmic scale lies in the plane $\mathbb{R}\{1,j\}$, the angle in the plane $\mathbb{R}\{i,ij\}$, and the two commute. Exponentiating each factor gives

$$
\breve r=\exp(\breve r_{\log})=\rho(\cosh\phi+j\sinh\phi),\qquad
u=\exp(i\Theta)=e^{i\alpha}e^{ij\beta},
$$

and the product is the single exponential $\breve Q=\breve r u$. The modulus is global and algebraic, and no coordinate on the torus is chosen.

### The Rational-Chart Form

The rational-chart form of *Rational-Chart Polar Decomposition of Reduced Biquaternions* writes the unit factor as

$$
u(s_{1},s_{2})=\frac{c(s_{1})+c(s_{2})}{2}+j\,\frac{c(s_{1})-c(s_{2})}{2},
\qquad c(s)=\frac{1-is}{1+is}.
$$

The chart coordinate and the angle are related on each circular component by

$$
s_{\pm}=-\tan\frac{\theta_{\pm}}{2},\qquad \theta_{\pm}=-2\arctan s_{\pm},
$$

that is, in the phases,

$$
s_{1}=-\tan\frac{\alpha+\beta}{2},\qquad s_{2}=-\tan\frac{\alpha-\beta}{2}.
$$

The chart is rational in $s_{k}$ and in $u_{k}$, it misses the two circles on which a circular component is $-1$, and four charts cover the torus. The modulus is unchanged, so the rational-chart form differs from the exponential form only in the coordinate used on $T^{2}$.

### The Change of Coordinates

The change from the exponential phases to the rational coordinates is

$$
s_{k}=-\tan\frac{\theta_{k}}{2},\qquad \theta_{k}=-2\arctan s_{k},
$$

transcendental and real-analytic on the principal strip $-\pi<\theta_{k}<\pi$. The endpoint $\theta_{k}=\pi$ is sent to $s_{k}=\infty$, which is the missing point $u_{k}=-1$ of the chart. The period lattice has no expression in the rational coordinates, which are coordinates on the circle itself rather than on its cover; the boundary survives only as the poles $s_{1}t_{1}=1$ and $s_{2}t_{2}=1$ of the group law.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is the group decomposition $P\times T^{2}$, algebraic and coordinate-free on the torus. The rational-chart form is the Cayley coordinate on the torus, rational and local. The exponential form is the Lie-algebra coordinate, global with the lattice quotient, and unique on the principal domain.

The exponential form is the only one in which the group law is addition. It is also the only one in which the non-uniqueness is a lattice: the kernel is $\mathbb{Z}^{2}$, and the principal diamond is a fundamental domain. The modulus–unit form has no non-uniqueness at all; the rational chart has a cut but no period.

| property | modulus–unit | rational-chart | exponential |
|---|---|---|---|
| algebraic or transcendental | algebraic | rational | transcendental |
| global on the units | yes | no | yes |
| unique without a choice | yes | no | no |
| restores uniqueness by | nothing | restricting the domain | a fundamental domain |
| group law | componentwise product | tangent addition | addition |

## The Exponential Coordinates

### The Coordinate Planes

The exponential coordinates are the four real functions

$$
(\ln\rho,\ \phi,\ \alpha,\ \beta),
$$

equivalently the real and imaginary parts of the two complex coordinates $Q_{\log\blacktriangle}=\ln\rho+i\alpha$ and $Q_{\log\blacktriangledown}=\phi+i\beta$ of the exponent.

Fixing the scales $\rho,\phi$ and varying the phases gives the torus

$$
T^{2}=\{\exp(i\alpha+ij\beta):\alpha,\beta\in\mathbb{R}\}.
$$

Fixing the phases and varying the scales gives the cone

$$
P=\{\exp(\ln\rho+j\phi):\ln\rho\in\mathbb{R},\ \phi\in\mathbb{R}\}
=\{\rho(\cosh\phi+j\sinh\phi):\rho>0,\ \phi\in\mathbb{R}\}.
$$

The product $P\times T^{2}$ is the unit group, and the exponential is the universal covering

$$
\mathbb{R}^{2}\times\mathbb{R}^{2}\longrightarrow P\times T^{2}
$$

with deck group $\Lambda\cong\mathbb{Z}^{2}$.

The surfaces $\rho=\mathrm{const}$ and $\phi=\mathrm{const}$ are the surfaces of constant scale; their intersection is the torus of constant modulus. The surfaces $\alpha=\mathrm{const}$ and $\beta=\mathrm{const}$ are the surfaces of constant phase; their intersection is the cone $P u$ of constant unit factor, a copy of $P$ rotated by $u$. The exponential maps the plane $\mathbb{R}\{1,j\}$ onto the cone $P$ and the plane $\mathbb{R}\{i,ij\}$ onto the torus $T^{2}$, and the two families of coordinate surfaces are the images of the coordinate lines in these planes.

### The Volume Element

In the Cartesian coordinates $(Q_{\blacktriangle},Q_{\blacktriangledown})\in\mathbb{C}^{2}\cong\mathbb{R}^{4}$ the Euclidean volume element is

$$
dV=d(\operatorname{Re}Q_{\blacktriangle})\,d(\operatorname{Im}Q_{\blacktriangle})\,d(\operatorname{Re}Q_{\blacktriangledown})\,d(\operatorname{Im}Q_{\blacktriangledown}).
$$

The linear change to the circular components $(Q_{+},Q_{-})$ has real determinant $4$, so

$$
dV=\frac14\,d(\operatorname{Re}(Q_{+}))\,d(\operatorname{Im}(Q_{+}))\,
d(\operatorname{Re}(Q_{-}))\,d(\operatorname{Im}(Q_{-})).
$$

In the polar coordinates of the two components, with $\rho_{\pm}=\rho e^{\pm\phi}$ and $\theta_{\pm}=\alpha\pm\beta$, the area elements are $\rho_{\pm}\,d\rho_{\pm}\,d\theta_{\pm}$, and the change $(\rho,\phi,\alpha,\beta)\mapsto(\rho_{+},\theta_{+},\rho_{-},\theta_{-})$ has determinant $4\rho$. Hence

$$
dV=\rho^{3}\,d\rho\,d\phi\,d\alpha\,d\beta
=\rho^{4}\,d(\ln\rho)\,d\phi\,d\alpha\,d\beta.
$$

The Jacobian determinant of the exponential, from the Cartesian volume in the exponent to the Cartesian volume in the algebra, is $\rho^{4}$, the same in either Cartesian reading. The image of a box

$$
[\ln\rho_{1},\ln\rho_{2}]\times[\phi_{1},\phi_{2}]\times[\alpha_{1},\alpha_{2}]\times[\beta_{1},\beta_{2}]
$$

has volume

$$
\frac{\rho_{2}^{4}-\rho_{1}^{4}}{4}\,(\phi_{2}-\phi_{1})(\alpha_{2}-\alpha_{1})(\beta_{2}-\beta_{1}),
$$

the integral of $\rho^{3}$ over the box. The formula is exact.

### The Harmonic Reading

The functions $\ln\rho$ and $\phi$ are harmonic on the cone, and the phases $\alpha,\beta$ are harmonic on the cut torus. The complex coordinates $\operatorname{Log}(Q_{+})$ and $\operatorname{Log}(Q_{-})$ are the local holomorphic coordinates supplied by the principal logarithm, and the exponential is their inverse.

The algebra carries two commuting complex structures: the left multiplication by $i$ and the left multiplication by $ij$. Both square to $-1$ and commute, and the two circular components diagonalise the second, with eigenvalue $+i$ on $Q_{+}$ and $-i$ on $Q_{-}$. The exponential is holomorphic for both structures, because the closed form $\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})=e^{Q_{\log\blacktriangle}}(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown})$ is entire in $Q_{\log\blacktriangle}$ and in $Q_{\log\blacktriangledown}$. The obstruction to a global logarithm is the lattice, not the complex structure.

### The Idempotent Form

The two circular components can be made into coordinates. Put

$$
\Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2},\qquad
Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}.
$$

Then

$$
\Pi_{\pm}^{2}=\Pi_{\pm},\qquad \Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}+\Pi_{-}=1,
$$

and

$$
\breve Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}.
$$

The multiplication is componentwise in these coordinates:

$$
\breve Q\,\breve R=(Q_{+}R_{+})\Pi_{+}+(Q_{-}R_{-})\Pi_{-}.
$$

The algebra is therefore the direct product $\mathbb{C}\oplus\mathbb{C}$, and the two circular components are its two factors. This is the **idempotent form** of the algebra. Every formula of this article is the pair of the corresponding complex formula in the two factors:

| object | idempotent form |
|---|---|
| element | $\breve Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ |
| bar | $\bar{\breve Q}=\bar Q_{+}\Pi_{+}+\bar Q_{-}\Pi_{-}$ |
| reduced norm | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ |
| modulus | $\breve r=\rho_{+}\Pi_{+}+\rho_{-}\Pi_{-}$ |
| unit factor | $u=e^{i\theta_{+}}\Pi_{+}+e^{i\theta_{-}}\Pi_{-}$ |
| exponent | $\breve Q_{\log}=\operatorname{Log}Q_{+}\Pi_{+}+\operatorname{Log}Q_{-}\Pi_{-}$ |
| kernel | $2\pi i(\mathbb{Z}\Pi_{+}\oplus\mathbb{Z}\Pi_{-})$ |
| principal domain | $\lvert\operatorname{Im}\operatorname{Log}Q_{+}\rvert\le\pi$, $\lvert\operatorname{Im}\operatorname{Log}Q_{-}\rvert\le\pi$ |
| group law | addition in each factor |

In this form the principal domain is the product of the two principal strips, and the diamond is its image under the linear change from $(\theta_{+},\theta_{-})$ to $(\alpha,\beta)$. The form is convenient for computation, because every operation is performed twice in $\mathbb{C}$. It is recorded here, at the end, because the decomposition itself is stated in the algebra: the modulus is an element of the cone $P$, the unit factor a point of the torus $T^{2}$, and the exponent an element of $\mathbb{B}_{\mathrm{r}}$ modulo a lattice. The idempotent coordinates are a choice of coordinates on that structure, not its definition.

## Summary

Every unit $\breve Q$ has exactly one exponential polar decomposition in the principal domain,

$$
\breve Q=\exp(\breve Q_{\log}),\qquad \breve Q_{\log}=\ln\rho+j\phi+i\alpha+ij\beta,
$$

with

$$
\rho>0,\qquad \phi\in\mathbb{R},\qquad \lvert\alpha\rvert+\lvert\beta\rvert\le\pi.
$$

Its four components are $(q_{\log\blacktriangle},q'_{\log\blacktriangle},q_{\log\blacktriangledown},q'_{\log\blacktriangledown})=(\ln\rho,\alpha,\phi,\beta)$.

The exponent is the sum of the logarithmic scale $\ln\rho+j\phi$ in the plane $\mathbb{R}\{1,j\}$ and the angle $i\alpha+ij\beta$ in the plane $\mathbb{R}\{i,ij\}$. The modulus is $\breve r=\rho(\cosh\phi+j\sinh\phi)$ and the unit factor is $u=e^{i\alpha}e^{ij\beta}$, and the polar word is the single exponential $\breve Q=\breve r u$.

The exponential is computed by the closed form

$$
\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})
=e^{Q_{\log\blacktriangle}}\bigl(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown}\bigr),
$$

and it is a homomorphism. It is surjective onto the unit group and its kernel is the lattice

$$
2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^{2},
$$

generated by $2\pi i$ and $\pi i(1+j)$. The scalar and split periods $2\pi i$ and $2\pi ij$ generate a sublattice of index two. The logarithm exists for every unit and is unique only modulo this lattice; the principal diamond is a fundamental domain of area $2\pi^{2}$, and the exponential is a bijection from the product of the two real lines with the diamond onto the units.

The group law is addition in the exponential coordinates,

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{R}^{2}\times T^{2}
\cong\mathbb{R}^{4}\big/2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

The derivative is left multiplication by $\exp\breve Q_{\log}$; its determinant is $\rho_{+}^{2}\rho_{-}^{2}=\rho^{4}$, and its singular values are $\rho_{+},\rho_{+},\rho_{-},\rho_{-}$. The exponential is conformal on each circular component and conformal on the whole algebra exactly when $\phi=0$.

In the idempotent coordinates the exponent is the pair $(\operatorname{Log}Q_{+},\operatorname{Log}Q_{-})$, the kernel is $2\pi i(\mathbb{Z}\Pi_{+}\oplus\mathbb{Z}\Pi_{-})$, and the principal domain is the product of the two principal strips. That form is a coordinate description of the decomposition, recorded at the end.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | the unit, with scalar part $Q_{\blacktriangle}$ and split part $Q_{\blacktriangledown}$ |
| $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ | the two complex coefficients, with their real and imaginary coordinates |
| $Q_{\pm}=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the two circular components |
| $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ | the exponent |
| $Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle}=\ln\rho+i\alpha$ | the scalar part of the exponent |
| $Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}=\phi+i\beta$ | the split part of the exponent |
| $q_{\log\blacktriangle},q'_{\log\blacktriangle},q_{\log\blacktriangledown},q'_{\log\blacktriangledown}$ | the four real components of the exponent: $\ln\rho,\alpha,\phi,\beta$ |
| $\rho>0$ | the radius, with logarithm $\ln\rho$ |
| $\phi\in\mathbb{R}$ | the boost |
| $\alpha,\beta$ | the two phases |
| $\Lambda=\langle2\pi(1,0),\pi(1,1)\rangle$ | the lattice of the phases |
| $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ | the principal diamond |
| $\breve r=\rho(\cosh\phi+j\sinh\phi)$ | the modulus |
| $\breve r_{\log}=\ln\rho+j\phi$ | the logarithm of the modulus |
| $u=e^{i\alpha}e^{ij\beta}$ | the unit factor |
| $i\Theta=i\alpha+ij\beta$ | the angle |
| $P=\{\rho(\cosh\phi+j\sinh\phi):\rho>0,\ \phi\in\mathbb{R}\}$ | the cone of moduli |
| $T^{2}=\{e^{i\alpha}e^{ij\beta}:\alpha,\beta\in\mathbb{R}\}$ | the unit torus |
| $\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})=e^{Q_{\log\blacktriangle}}(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown})$ | the closed form of the exponential |
| $\operatorname{Log}\breve Q$ | the principal logarithm |
| $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ | the kernel of the exponential |
| $\rho_{+}=\rho e^{\phi}$, $\rho_{-}=\rho e^{-\phi}$ | the two scales |
| $\theta_{+}=\alpha+\beta$, $\theta_{-}=\alpha-\beta$ | the two arguments |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | the idempotent coordinates |
| $\det d\exp_{\breve Q_{\log}}=\rho^{4}$ | the Jacobian determinant |

## Further Reading

- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the modulus, the torus and the uniqueness of the pair.
- [Rational-Chart Polar Decomposition of Reduced Biquaternions](rational-chart-polar-decomposition-of-reduced-biquaternions.html), for the rational coordinate on the torus.
- [Reduced Biquaternion Elementary Functions](reduced-biquaternion-elementary-functions.html), for the exponential and the logarithm as functions.
- [Reduced Biquaternion Lie Group and Exponential Structure](reduced-biquaternion-lie-group-and-exponential-structure.html), for the kernel, the covering and the group of units.
- [Exponential Polar Decomposition of Complex Numbers](exponential-polar-decomposition-of-complex-numbers.html), for the one-coordinate exponential.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the hyperbolic exponential.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the noncommutative counterpart.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the topology of the unit group.
