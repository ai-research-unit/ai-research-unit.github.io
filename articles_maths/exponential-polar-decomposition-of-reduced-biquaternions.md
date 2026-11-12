# __Exponential Polar Decomposition of Reduced Biquaternions__

## Introduction

This article treats the **exponential polar decomposition** of an invertible reduced biquaternion: the writing

$$
\breve Q=\exp(\breve Q_{\log})
=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr)\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}),
\qquad
\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}},
$$

with $\rho>0$ the radius, $\theta_{\mathrm{rpd}}$ the boost, $\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ the two phases, and $\ln\rho$ the logarithmic scale. Equivalently,

$$
\breve Q=\breve r\,u,
\qquad
\breve r=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr),
\quad
u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}),
$$

with $\breve r$ the modulus and $u$ the unit factor. The decomposition is the exponential form of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Reduced Biquaternions*, which writes every invertible reduced biquaternion as $\breve Q=\breve r u$ with $\breve r$ in the cone $P$ and $u$ in the torus $T^2$.

The exponential and the logarithm are those of *Reduced Biquaternion Elementary Functions*: the exponential is a homomorphism onto the unit group, with kernel the rank-two lattice $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$, and the logarithm is its multivalued inverse. §*The Analytic Setting* states them in the form used below, and they are not derived again. What the article owns is the decomposition itself, its existence and uniqueness, the matrix picture and the exponential coordinates.

The algebra is the product $\mathbb{C}\times\mathbb{C}$ in the two complex components

$$
C_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\qquad
C_-=Q_{\blacktriangle}-Q_{\blacktriangledown},
$$

which are a complex-linear change of coordinates on the element. The decomposition is componentwise: the scalar factor $\rho e^{i\theta_{\mathrm{pha}}}$ multiplies both components, and the split factor $\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}$ enters with opposite signs. This is the form used throughout.

**The result.** The decomposition reads as follows.

| Item | Value |
|---|---|
| Algebra | $\mathbb{B}_{\mathrm{red}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, basis $1,i,j,ij$ |
| Domain | ${\mathbb{B}_{\mathrm{red}}}^\times=\{\breve Q:N=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0\}$ |
| Decomposition | $\breve Q=\breve r\,u=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ |
| Parameters | $\rho>0$, $\theta_{\mathrm{rpd}}\in\mathbb{R}$, $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\in\mathbb{R}^2/\Lambda$ |
| Unit factor | $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})=Q/\breve r$, in $T^2$ |
| Exponent | $\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ |
| Existence | every unit has a decomposition |
| Uniqueness | unique in the principal diamond $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$ |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Group | ${\mathbb{B}_{\mathrm{red}}}^\times\cong\mathbb{R}^2\times T^2$ |
| Companion | *Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion*, for the reading through the two complex components |
| Worked examples | *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*, for the eight cases and the reconstruction tables |

The plan is as follows. The analytic facts and the two complex components are recalled (§*The Analytic Setting*); the definition, the exponent and its four real coordinates, the factors and the single exponential are given (§*The Decomposition*); existence and uniqueness are proved in the principal domain (§*Existence and Uniqueness*); the logarithm, its principal branch and its fibre are read (§*The Logarithm*); the group law is stated (§*The Group Law*); the matrix picture is given (§*The Matrix Picture*); the three polar forms are compared (§*The Three Polar Decompositions*); the coordinates and the volume element are described (§*The Exponential Coordinates*); the numerical cases are collected in *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*.

## The Analytic Setting

The decomposition rests on the exponential and the logarithm of *Reduced Biquaternion Elementary Functions*, and on the product structure of the algebra in the two complex components.

### The Exponential and the Logarithm

The exponential of $X=X_{\blacktriangle}+jX_{\blacktriangledown}$ is

$$
\exp(X)=\exp(X_{\blacktriangle})\bigl(\cosh X_{\blacktriangledown}+j\sinh X_{\blacktriangledown}\bigr),
$$

the reduced Euler formula of the algebra. The table collects the properties used below.

| Property | Value |
|---|---|
| Closed form | $\exp(X_{\blacktriangle}+jX_{\blacktriangledown})=\exp(X_{\blacktriangle})(\cosh X_{\blacktriangledown}+j\sinh X_{\blacktriangledown})$ |
| Image | the unit group ${\mathbb{B}_{\mathrm{red}}}^\times=\{N\neq0\}$ |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Logarithm | exists for every unit, unique modulo the kernel |
| Principal domain | $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$, boundary half-open |
| Fibre | $\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^2$ |

These are the statements of *Reduced Biquaternion Elementary Functions*, §*The Exponential*, §*The Kernel and the Image* and §*The Principal Logarithm*. The present article reads them in the modulus–unit coordinates; it does not re-derive the kernel or the branch.

### The Two Complex Components

Put

$$
C_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\qquad
C_-=Q_{\blacktriangle}-Q_{\blacktriangledown}.
$$

The change $(Q_{\blacktriangle},Q_{\blacktriangledown})\mapsto(C_+,C_-)$ is complex-linear and invertible:

$$
Q_{\blacktriangle}=\frac{C_++C_-}{2},
\qquad
Q_{\blacktriangledown}=\frac{C_+-C_-}{2},
\qquad
\breve Q=\frac{C_++C_-}{2}+j\,\frac{C_+-C_-}{2}.
$$

In these coordinates the product is componentwise:

$$
(C_+,C_-)(D_+,D_-)=(C_+D_+,C_-D_-),
\qquad
1=(1,1),
\qquad
j=(1,-1).
$$

The reduced norm is the product of the components,

$$
N=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=C_+C_-,
$$

and an element is a unit exactly when both components are nonzero. The table records the change.

| Object | In $Q_{\blacktriangle},Q_{\blacktriangledown}$ | In $C_+,C_-$ |
|---|---|---|
| Element | $Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tfrac12(C_++C_-)+j\tfrac12(C_+-C_-)$ |
| Product | $(Q_{\blacktriangle}+jQ_{\blacktriangledown})(R_{\blacktriangle}+jR_{\blacktriangledown})$ | $(C_+D_+,C_-D_-)$ |
| Conjugate | $\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$ | $(\bar C_+,\bar C_-)$ |
| Norm | $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | $C_+C_-$ |
| Unit criterion | $N\neq0$ | $C_+\neq0$ and $C_-\neq0$ |

### The Four Real Coordinates

The exponential polar decomposition is the writing

$$
C_+=\rho e^{i\theta_{\mathrm{pha}}}e^{\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}},
\qquad
C_-=\rho e^{i\theta_{\mathrm{pha}}}e^{-\theta_{\mathrm{rpd}}-i\theta_{\mathrm{phb}}},
$$

with $\rho>0$ and real $\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$. The four real coordinates are therefore the polar data of the two components:

$$
\rho=\sqrt{\lvert C_+C_-\rvert},
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln\left\lvert\frac{C_+}{C_-}\right\rvert,
\qquad
\theta_{\mathrm{pha}}=\tfrac12\bigl(\operatorname{Arg}C_++\operatorname{Arg}C_-\bigr),
\qquad
\theta_{\mathrm{phb}}=\tfrac12\bigl(\operatorname{Arg}C_+-\operatorname{Arg}C_-\bigr).
$$

The change is inverted by

$$
C_+=\rho e^{i\theta_{\mathrm{pha}}}e^{\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}},
\qquad
C_-=\rho e^{i\theta_{\mathrm{pha}}}e^{-\theta_{\mathrm{rpd}}-i\theta_{\mathrm{phb}}}.
$$

The phases are defined modulo the lattice $\Lambda$: adding $\pi$ to both $\theta_{\mathrm{pha}}$ and $\theta_{\mathrm{phb}}$, or $\pi$ to one and $-\pi$ to the other, leaves both components unchanged. The principal diamond $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$ selects one representative. The table records the coordinates and their ranges.

| Coordinate | Formula from $C_\pm$ | Range | Role |
|---|---|---|---|
| $\rho$ | $\lvert C_+C_-\rvert^{1/2}$ | $(0,\infty)$ | common radius |
| $\theta_{\mathrm{rpd}}$ | $\tfrac12\ln\lvert C_+/C_-\rvert$ | $\mathbb{R}$ | boost, opposite signs |
| $\theta_{\mathrm{pha}}$ | $\tfrac12(\operatorname{Arg}C_++\operatorname{Arg}C_-)$ | modulo $\pi$ | common phase |
| $\theta_{\mathrm{phb}}$ | $\tfrac12(\operatorname{Arg}C_+-\operatorname{Arg}C_-)$ | modulo $\pi$ | relative phase |

The real dimension is four, the real dimension of the group of units. The coordinates separate into the modulus pair $(\rho,\theta_{\mathrm{rpd}})$ and the phase pair $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$.

## The Decomposition

### The Definition

**Definition.** An **exponential polar decomposition** of $\breve Q\in{\mathbb{B}_{\mathrm{red}}}^\times$ is a writing

$$
\breve Q=\breve r\,u,
\qquad
\breve r=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr),
\quad
u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}),
$$

with $\rho>0$, $\theta_{\mathrm{rpd}}\in\mathbb{R}$ and $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\in\mathbb{R}^2$, equivalently the single exponential

$$
\breve Q=\exp(\breve Q_{\log}),
\qquad
\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}.
$$

The factor $\breve r$ is the **modulus**, $u$ the **unit factor**, $\theta_{\mathrm{rpd}}$ the **boost**, $\theta_{\mathrm{pha}}$ and $\theta_{\mathrm{phb}}$ the **phases**, and $\breve Q_{\log}$ the **exponent**.

The modulus lies in the cone

$$
P=\{\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}):\rho>0,\ \theta_{\mathrm{rpd}}\in\mathbb{R}\},
$$

and the unit factor lies in the torus

$$
T^2=\{u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}):\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}\in\mathbb{R}\}.
$$

The decomposition is the modulus–unit decomposition with each factor exponentiated.

### The Exponent and Its Components

The exponent is

$$
\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown},
\qquad
Q_{\log\blacktriangle}=\ln\rho+i\theta_{\mathrm{pha}},
\qquad
Q_{\log\blacktriangledown}=\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}.
$$

Its four real coordinates are $(\ln\rho,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\theta_{\mathrm{phb}})$. The table collects them.

| Component | Symbol | Range | Factor | Character |
|---|---|---|---|---|
| Logarithmic scale | $\ln\rho$ | $\mathbb{R}$ | $\exp(\ln\rho)=\rho$ | central, positive, non-compact |
| Scalar phase | $\theta_{\mathrm{pha}}$ | $\mathbb{R}/2\pi\mathbb{Z}$ | $\exp(i\theta_{\mathrm{pha}})$ | central, compact, period $2\pi$ |
| Boost | $\theta_{\mathrm{rpd}}$ | $\mathbb{R}$ | $\exp(j\theta_{\mathrm{rpd}})=\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}$ | non-compact, hyperbolic |
| Split phase | $\theta_{\mathrm{phb}}$ | $\mathbb{R}/2\pi\mathbb{Z}$ | $\exp(ij\theta_{\mathrm{phb}})=\cos\theta_{\mathrm{phb}}+ij\sin\theta_{\mathrm{phb}}$ | compact, period $2\pi$ |

The two phases are not independent on the torus: the pair $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ is taken modulo the lattice $\Lambda=\langle2\pi(1,0),\pi(1,1)\rangle$, because $\exp(2\pi i)=1$ and $\exp(\pi i(1+j))=(-1)(-1)=1$. The exact kernel is computed in §*The Kernel and the Fibre*. On the principal diamond the pair is unique.

### The Factors

The modulus is the positive square root of $\breve Q\bar{\breve Q}$ in the cone $P$, and it is exponentiated by the split-complex exponential:

$$
\breve r=\sqrt{\breve Q\bar{\breve Q}}
=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr)=\exp(\ln\rho+j\theta_{\mathrm{rpd}}),
\qquad
\breve r_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}.
$$

The unit factor is the exponential of the angle:

$$
u=\breve r^{-1}\breve Q=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})=\exp(i\Theta),
\qquad
i\Theta=i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}.
$$

In the components the two factors read

$$
C_+=\rho_+e^{i\theta_+},
\qquad
C_-=\rho_-e^{i\theta_-},
\qquad
\rho_\pm=\rho e^{\pm\theta_{\mathrm{rpd}}},
\quad
\theta_\pm=\theta_{\mathrm{pha}}\pm\theta_{\mathrm{phb}}.
$$

The modulus has components $\rho_\pm$; the unit factor has components $e^{i\theta_\pm}$; their products are $C_\pm=\rho_\pm e^{i\theta_\pm}$. The table records the split.

| Factor | Formula | Components | Range | Exponent |
|---|---|---|---|---|
| Modulus | $\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})$ | $\rho_+=\rho e^{\theta_{\mathrm{rpd}}}$, $\rho_-=\rho e^{-\theta_{\mathrm{rpd}}}$ | cone $P$ | $\ln\rho+j\theta_{\mathrm{rpd}}$ |
| Unit factor | $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ | $e^{i\theta_+}$, $e^{i\theta_-}$ | torus $T^2$ | $i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ |
| Element | $\breve Q=\breve r u$ | $C_+=\rho_+e^{i\theta_+}$, $C_-=\rho_-e^{i\theta_-}$ | units | $\breve Q_{\log}$ |

The inverse change is

$$
\rho=\sqrt{\rho_+\rho_-},
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln\frac{\rho_+}{\rho_-},
\qquad
\theta_{\mathrm{pha}}=\tfrac12(\theta_++\theta_-),
\qquad
\theta_{\mathrm{phb}}=\tfrac12(\theta_+-\theta_-).
$$

The real dimensions are $2$ for the modulus and $2$ for the torus, and they add to the real dimension $4$ of the group of units.

### One Exponential

Because the algebra is commutative and the exponents commute,

$$
\breve Q=\exp(\breve r_{\log}+i\Theta)
=\breve r\,u
=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr)\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}).
$$

In full,

$$

\boxed{\;\breve Q=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr)\bigl(\cos\theta_{\mathrm{pha}}+i\sin\theta_{\mathrm{pha}}\bigr)\bigl(\cos\theta_{\mathrm{phb}}+ij\sin\theta_{\mathrm{phb}}\bigr)
\;}.
$$

The polar word is one exponential, not a product of independent exponentials with an ordering correction. The closed form of the exponential is

$$
\exp(X_{\blacktriangle}+jX_{\blacktriangledown})
=\exp(X_{\blacktriangle})\bigl(\cosh X_{\blacktriangledown}+j\sinh X_{\blacktriangledown}\bigr),
$$

which is the reduced Euler formula of *Reduced Biquaternion Elementary Functions*, §*The Exponential*. It reduces to $\exp(X_{\blacktriangle})$ when $X_{\blacktriangledown}=0$ and to $\cosh X_{\blacktriangledown}+j\sinh X_{\blacktriangledown}$ when $X_{\blacktriangle}=0$.

**Example.** For $\breve Q_{\log}=j\ln2$ the closed form gives

$$
\exp(j\ln2)=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34j.
$$

In the four coordinates, $\rho=1$, $\theta_{\mathrm{rpd}}=\ln2$ and $\theta_{\mathrm{pha}}=\theta_{\mathrm{phb}}=0$.

## Existence and Uniqueness

**Theorem.** The exponential is a bijection from the **principal domain**

$$

D=\Bigl\{\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}:\rho>0,\ \theta_{\mathrm{rpd}}\in\mathbb{R},\ \lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi\Bigr\}

$$

onto the unit group ${\mathbb{B}_{\mathrm{red}}}^\times$; the boundary of the diamond is taken half-open, so that each pair of angles $(\theta_+,\theta_-)\in(-\pi,\pi]^2$ has exactly one representative.

**Existence.** Let $\breve Q$ be a unit, so $C_+\neq0$ and $C_-\neq0$. Put

$$
\rho=\sqrt{\lvert C_+C_-\rvert},
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln\left\lvert\frac{C_+}{C_-}\right\rvert,
$$

and choose the principal arguments $\theta_\pm=\operatorname{Arg}C_\pm\in(-\pi,\pi]$. Put

$$
\theta_{\mathrm{pha}}=\tfrac12(\theta_++\theta_-),
\qquad
\theta_{\mathrm{phb}}=\tfrac12(\theta_+-\theta_-).
$$

Then $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert=\max(\lvert\theta_+\rvert,\lvert\theta_-\rvert)\le\pi$, and

$$
\rho e^{i\theta_{\mathrm{pha}}}e^{\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}}
=\lvert C_+\rvert e^{i\theta_+}=C_+,
\qquad
\rho e^{i\theta_{\mathrm{pha}}}e^{-\theta_{\mathrm{rpd}}-i\theta_{\mathrm{phb}}}
=\lvert C_-\rvert e^{i\theta_-}=C_-.
$$

Therefore

$$
\breve Q=\frac{C_++C_-}{2}+j\frac{C_+-C_-}{2}
=\rho e^{i\theta_{\mathrm{pha}}}\Bigl(\cosh(\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}})+j\sinh(\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}})\Bigr)
=\exp(\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}),
$$

with the exponent in $D$.

**Uniqueness.** Suppose $\exp\breve Q_{1\log}=\exp\breve Q_{2\log}$ with both exponents in $D$. Then the difference lies in the kernel of the exponential, computed in §*The Kernel and the Fibre* as

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

In the coordinates $(\ln\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ the kernel acts by

$$
(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\longmapsto(\theta_{\mathrm{pha}}+2\pi k+\pi l,\ \theta_{\mathrm{phb}}+\pi l),
\qquad k,l\in\mathbb{Z},
$$

with $\rho$ and $\theta_{\mathrm{rpd}}$ fixed. The diamond is a fundamental domain for this lattice: the linear change $(\theta_+,\theta_-)\mapsto(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ carries the fundamental square $(-\pi,\pi]^2$ of $2\pi\mathbb{Z}^2$ bijectively onto it. Two points of the diamond therefore differ by a kernel element only if they are equal. Hence $\breve Q_{1\log}=\breve Q_{2\log}$.

The theorem is the analogue of the principal strip of $\mathbb{C}$, with two phases instead of one. The parameters and their uniqueness are collected in the table.

| Parameter | Range | Unique? |
|---|---|---|
| $\ln\rho$ | $\mathbb{R}$ | yes: $\tfrac12\ln\lvert C_+C_-\rvert$ |
| $\theta_{\mathrm{rpd}}$ | $\mathbb{R}$ | yes: $\tfrac12\ln\lvert C_+/C_-\rvert$ |
| $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ | $\mathbb{R}^2/\Lambda$ | no in general; yes in the principal diamond |

## The Logarithm

### The General Logarithm

A **logarithm** of a unit $\breve Q$ is an element $\breve Q_{\log}$ with $\exp\breve Q_{\log}=\breve Q$. In the components it is

$$
\breve Q_{\log}=\frac{\log C_++\log C_-}{2}
+j\,\frac{\log C_+-\log C_-}{2},
$$

with an independent complex logarithm of each component. This is the **global formula** of *Reduced Biquaternion Elementary Functions*, §*The Logarithm*, written in the components. A logarithm exists exactly when both components are nonzero, that is exactly when $\breve Q$ is a unit. The general solution is

$$
\breve Q_{\log}=\operatorname{Log}\breve Q+2\pi i k+\pi i(1+j)l,
\qquad k,l\in\mathbb{Z},
$$

or, in the phases, the principal logarithm plus the lattice $\Lambda$.

**Example.** Take $\breve Q=3+4i+j(1-i)$, so $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. Then

$$
C_+=4+3i,
\qquad
C_-=2+5i,
$$

and the principal complex logarithms are

$$
\operatorname{Log}(4+3i)=1.6094379+0.6435011\,i,
\qquad
\operatorname{Log}(2+5i)=1.6836479+1.1902899\,i.
$$

The principal logarithm is

$$
\operatorname{Log}\breve Q=1.6465429+0.9168955\,i-0.0371050\,j-0.2733944\,ij.
$$

Exponentiating it back gives $3+4i+j(1-i)$ up to rounding. In the four coordinates, $\ln\rho=1.6465429$, $\theta_{\mathrm{rpd}}=-0.0371050$, $\theta_{\mathrm{pha}}=0.9168955$, $\theta_{\mathrm{phb}}=-0.2733944$.

### The Principal Logarithm

The **principal logarithm** is the formula of §*The General Logarithm* with the principal complex logarithm of each component, that is with the arguments in $(-\pi,\pi]$. In the four coordinates it is

$$
q_{\log\blacktriangle}=\tfrac12\ln\lvert C_+C_-\rvert,
\qquad
q'_{\log\blacktriangle}=\tfrac12\bigl(\operatorname{Arg}C_++\operatorname{Arg}C_-\bigr),
$$

$$
q_{\log\blacktriangledown}=\tfrac12\ln\left\lvert\frac{C_+}{C_-}\right\rvert,
\qquad
q'_{\log\blacktriangledown}=\tfrac12\bigl(\operatorname{Arg}C_+-\operatorname{Arg}C_-\bigr),
$$

with $\operatorname{Arg}$ the principal argument in $(-\pi,\pi]$. The phases satisfy

$$
\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert
=\max\bigl(\lvert\operatorname{Arg}C_+\rvert,\lvert\operatorname{Arg}C_-\rvert\bigr)\le\pi.
$$

The principal logarithm therefore lies in the principal diamond, and by §*Existence and Uniqueness* it is the unique logarithm there. It is defined on the whole unit group.

The principal logarithm is real-analytic on the complement of the two walls

$$
W_+=\{C_+\in(-\infty,0)\},
\qquad
W_-=\{C_-\in(-\infty,0)\},
$$

each of real dimension three, and it is discontinuous across them. A branch that continued analytically across a wall would have to continue by a period and would not be single-valued. The walls are the exact analogue of the negative real axis of $\mathbb{C}$; there is one wall for each component.

The two walls are not the zero divisors. The zero divisors are the two real two-planes $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$, on which $C_-=0$ or $C_+=0$; they lie in the closures of the walls. The walls are larger: a unit with $C_+=-1$ and $C_-=-2$ lies on both and has a perfectly good logarithm,

$$
\operatorname{Log}\breve Q=\frac{\ln2}{2}+i\pi-\frac{\ln2}{2}j,
$$

because both components are negative reals, with principal argument $\pi$.

No continuous single-valued branch exists on the whole unit group, because the unit group has fundamental group $\mathbb{Z}^2$; the obstruction is the kernel lattice, not a failure of local invertibility. The exponential is a covering map onto the unit group, and the logarithm is its multivalued inverse.

### The Kernel and the Fibre

The kernel of the exponential is the set of exponents with $\rho=1$, $\theta_{\mathrm{rpd}}=0$ and $u=1$, that is the set of $i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ with $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\in\Lambda$. In the algebra,

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}
=\bigl\{\pi i(k(1+j)+l(1-j)):k,l\in\mathbb{Z}\bigr\}.
$$

It is a rank-two lattice, generated by $2\pi i$ and $\pi i(1+j)$. The scalar period $2\pi i$ and the split period $2\pi ij$ generate only the sublattice of index two in the kernel. The two half-periods $\pi i(1+j)$ and $\pi i(1-j)$ are independent generators.

The fibre of the exponential over a unit $\breve Q$ is

$$
\exp^{-1}(\breve Q)=\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^2.
$$

In the phases the fibre is the orbit of $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ under $\Lambda$, and exactly one point of the orbit lies in the half-open diamond. The ambiguity is one integer for each component, the exact replacement of the single integer $2\pi i\mathbb{Z}$ of the complex case.

### The Exponent and the Logarithm

On this algebra the exponent is a logarithm of the element, and the two objects coincide: the decomposition $\breve Q=\exp\breve Q_{\log}$ says exactly that $\breve Q_{\log}\in\exp^{-1}(\breve Q)$. The polar data $(\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ are the representative of that fibre in the principal diamond, so the uniqueness is uniqueness modulo the lattice $\Lambda$. There is no discrete factor as in the split-complex case, and no canonical word distinct from the logarithm as in the biquaternion case; the exponent is the logarithm, read in the coordinates of the modulus and the torus.

## The Group Law

The exponential is a homomorphism from the additive group of the algebra to the multiplicative group of the units:

$$
\exp(\breve Q_{1\log}+\breve Q_{2\log})=\exp\breve Q_{1\log}\,\exp\breve Q_{2\log},
\qquad
\exp 0=1.
$$

In the four coordinates the law is

$$
\rho=\rho_1\rho_2,
\qquad
\theta_{\mathrm{rpd}}=\theta_{\mathrm{rpd},1}+\theta_{\mathrm{rpd},2},
\qquad
(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})=(\theta_{\mathrm{pha},1}+\theta_{\mathrm{pha},2},\ \theta_{\mathrm{phb},1}+\theta_{\mathrm{phb},2})\ \text{modulo}\ \Lambda.
$$

The radii multiply, the boosts add, and the phases add on the torus. In the components the law is the pair of complex laws $C_\pm(\breve Q_1\breve Q_2)=C_\pm(\breve Q_1)C_\pm(\breve Q_2)$. The group of units is therefore

$$
\boxed{\;{\mathbb{B}_{\mathrm{red}}}^\times\cong\mathbb{R}^2\times T^2\;},
$$

with the two real coordinates $\ln\rho$ and $\theta_{\mathrm{rpd}}$ and the two torus coordinates $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ modulo $\Lambda$. The exponential exhibits the group as the quotient of the additive group $\mathbb{R}^4$ by the kernel lattice,

$$
{\mathbb{B}_{\mathrm{red}}}^\times
\cong\mathbb{R}^4\big/2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

The four coordinates obey the following laws.

| Data | Law |
|---|---|
| Radius $\rho$ | multiplies |
| Boost $\theta_{\mathrm{rpd}}$ | adds |
| Phases $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ | add modulo $\Lambda$ |
| Exponent | adds |
| Group | ${\mathbb{B}_{\mathrm{red}}}^\times\cong\mathbb{R}^2\times T^2$ |

## The Matrix Picture

### The Matrix Exponential

In the complex basis $\{1,j\}$ the multiplication by $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ is the matrix

$$
M_{\breve Q_{\log}}
=\begin{pmatrix}Q_{\log\blacktriangle}&Q_{\log\blacktriangledown}\\Q_{\log\blacktriangledown}&Q_{\log\blacktriangle}\end{pmatrix}.
$$

The change of coordinates to the two components,

$$
(C_+,C_-)=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}),
$$

puts it in diagonal form:

$$
M_{\breve Q_{\log}}\longmapsto
\begin{pmatrix}\log C_+&0\\0&\log C_-\end{pmatrix}.
$$

The exponential of the matrix is therefore

$$
\exp M_{\breve Q_{\log}}\longmapsto
\begin{pmatrix}C_+&0\\0&C_-\end{pmatrix},
$$

which is $M_{\breve Q}$ in the same coordinates. In the original basis,

$$
M_{\breve Q}=\exp M_{\breve Q_{\log}}
=\begin{pmatrix}\exp(Q_{\log\blacktriangle})\cosh Q_{\log\blacktriangledown}&\exp(Q_{\log\blacktriangle})\sinh Q_{\log\blacktriangledown}\\
\exp(Q_{\log\blacktriangle})\sinh Q_{\log\blacktriangledown}&\exp(Q_{\log\blacktriangle})\cosh Q_{\log\blacktriangledown}\end{pmatrix}
=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}.
$$

In the real basis $\{1,i,j,ij\}$ the same identity is the exponential of a $4\times4$ matrix. Its block structure is two copies of the complex $2\times2$ matrix, and its determinant is $\lvert N\rvert^2$.

**Proposition (the derivative).** The derivative of the exponential at $\breve Q_{\log}$ is left multiplication by $\exp\breve Q_{\log}$:

$$

\boxed{\;d\exp_{\breve Q_{\log}}(\breve H)=\exp(\breve Q_{\log})\,\breve H
\;}.
$$

Its determinant is

$$
\det d\exp_{\breve Q_{\log}}
=\lvert Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\rvert^2
=\lvert C_+C_-\rvert^2=\rho_+^2\rho_-^2=\rho^4,
$$

and its singular values are $\rho_+,\rho_+,\rho_-,\rho_-$.

*Proof.* The derivative follows from $\exp(\breve Q_{\log}+t\breve H)=\exp\breve Q_{\log}\exp(t\breve H)$ and $\exp(t\breve H)=1+t\breve H+O(t^2)$. The matrix of left multiplication by $\breve Q$ has complex determinant $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=C_+C_-$ in the basis $\{1,j\}$, hence real determinant $\lvert C_+C_-\rvert^2$; and $\lvert C_+C_-\rvert=\rho_+\rho_-$. The singular values are those of $M_{\breve r}$, namely $\rho_+$ and $\rho_-$, each twice.

The exponential is conformal in each component coordinate, and conformal on the whole algebra exactly when $\rho_+=\rho_-$, that is when $\theta_{\mathrm{rpd}}=0$.

### The Matrix Logarithm and the Derivative

On the principal domain the matrix $M_{\breve Q_{\log}}$ is a logarithm of $M_{\breve Q}$ obtained by applying the principal scalar logarithm to each component: its diagonal entries $\operatorname{Log}C_\pm$ have imaginary parts in $(-\pi,\pi]$, so they are the principal logarithms of the components of $M_{\breve Q}$, and the two matrices are put in diagonal form by the same change of coordinates.

The logarithm is differentiable on the complement of the walls, and its derivative is left multiplication by $\breve Q^{-1}$:

$$
d\operatorname{Log}_{\breve Q}(\breve H)=\breve Q^{-1}\breve H.
$$

In the component coordinates,

$$
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_+=\frac{H_+}{C_+},
\qquad
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_-=\frac{H_-}{C_-}.
$$

*Proof.* The exponential is a local biholomorphism with derivative left multiplication by $\exp\breve Q_{\log}=\breve Q$; the inverse function theorem gives the derivative of the inverse as left multiplication by $\breve Q^{-1}$.

The formula is the exact analogue of $\operatorname{Log}'Q=1/Q$ in $\mathbb{C}$, applied twice. The logarithm is holomorphic in each component, and the two Wirtinger derivatives with respect to the conjugates of the components annihilate it.

## The Three Polar Decompositions

### The Three Forms

| Decomposition | Formula | Parameters | Domain | Uniqueness | Functions | Group reading |
|---|---|---|---|---|---|---|
| Modulus–unit | $\breve Q=\breve r u$ | $\breve r\in P$, $u\in T^2$ | all units | unique | square roots | $P\times T^2$ |
| Rational-chart | $\breve Q=\breve r\,u(s_1,s_2)$ | $\breve r\in P$, $(s_1,s_2)\in\mathbb{R}^2$ | units with $C_+,C_-\notin(-\infty,0]$ | unique on the chart | rational | four charts on $T^2$ |
| Exponential | $\breve Q=\exp\breve Q_{\log}$ | $\breve Q_{\log}$ modulo $\ker\exp$ | all units | unique in the principal domain | exponential and logarithm | $\mathbb{B}_{\mathrm{red}}/\ker\exp$ |

### The Modulus–Unit Form

The modulus–unit form of *Modulus–Unit Polar Decomposition of Reduced Biquaternions* is the same decomposition with the exponent split as

$$
\breve Q_{\log}=\breve r_{\log}+i\Theta,
\qquad
\breve r_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}\in\mathbb{R}\{1,j\},
\qquad
i\Theta=i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}\in\mathbb{R}\{i,ij\}.
$$

The logarithmic scale lies in the plane $\mathbb{R}\{1,j\}$, the angle in the plane $\mathbb{R}\{i,ij\}$, and the two commute. Exponentiating each factor gives

$$
\breve r=\exp(\breve r_{\log})=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}),
\qquad
u=\exp(i\Theta)=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}),
$$

and the product is the single exponential $\breve Q=\breve r u$. The modulus is global and algebraic, and no coordinate on the torus is chosen.

### The Rational-Chart Form

The rational-chart form of *Rational-Chart Polar Decomposition of Reduced Biquaternions* writes the unit factor as

$$
u(s_1,s_2)=\frac{c(s_1)+c(s_2)}{2}+j\,\frac{c(s_1)-c(s_2)}{2},
\qquad
c(s)=\frac{1-is}{1+is}.
$$

The chart coordinate and the angle are related in each component by

$$
s_\pm=-\tan\frac{\theta_\pm}{2},
\qquad
\theta_\pm=-2\arctan s_\pm,
$$

that is, in the phases,

$$
s_1=-\tan\frac{\theta_{\mathrm{pha}}+\theta_{\mathrm{phb}}}{2},
\qquad
s_2=-\tan\frac{\theta_{\mathrm{pha}}-\theta_{\mathrm{phb}}}{2}.
$$

The chart is rational in $s_k$ and in $u_k$, it misses the two circles on which a component is $-1$, and four charts cover the torus. The modulus is unchanged, so the rational-chart form differs from the exponential form only in the coordinate used on $T^2$.

### The Change of Coordinates

The change from the exponential phases to the rational coordinates is

$$
s_k=-\tan\frac{\theta_k}{2},
\qquad
\theta_k=-2\arctan s_k,
$$

transcendental and real-analytic on the principal strip $-\pi<\theta_k<\pi$. The endpoints $\theta_k=\pm\pi$ are sent to $s_k=\mp\infty$, the two ends of the real line, which are the same missing point $u_k=-1$ of the chart. The period lattice has no expression in the rational coordinates, which are coordinates on the circle itself rather than on its cover; the boundary survives only as the poles $s_1t_1=1$ and $s_2t_2=1$ of the group law.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is the group decomposition $P\times T^2$, algebraic and coordinate-free on the torus. The rational-chart form is the Cayley coordinate on the torus, rational and local. The exponential form is the Lie-algebra coordinate, global with the lattice quotient, and unique on the principal domain.

The exponential form is the only one in which the group law is addition. It is also the only one in which the non-uniqueness is a lattice: the kernel is $\mathbb{Z}^2$, and the principal diamond is a fundamental domain. The modulus–unit form has no non-uniqueness at all; the rational chart has a cut but no period.

| Property | Modulus–unit | Rational-chart | Exponential |
|---|---|---|---|
| Algebraic or transcendental | algebraic | rational | transcendental |
| Global on the units | yes | no | yes |
| Unique without a choice | yes | no | no |
| Non-uniqueness | none | a cut at a component $-1$ | the lattice $\Lambda$ |
| Group law | componentwise product | tangent addition | addition |
| Logarithm | none: a square root is used | none: the chart is rational | the exponent, a logarithm modulo $\Lambda$ |

## The Exponential Coordinates

### The Coordinate Map

The exponential coordinates are the four real functions

$$
(\ln\rho,\ \theta_{\mathrm{rpd}},\ \theta_{\mathrm{pha}},\ \theta_{\mathrm{phb}}),
$$

equivalently the real and imaginary parts of the two complex coordinates $Q_{\log\blacktriangle}=\ln\rho+i\theta_{\mathrm{pha}}$ and $Q_{\log\blacktriangledown}=\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}$ of the exponent.

Fixing the scales $\rho,\theta_{\mathrm{rpd}}$ and varying the phases gives the torus

$$
T^2=\{\exp(i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}):\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}\in\mathbb{R}\}.
$$

Fixing the phases and varying the scales gives the cone

$$
P=\{\exp(\ln\rho+j\theta_{\mathrm{rpd}}):\ln\rho\in\mathbb{R},\ \theta_{\mathrm{rpd}}\in\mathbb{R}\}
=\{\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}):\rho>0,\ \theta_{\mathrm{rpd}}\in\mathbb{R}\}.
$$

The product $P\times T^2$ is the unit group, and the exponential is the universal covering

$$
\mathbb{R}^2\times\mathbb{R}^2\longrightarrow P\times T^2
$$

with deck group $\Lambda\cong\mathbb{Z}^2$.

The surfaces $\rho=\mathrm{const}$ and $\theta_{\mathrm{rpd}}=\mathrm{const}$ are the surfaces of constant scale; their intersection is the torus of constant modulus. The surfaces $\theta_{\mathrm{pha}}=\mathrm{const}$ and $\theta_{\mathrm{phb}}=\mathrm{const}$ are the surfaces of constant phase; their intersection is the cone $P u$ of constant unit factor, a copy of $P$ rotated by $u$. The exponential maps the plane $\mathbb{R}\{1,j\}$ onto the cone $P$ and the plane $\mathbb{R}\{i,ij\}$ onto the torus $T^2$; each coordinate surface is the product of the image of a coordinate line in one plane with the other factor.

### The Jacobian and the Volume Element

In the Cartesian coordinates $(Q_{\blacktriangle},Q_{\blacktriangledown})\in\mathbb{C}^2\cong\mathbb{R}^4$ the Euclidean volume element is

$$
dV=d(\operatorname{Re}Q_{\blacktriangle})\,d(\operatorname{Im}Q_{\blacktriangle})\,d(\operatorname{Re}Q_{\blacktriangledown})\,d(\operatorname{Im}Q_{\blacktriangledown}).
$$

The complex-linear change to the components $(C_+,C_-)$ has real determinant $4$, so

$$
dV=\frac14\,d(\operatorname{Re}C_+)\,d(\operatorname{Im}C_+)\,
d(\operatorname{Re}C_-)\,d(\operatorname{Im}C_-).
$$

In the polar coordinates of the two components, with $\rho_\pm=\rho e^{\pm\theta_{\mathrm{rpd}}}$ and $\theta_\pm=\theta_{\mathrm{pha}}\pm\theta_{\mathrm{phb}}$, the area elements are $\rho_\pm\,d\rho_\pm\,d\theta_\pm$, and the change $(\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\mapsto(\rho_+,\theta_+,\rho_-,\theta_-)$ has determinant $4\rho$. Hence

$$
dV=\rho^3\,d\rho\,d\theta_{\mathrm{rpd}}\,d\theta_{\mathrm{pha}}\,d\theta_{\mathrm{phb}}
=\rho^4\,d(\ln\rho)\,d\theta_{\mathrm{rpd}}\,d\theta_{\mathrm{pha}}\,d\theta_{\mathrm{phb}}.
$$

The Jacobian determinant of the exponential, from the Cartesian volume in the exponent to the Cartesian volume in the algebra, is $\rho^4$, the same in either Cartesian reading. For a box

$$
[\ln\rho_+,\ln\rho_-]\times[\theta_{\mathrm{rpd},1},\theta_{\mathrm{rpd},2}]\times[\theta_{\mathrm{pha},1},\theta_{\mathrm{pha},2}]\times[\theta_{\mathrm{phb},1},\theta_{\mathrm{phb},2}]
$$

contained in the principal domain, the image has volume

$$
\frac{\rho_-^4-\rho_+^4}{4}\,(\theta_{\mathrm{rpd},2}-\theta_{\mathrm{rpd},1})(\theta_{\mathrm{pha},2}-\theta_{\mathrm{pha},1})(\theta_{\mathrm{phb},2}-\theta_{\mathrm{phb},1}),
$$

the integral of $\rho^3$ over the box. Outside the principal domain the same integral counts the image with multiplicity. The formula is exact.

### The Harmonic Reading

The functions $\ln\rho$ and $\theta_{\mathrm{rpd}}$ are harmonic in the component coordinates, being the real parts of the holomorphic functions $\tfrac12(\operatorname{Log}C_+\pm\operatorname{Log}C_-)$ away from the cuts, and the phases $\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ are harmonic on the cut plane, that is on the universal cover on which they are single-valued. The complex coordinates $\operatorname{Log}C_+$ and $\operatorname{Log}C_-$ are the local holomorphic coordinates supplied by the principal logarithm, and the exponential is their inverse.

The algebra carries two commuting complex structures: the left multiplication by $i$ and the left multiplication by $ij$. Both square to $-1$ and commute, and the two components are the coordinates in which the second is diagonal, with value $+i$ on $C_+$ and $-i$ on $C_-$. The exponential is holomorphic for both structures, because the closed form $\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})=\exp(Q_{\log\blacktriangle})(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown})$ is entire in $Q_{\log\blacktriangle}$ and in $Q_{\log\blacktriangledown}$. The obstruction to a global logarithm is the lattice, not the complex structure.

## Summary

### Main Results

| Result | Statement |
|---|---|
| Domain | the units $\breve Q\in{\mathbb{B}_{\mathrm{red}}}^\times$, that is $C_+C_-\neq0$ |
| Components | $C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ |
| Decomposition | $\breve Q=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ |
| Parameters | $\rho>0$, $\theta_{\mathrm{rpd}}\in\mathbb{R}$, $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})\in\mathbb{R}^2/\Lambda$ |
| Unit factor | $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})\in T^2$ |
| Exponent | $\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ |
| Existence | every unit has a decomposition |
| Uniqueness | unique in the principal diamond $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$ |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Fibre | $\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^2$ |
| Group law | the exponents add, modulo the kernel |
| Group | ${\mathbb{B}_{\mathrm{red}}}^\times\cong\mathbb{R}^2\times T^2$ |
| Matrix picture | block matrix in $\{1,j\}$; $\det d\exp=\rho^4$ |
| Coordinates | $(\ln\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$, with volume $\rho^3\,d\rho\,d\theta_{\mathrm{rpd}}\,d\theta_{\mathrm{pha}}\,d\theta_{\mathrm{phb}}$ |
| Component form | two independent complex polar decompositions, $C_\pm=\rho_\pm e^{i\theta_\pm}$ |

### Formulas

| Quantity | Formula |
|---|---|
| Element | $\breve Q=\tfrac12(C_++C_-)+j\tfrac12(C_+-C_-)$ |
| Components | $C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}=\rho e^{i\theta_{\mathrm{pha}}}e^{\pm(\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}})}$ |
| Exponent | $\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ |
| Modulus | $\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})$, with $\rho>0$, $\theta_{\mathrm{rpd}}\in\mathbb{R}$ |
| Unit factor | $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ |
| Decomposition | $\breve Q=\breve r\,u=\exp(\breve Q_{\log})$ |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Principal domain | $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$ |
| Group law | the exponent adds modulo $\Lambda$ |

Every unit $\breve Q$ has exactly one exponential polar decomposition in the principal domain,

$$
\breve Q=\exp(\breve Q_{\log}),
\qquad
\breve Q_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}},
$$

with

$$
\rho>0,\qquad
\theta_{\mathrm{rpd}}\in\mathbb{R},\qquad
\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi.
$$

In the two components,

$$
C_+=\rho e^{i\theta_{\mathrm{pha}}}e^{\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}},
\qquad
C_-=\rho e^{i\theta_{\mathrm{pha}}}e^{-\theta_{\mathrm{rpd}}-i\theta_{\mathrm{phb}}},
$$

and the four real coordinates are

$$
(\ln\rho,\ \theta_{\mathrm{pha}},\ \theta_{\mathrm{rpd}},\ \theta_{\mathrm{phb}})
=(q_{\log\blacktriangle},q'_{\log\blacktriangle},q_{\log\blacktriangledown},q'_{\log\blacktriangledown}).
$$

The exponent is the sum of the logarithmic scale $\ln\rho+j\theta_{\mathrm{rpd}}$ in the plane $\mathbb{R}\{1,j\}$ and the angle $i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ in the plane $\mathbb{R}\{i,ij\}$. The modulus is $\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})$ and the unit factor is $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$, and the polar word is the single exponential $\breve Q=\breve r u$.

The exponential is given by the closed form of *Reduced Biquaternion Elementary Functions*, §*The Exponential*:

$$
\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})
=\exp(Q_{\log\blacktriangle})\bigl(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown}\bigr),
$$

and it is a homomorphism. It is surjective onto the unit group and its kernel is the lattice

$$
2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2,
$$

generated by $2\pi i$ and $\pi i(1+j)$. The scalar and split periods $2\pi i$ and $2\pi ij$ generate a sublattice of index two. The logarithm exists for every unit and is unique only modulo this lattice; the principal diamond is a fundamental domain of area $2\pi^2$, and the exponential is a bijection from the product of the two real lines with the diamond onto the units.

The group law is addition in the exponential coordinates,

$$
{\mathbb{B}_{\mathrm{red}}}^\times\cong\mathbb{R}^2\times T^2
\cong\mathbb{R}^4\big/2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

The derivative is left multiplication by $\exp\breve Q_{\log}$; its determinant is $\rho_+^2\rho_-^2=\lvert C_+C_-\rvert^2=\rho^4$, and its singular values are $\rho_+,\rho_+,\rho_-,\rho_-$. The exponential is conformal in each component coordinate and conformal on the whole algebra exactly when $\theta_{\mathrm{rpd}}=0$.

### Comparison with the Neighbouring Cases

The table compares the three exponential polar decompositions; in the split-complex column, $\epsilon$ is the component sign.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Algebra | $\mathbb{R}[j]$, $j^2=1$ | $\mathbb{C}\otimes\mathbb{C}$ | $\mathbb{C}\otimes\mathbb{H}$ |
| Element | $Q=q+jq'$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tilde Q=Q_te_t+\vec Q$ |
| Parameters | $r>0$, $\theta_{\mathrm{rpd}}$, $\epsilon$ | $\rho>0$, $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{pha}}$, $\theta_{\mathrm{phb}}$ | $r>0$, $\theta_{\mathrm{pha}}$, $\theta_{\mathrm{rpd}}$, $\theta$, two axes |
| Discrete data | $(\mathbb{Z}/2)^2$ | lattice $\Lambda$ | none |
| Kernel | trivial | $\mathbb{Z}^2$ | not a subgroup |
| Matrix model | $2\times2$ real symmetric | $2\times2$ complex in $\{1,j\}$ | $2\times2$ complex |
| Group | $(\mathbb{Z}/2)^2\times\mathbb{R}^2$ | $\mathbb{R}^2\times T^2$ | $\mathbb{C}^{\times}\times SL(2,\mathbb{C})\cong\mathrm{GL}_2(\mathbb{C})$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{red}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | the reduced biquaternion algebra |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | the element, with scalar part $Q_{\blacktriangle}$ and split part $Q_{\blacktriangledown}$ |
| $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ | the two complex coefficients |
| $C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the two complex components |
| $N=C_+C_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | the reduced norm |
| $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ | the exponent |
| $Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle}=\ln\rho+i\theta_{\mathrm{pha}}$ | the scalar part of the exponent |
| $Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}=\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}$ | the split part of the exponent |
| $\rho>0$ | the radius, with logarithm $\ln\rho$ |
| $\theta_{\mathrm{rpd}}\in\mathbb{R}$ | the boost |
| $\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ | the two phases |
| $\Lambda=\langle2\pi(1,0),\pi(1,1)\rangle$ | the lattice of the phases |
| $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$ | the principal diamond |
| $\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})$ | the modulus |
| $\breve r_{\log}=\ln\rho+j\theta_{\mathrm{rpd}}$ | the logarithm of the modulus |
| $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ | the unit factor |
| $i\Theta=i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}$ | the angle |
| $P=\{\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}):\rho>0,\ \theta_{\mathrm{rpd}}\in\mathbb{R}\}$ | the cone of moduli |
| $T^2=\{\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}):\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}\in\mathbb{R}\}$ | the unit torus |
| $\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})=\exp(Q_{\log\blacktriangle})(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown})$ | the closed form of the exponential |
| $\operatorname{Log}\breve Q$ | the principal logarithm |
| $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ | the kernel of the exponential |
| $\rho_\pm=\rho e^{\pm\theta_{\mathrm{rpd}}}$ | the two component scales |
| $\theta_\pm=\theta_{\mathrm{pha}}\pm\theta_{\mathrm{phb}}$ | the two component arguments |
| $\det d\exp_{\breve Q_{\log}}=\rho^4$ | the Jacobian determinant |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the eight cases, the reconstruction tables and the boundary family.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-reduced-biquaternions.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Reduced Biquaternion Elementary Functions](reduced-biquaternion-elementary-functions.html), for the exponential and the logarithm as functions, the kernel and the principal domain.
- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the modulus, the torus and the uniqueness of the pair.
- [Rational-Chart Polar Decomposition of Reduced Biquaternions](rational-chart-polar-decomposition-of-reduced-biquaternions.html), for the rational coordinate on the torus.
- [Reduced Biquaternion Lie Group and Exponential Structure](reduced-biquaternion-lie-group-and-exponential-structure.html), for the kernel, the covering and the group of units.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-algebra-of-the-reduced-biquaternions.html), for the topology of the unit group.
- [Exponential Polar Decomposition of Complex Numbers](exponential-polar-decomposition-of-complex-numbers.html), for the one-coordinate exponential.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the hyperbolic exponential.
- *Exponential Polar Decomposition of Biquaternions*, for the noncommutative counterpart.
- [Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-a-reduced-biquaternion.html), for the relation with the eigenvalue decomposition.
- [Conventions in Mathematics](algebra-and-element-conventions.html), for the notation.
