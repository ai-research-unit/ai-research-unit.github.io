# __Exponential Polar Decomposition of Split-Complex Numbers__

## Introduction

This article treats the **exponential polar decomposition** of an invertible split-complex number: the writing

$$
Q=\epsilon\exp(Q_{\log}), \qquad Q_{\log}=q_{\log}+jq'_{\log}, \qquad
q_{\log}=\ln r, \quad q'_{\log}=\phi,
$$

with $r>0$ the modulus, $\phi$ the hyperbolic angle, $\ln r$ the logarithmic scale, and $\epsilon\in\{\pm1,\pm j\}$ the component sign. Equivalently,

$$
Q=r\,\epsilon\exp(\phi j).
$$

The decomposition is the exponential form of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, which writes every invertible split-complex number as

$$
Q = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{D}, \quad \lvert \langle u\rangle_{*}\rvert = 1,
$$

with $r$ the modulus and $u$ the unit factor. The unit factor is written $u=\epsilon\exp(\phi j)$, with $\epsilon$ the component sign.

The exponential and the logarithm are those of *Split-Complex Elementary Functions*: the exponential is injective with image the future cone $F$, and the logarithm on $F$ is its two-sided inverse. §*The Analytic Setting* states them in the form used below, and they are not derived again. What the article owns is the decomposition itself, the component sign, its existence and uniqueness, the matrix picture and the exponential coordinates.

The shape of the formula is forced by the image of the exponential. In $\mathbb{C}$ the exponential is onto $\mathbb{C}^\times$, so every nonzero $Q$ is $\exp(Q_{\log})$. In $\mathbb{D}$ the exponential is injective and its image is the future cone $F=\{Q:q>\lvert q'\rvert\}$ (*Split-Complex Elementary Functions*, §*The Exponential*). A logarithm therefore exists exactly on $F$, and nowhere else. The four elements $\epsilon\in\{\pm1,\pm j\}$ permute the four components of $\mathbb{D}^\times$, and exactly one of the four products $\epsilon Q$ lies in $F$ (§*The Four Components*). The exponent is the logarithm of that product, and the discrete factor $\epsilon$ records the component of $Q$. It is not a period: the exponential has trivial kernel.

The element $Q_{\log}$ is the logarithm of $\epsilon Q$, the element that is exponentiated: $\exp(Q_{\log})=\epsilon Q$. It is a logarithm of $Q$ itself exactly when $\epsilon=1$. In coordinates, with $\langle Q\rangle_{*}=q^2-q'^2$, the logarithm formula of *Split-Complex Elementary Functions*, §*The Logarithm*, applied to $\epsilon Q$, gives one branch on the two timelike components and one on the two spacelike components. The two coordinates, their formulas and their roles are tabulated in §*The Exponent and Its Components*.

**The result.** The decomposition reads as follows.

| Item | Value |
|---|---|
| Algebra | $\mathbb{D}=\mathbb{R}[j]/(j^{2}-1)$ |
| Domain | $\mathbb{D}^{\times}=\{Q:\langle Q\rangle_{*}=q^{2}-q'^{2}\neq0\}$ |
| Decomposition | $Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j)$ |
| Parameters | $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |
| Unit factor | $\epsilon\exp(\phi j)=Q/r$, with $\lvert\langle u\rangle_{*}\rvert=1$ |
| Exponent | $Q_{\log}=\ln r+j\phi$, the logarithm of $\epsilon Q\in F$ |
| Existence | every unit has a decomposition |
| Uniqueness | $\epsilon$ and $Q_{\log}$ are both unique |
| Kernel | $\ker\exp=\{0\}$ |
| Group | $\mathbb{D}^{\times}\cong(\mathbb{Z}/2\mathbb{Z})^{2}\times\mathbb{R}^{2}$ |
| Companion | *Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number*, for the reading through the two real coordinates of $Q$ |
| Worked examples | *Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers*, for the eight cases and the reconstruction tables |

The plan is as follows. The analytic facts and the four components are recalled (§*The Analytic Setting*); the definition, the component sign, the exponent and its components, the factors and the single exponential are given (§*The Decomposition*); existence and uniqueness are proved (§*Existence and Uniqueness*); the logarithm, its domain and its fibre are read (§*The Logarithm*); the group law is stated (§*The Group Law*); the matrix picture is given (§*The Matrix Picture*); the three polar forms are compared (§*The Three Polar Decompositions*); the coordinates and the volume element are described (§*The Exponential Coordinates*); the numerical cases are collected in *Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers*. The logarithm is not derived again: §*The Exponent and Its Components* quotes the formula of *Split-Complex Elementary Functions*.

## The Analytic Setting

The decomposition rests on the exponential and the logarithm of *Split-Complex Elementary Functions*, and on the geometry of the four components of the unit group.

### The Exponential and the Logarithm

The exponential of $X=x+jy$ is

$$
\exp(X)=\exp(x)\bigl(\cosh y+j\sinh y\bigr).
$$

The table collects the properties used below.

| Property | Value |
|---|---|
| Closed form | $\exp(x+jy)=\exp(x)(\cosh y+j\sinh y)$ |
| Image | the future cone $F=\{Q:q>\lvert q'\rvert\}=\{\langle Q\rangle_{*}>0,\ q>0\}$ |
| Kernel | $\{0\}$: the exponential is injective and aperiodic |
| Logarithm | exists on $F$ and nowhere else, and is unique; $\tfrac12\ln \langle Q\rangle_{*}+j\operatorname{artanh}(q'/q)$ |
| Principal domain | $F$ itself |
| Fibre | one point on $F$, empty elsewhere |

These are the statements of *Split-Complex Elementary Functions*, §*The Exponential* and §*The Logarithm*. The present article adds the extension of the logarithm from $F$ to the four components, and the discrete factor that records the component.

### The Four Components

The group of units is $\mathbb{D}^{\times}=\{Q:\langle Q\rangle_{*}\neq0\}$. Its four components are the future cone and the past cone, where $\langle Q\rangle_{*}>0$, and the two spacelike wedges, where $\langle Q\rangle_{*}<0$:

$$
F=\{q>\lvert q'\rvert\},\qquad
P=\{q<-\lvert q'\rvert\},\qquad
R=\{q'>\lvert q\rvert\},\qquad
L=\{q'<-\lvert q\rvert\}.
$$

The four elements $\epsilon\in\{\pm1,\pm j\}$ act by multiplication and permute the components. The table gives the action and the logarithm of the product $\epsilon Q$, which lies in $F$ in every row.

| region | condition | $\langle Q\rangle_{*}$ | $\epsilon$ | $\epsilon Q$ | $q_{\log}$ | $q'_{\log}$ |
|---|---|---|---|---|---|---|
| future cone $F$ | $q>\lvert q'\rvert$ | $>0$ | $1$ | $q+jq'$ | $\tfrac12\ln \langle Q\rangle_{*}$ | $\operatorname{artanh}\dfrac{q'}{q}$ |
| past cone $P$ | $q<-\lvert q'\rvert$ | $>0$ | $-1$ | $-q-jq'$ | $\tfrac12\ln \langle Q\rangle_{*}$ | $\operatorname{artanh}\dfrac{q'}{q}$ |
| right spacelike $R$ | $q'>\lvert q\rvert$ | $<0$ | $j$ | $q'+qj$ | $\tfrac12\ln(-\langle Q\rangle_{*})$ | $\operatorname{artanh}\dfrac{q}{q'}$ |
| left spacelike $L$ | $q'<-\lvert q\rvert$ | $<0$ | $-j$ | $-q'-qj$ | $\tfrac12\ln(-\langle Q\rangle_{*})$ | $\operatorname{artanh}\dfrac{q}{q'}$ |

The check is direct. On $P$, the real part of $\epsilon Q=-q$ is positive and larger than $\lvert q'\rvert$; on $R$, the real part of $jQ=q'+qj$ is $q'>\lvert q\rvert$; on $L$, the real part of $-jQ=-q'-qj$ is $-q'>\lvert q\rvert$. In every row $\epsilon Q$ lies in $F$, and $\epsilon^2=1$, so $Q=\epsilon(\epsilon Q)$.

The four components are the cosets of $F$ in $\mathbb{D}^{\times}$, and the quotient is

$$
\mathbb{D}^{\times}/F\cong(\mathbb{Z}/2\mathbb{Z})^{2}.
$$

The group of units is therefore

$$
\mathbb{D}^{\times}\cong(\mathbb{Z}/2\mathbb{Z})^{2}\times\mathbb{R}^{2},
$$

the discrete factor being the component and the two real coordinates being $(\ln r,\phi)$. The isomorphism is made explicit in §*The Group Law*.

## The Decomposition

### The Definition

**Definition.** An **exponential polar decomposition** of $Q\in\mathbb{D}^\times$ is a writing

$$
Q=\epsilon\exp(Q_{\log}), \qquad \epsilon\in\{\pm1,\pm j\}, \quad Q_{\log}\in\mathbb{D},
$$

in which $\epsilon$ is the **component sign** and $Q_{\log}$ the **exponent**. In coordinates,

$$
q_{\log}=\operatorname{Re}Q_{\log}, \qquad q'_{\log}=\operatorname{Im}Q_{\log}.
$$

The subscript is a label, not an operation: $q_{\log}$ is the real coordinate of the exponent, not the logarithm of $q$.

### The Exponent and Its Components

Let $Q=q+jq'$ lie in the future cone $F$: $q>\lvert q'\rvert$, hence $\langle Q\rangle_{*}=q^2-q'^2>0$. The logarithm of *Split-Complex Elementary Functions*, §*The Logarithm*, gives at once

$$
Q_{\log}=\tfrac12\ln \langle Q\rangle_{*}+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

which is the formula of *Split-Complex Elementary Functions*, §*The Logarithm*, written in the coefficients. Writing

$$
r=\exp\Bigl(\tfrac12\ln \langle Q\rangle_{*}\Bigr)=\sqrt{\langle Q\rangle_{*}}>0,
\qquad
\phi=\operatorname{artanh}\frac{q'}{q}\in\mathbb{R},
$$

gives the same number in the three forms

$$
Q=r\bigl(\cosh\phi+j\sinh\phi\bigr)=r\exp(\phi j)=\exp(Q_{\log}).
$$

The reconstruction is immediate from the closed form: $\exp(Q_{\log})=\exp(q_{\log})(\cosh q'_{\log}+j\sinh q'_{\log})$, and the two coordinates are $\ln r$ and $\phi$. The first form is the modulus–unit form; the last is the exponential polar decomposition, with component sign $\epsilon=1$.

The exponent has two real components, and they play different roles.

| Component | Exponent | Range | Factor | Character |
|---|---|---|---|---|
| Scale | $q_{\log}=\operatorname{Re}Q_{\log}=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert$ | $\mathbb{R}$ | $\exp(q_{\log})=r$ | real, central; one value, no branch |
| Angle | $q'_{\log}=\operatorname{Im}Q_{\log}=\operatorname{artanh}\dfrac{q'}{q}$ if $\langle Q\rangle_{*}>0$, $\operatorname{artanh}\dfrac{q}{q'}$ if $\langle Q\rangle_{*}<0$ | $\mathbb{R}$ | $\exp(q'_{\log}j)=\cosh\phi+j\sinh\phi$ | hyperbolic, central; one value on each component, no period |

The first coordinate is the same on the four components: it is fixed by the norm, $q_{\log}=\ln r=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert$, and carries the scale. The second depends on the component: the ratio is $q'/q$ on the two timelike components and $q/q'$ on the two spacelike ones, and it carries the hyperbolic angle. On each component the pair is unique, with no lattice of alternative values and no branch cut.

Read backwards, the pair gives the element:

$$
r=\exp(q_{\log})=\sqrt{\lvert \langle Q\rangle_{*}\rvert}, \qquad \phi=q'_{\log}, \qquad Q=r\,\epsilon\exp(\phi j).
$$

The exponent is a point $(q_{\log},q'_{\log})\in\mathbb{R}^2$, not a class modulo a lattice; the discrete data are the separate factor $\epsilon$.

### The Component Sign

For a general unit $Q$, the component sign is the unique $\epsilon$ with $\epsilon Q\in F$. In the coefficients it is

$$
\epsilon=\operatorname{sgn}q\ \ (\langle Q\rangle_{*}>0), \qquad
\epsilon=j\operatorname{sgn}q'\ \ (\langle Q\rangle_{*}<0),
$$

the rule of the table of §*The Four Components*. The four possibilities are

| $\epsilon$ | $1$ | $-1$ | $j$ | $-j$ |
|---|---|---|---|---|
| region of $\epsilon Q$ | $F$ | $F$ | $F$ | $F$ |
| effect on $(q,q')$ | $(q,q')$ | $(-q,-q')$ | $(q',q)$ | $(-q',-q)$ |

In every case $\epsilon^2=1$. The sign is not a period of the exponential, because the exponential is injective; it is the label of the component, and it is forced by the requirement that the exponentiated element lie in the image.

### The Factors

The decomposition is also a product of a positive scale and a unit factor:

$$
Q=r\,\epsilon\exp(\phi j), \qquad
r=\exp(\ln r)=\sqrt{\lvert \langle Q\rangle_{*}\rvert}, \qquad
\epsilon\exp(\phi j)=\frac{Q}{r}.
$$

The scale is positive. The unit factor has norm $\operatorname{sgn}\langle Q\rangle_{*}$, because $\langle\epsilon\exp(\phi j)\rangle_{*}=\langle\epsilon\rangle_{*}=\pm1$ according to the component, so it lies in the unit set $\{\lvert\langle u\rangle_{*}\rvert=1\}$. The four choices of $\epsilon$ label the four branches of that set, and $\phi$ is a coordinate on each branch. The table records the factors.

| Factor | Formula | Range | Exponent | Parameter |
|---|---|---|---|---|
| Modulus | $r=\exp(q_{\log})$ | $(0,\infty)$ | $q_{\log}=\ln r$ | $r>0$ |
| Unit factor | $\epsilon\exp(\phi j)=Q/r$ | four branches, $\lvert\langle\epsilon\exp(\phi j)\rangle_{*}\rvert=1$ | $jq'_{\log}=j\phi$ | $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |

The unit factor is exactly the modulus–unit factor of *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, written in the exponential chart of its branch. The scale is non-compact and the unit factor is non-compact too: its identity branch is a line, not a circle.

### One Exponential

The continuous part of the decomposition is one exponential:

$$
Q=\epsilon\exp(q_{\log})\exp(q'_{\log}j)=\epsilon\exp(Q_{\log}).
$$

The amalgamation uses the group law $\exp(Q_{1\log})\exp(Q_{2\log})=\exp(Q_{1\log}+Q_{2\log})$ and the commutativity of $\mathbb{D}$: the two scalar exponents $\ln r$ and $\phi j$ commute. The finite factor $\epsilon$ cannot be absorbed into the continuous exponential, because it changes the component. The decomposition therefore has one continuous exponent and one discrete component label.

## Existence and Uniqueness

**Theorem.** Every split-complex number $Q$ with $\langle Q\rangle_{*}\neq0$ has exactly one exponential polar decomposition

$$
\boxed{\; Q=\epsilon\exp(Q_{\log}), \qquad Q_{\log}=q_{\log}+jq'_{\log}, \qquad
q_{\log}=\ln r, \quad q'_{\log}=\phi \;}
$$

with $\epsilon\in\{\pm1,\pm j\}$, $r>0$ and $\phi\in\mathbb{R}$; equivalently

$$
Q=r\,\epsilon\exp(\phi j), \qquad r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}.
$$

The data are those of §*The Four Components* and §*The Component Sign*:

$$
\epsilon=\operatorname{sgn}q\ (\langle Q\rangle_{*}>0),\quad \epsilon=j\operatorname{sgn}q'\ (\langle Q\rangle_{*}<0), \qquad
q_{\log}=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert, \qquad
q'_{\log}=
\begin{cases}
\operatorname{artanh}(q'/q), & \langle Q\rangle_{*}>0,\\
\operatorname{artanh}(q/q'), & \langle Q\rangle_{*}<0.
\end{cases}
$$

**Existence.** §*The Four Components* gives $\epsilon$ with $\epsilon Q\in F$. §*The Exponent and Its Components* gives a number $Q_{\log}$ with $\exp(Q_{\log})=\epsilon Q$. Then $Q=\epsilon\exp(Q_{\log})=r\epsilon\exp(\phi j)$.

**Uniqueness.** Suppose $Q=\epsilon_1\exp(Q_{1\log})=\epsilon_2\exp(Q_{2\log})$ with $\epsilon_i\in\{\pm1,\pm j\}$ and $Q_{i\log}\in\mathbb{D}$. Multiplying by $\epsilon_i$ gives $\epsilon_iQ=\exp(Q_{i\log})\in F$ for $i=1,2$. The four components are disjoint, so $\epsilon_1Q$ and $\epsilon_2Q$ lie in the same component only if $\epsilon_1=\epsilon_2$. Then $\exp(Q_{1\log})=\exp(Q_{2\log})$, and the injectivity of the exponential gives $Q_{1\log}=Q_{2\log}$. The coordinates of the exponent give $r=\exp(q_{\log})$ and $\phi=q'_{\log}$.

The decomposition is defined exactly on $\mathbb{D}^\times=\{Q:\langle Q\rangle_{*}\neq0\}$. On the null cone $\langle Q\rangle_{*}=0$ the modulus vanishes and no decomposition exists. The element $1+j$ is nonzero but has no decomposition; the domain is the group of units, not the set of nonzero elements. The parameters and their ranges are collected in one table.

| Parameter | Range | Unique? |
|---|---|---|
| $\epsilon$ | $\{\pm1,\pm j\}$ | yes: the component sign of $Q$ |
| $q_{\log}=\ln r$ | $\mathbb{R}$ | yes: $\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert$ |
| $q'_{\log}=\phi$ | $\mathbb{R}$ | yes: the angle of $\epsilon Q$ on its component |

## The Logarithm

### The Logarithm on a Component

*Split-Complex Elementary Functions*, §*The Logarithm*, gives the image, the injectivity and the inverse: $\exp(\mathbb{D})=F$, the kernel is $\{0\}$, and the inverse on $F$ is the logarithm

$$
\boxed{\; Q_{\log}=\tfrac12\ln\bigl(q^2-q'^2\bigr)+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert \;}
$$

and the two compositions hold as stated there. There is no branch to choose and no period: the kernel is $\{0\}$, and the exponential is not periodic.

### The Principal Domain

On this algebra the principal logarithm is the logarithm itself. The exponential is injective on $\mathbb{D}$ and its image is $F$, so a point of $F$ has exactly one logarithm and no branch is selected. The principal value is the formula of §*The Logarithm on a Component*, with the ordinary real logarithm of the positive norm. It is real-analytic on $F$ and diverges on the boundary. There is no cut to choose, because the boundary is the null cone and no point of $F$ lies on it; this is the sharpest difference from the reduced biquaternion and biquaternion cases, where the logarithm has a branch choice and cut walls.

The logarithm exists on one component of four and nowhere else.

| Region | Condition | Logarithm of $Q$ |
|---|---|---|
| Future cone | $q>\lvert q'\rvert$ | exists, unique |
| Past cone | $q<-\lvert q'\rvert$ | none |
| Spacelike wedges | $\lvert q'\rvert>\lvert q\rvert$ | none |
| Null cone | $q=\pm q'$ | none |

The past cone and the spacelike wedges fail because they are the other components, while the image of the exponential is $F$. The null cone is not in $\mathbb{D}^\times$: the norm vanishes, and the logarithm diverges rather than jumps. As $q^2-q'^2\to0^+$ inside $F$, for instance, the angle $\operatorname{artanh}(q'/q)\to+\infty$. The principal domain is $F$ itself: the exponential maps $\mathbb{D}$ bijectively onto $F$, so $\exp:\mathbb{D}\to F$ is bijective and $\log:F\to\mathbb{D}$ is its inverse.

### The Fibre

For $Q\in F$ the fibre of the exponential is a single point,

$$
\exp^{-1}(Q)=\{Q_{\log}\},
$$

and for $Q\notin F$ it is empty. In particular the fibre is not a lattice and there is no period: the kernel is $\{0\}$.

The quotient of the group of units by the image is

$$
\mathbb{D}^\times/\exp(\mathbb{D})=\mathbb{D}^\times/F\cong(\mathbb{Z}/2\mathbb{Z})^2.
$$

**Proof.** By §*The Four Components*, the map $\epsilon\mapsto\epsilon F$ is a bijection from $\{\pm1,\pm j\}$ onto the set of the four components. The components are the cosets of $F$, and the multiplication of cosets is the multiplication of the corresponding signs, which is the group law of $(\mathbb{Z}/2\mathbb{Z})^2$. Hence the quotient has four elements and the class of $\epsilon$ is $\epsilon F$.

### The Exponent and the Logarithm

The construction gives $\exp(Q_{\log})=\epsilon Q$, not $Q$. If $\epsilon=1$, then $Q_{\log}$ is a logarithm of $Q$. If $\epsilon\neq1$, then $Q$ is not an exponential at all: it lies in the component $\epsilon^{-1}F\neq F$, while the image of the exponential is $F$, so $Q$ has no logarithm. The factor $\epsilon$ is exactly what makes the logarithm exist, and the exponent is a logarithm of the element $\epsilon Q$.

This is the central difference from the complex case. There every nonzero element has a logarithm and the discrete factor is absent; here the logarithm exists on one component, and the discrete factor reaches the other three. The exponent is a point of $\mathbb{D}$, not a class modulo a lattice.

## The Group Law

The product of two decompositions is the decomposition of the product. With $Q_i=\epsilon_i\exp(Q_{i\log})$, the commutativity of $\mathbb{D}$ gives

$$
Q_1Q_2=(\epsilon_1\epsilon_2)\exp(Q_{1\log}+Q_{2\log}),
$$

and the right-hand side is already a decomposition: $\epsilon_1\epsilon_2\in\{\pm1,\pm j\}$ and the sum is in $\mathbb{D}$. In the coordinates the law is therefore

$$
(\epsilon_1,q_{1\log},q'_{1\log})(\epsilon_2,q_{2\log},q'_{2\log})
=\bigl(\epsilon_1\epsilon_2,\ q_{1\log}+q_{2\log},\ q'_{1\log}+q'_{2\log}\bigr).
$$

The component multiplies in $(\mathbb{Z}/2\mathbb{Z})^2$, and the two coordinates add. Hence

$$
\boxed{\; \mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2 \;}.
$$

On the future cone the law is the isomorphism $\exp:(F,+)\to(F,\cdot)$ of *Split-Complex Elementary Functions*; the polar coordinates extend it to the whole group by the discrete factor. The law is exact, not a Baker–Campbell–Hausdorff series. The table restates it.

| Data | Law |
|---|---|
| Component sign | multiplies in $(\mathbb{Z}/2\mathbb{Z})^2$ |
| Exponent | adds |
| Group | $\mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ |

## The Matrix Picture

### The Matrix Exponential

In the basis $\{1,j\}$, multiplication by $Q=q+jq'$ is

$$
M_Q=qI+q'K, \qquad
K=\begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad K^2=I.
$$

Since $I$ and $K$ commute,

$$
\exp(xI+yK)=\exp(x)\bigl(\cosh y\,I+\sinh y\,K\bigr)
=\exp(x)\begin{pmatrix}\cosh y&\sinh y\\\sinh y&\cosh y\end{pmatrix}.
$$

On the future cone the matrix $M_Q=\exp(q_{\log}I+q'_{\log}K)$ is symmetric positive definite, with positive diagonal entries.

### The Matrix Logarithm and the Derivative

The real symmetric logarithm of $M_Q$ on the future cone is

$$
\log M_Q=\tfrac12\ln \langle Q\rangle_{*}\,I+\operatorname{artanh}\frac{q'}{q}\,K,
\qquad Q=q+jq',\quad q>\lvert q'\rvert.
$$

For a general $Q$ the matrix is $M_Q=M_\epsilon\exp(q_{\log}I+q'_{\log}K)$ with $M_\epsilon\in\{\pm I,\pm K\}$; the real symmetric logarithm exists only on the identity component, and the other components are reached by the finite matrix $M_\epsilon$.

The derivative of the exponential at $X=xI+yK$ is left multiplication by $\exp X$,

$$
d\exp_X(H)=\exp(X)H,
$$

because $\exp(X+tH)=\exp(X)\exp(tH)=\exp(X)\bigl(I+tH+O(t^2)\bigr)$. The determinant of left multiplication by $Q$ is $\langle Q\rangle_{*}$, so

$$
\det d\exp_X=\langle\exp X\rangle_{*}=\exp(2x)>0.
$$

The derivative of the logarithm at $Q\in F$ is left multiplication by $Q^{-1}$, by the inverse function theorem.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $Q=ru$ | $r>0$, $\lvert\langle u\rangle_{*}\rvert=1$ | $\mathbb{D}^\times$ | unique | square root | $\mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2\mathbb{Z})^2$ |
| rational-chart | $Q=r\epsilon\dfrac{1-sj}{1+sj}$ | $r>0$, $\epsilon\in\{1,j,-j\}$, $s\neq\pm1$ | $\mathbb{D}^\times$ minus the negative real axis | unique on the chart | rational | local |
| exponential | $Q=r\epsilon\exp(\phi j)$ | $r>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ | $\mathbb{D}^\times$ | unique | exponential and logarithm | $(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ |

### The Modulus–Unit Form

The modulus–unit form is $Q=ru$ with $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}$ and $u=Q/r$. It is unique on $\mathbb{D}^\times$, uses the square root of the absolute norm, and is the product decomposition of the group of units. Its unit factor has norm $\operatorname{sgn}\langle Q\rangle_{*}$, so it lies on one of the four branches.

### The Rational-Chart Form

The rational-chart form writes the unit factor by the Cayley chart

$$
u(s)=\frac{1-sj}{1+sj}=\frac{1+s^2}{1-s^2}-j\frac{2s}{1-s^2},
\qquad s\neq\pm1,
$$

a bijection from $\mathbb{R}\setminus\{\pm1\}$ onto $\{\langle u\rangle_{*}=1\}\setminus\{-1\}$. The chart is rational and misses the negative real axis, where the unit factor is $-1$. The past timelike component is covered by the same $\epsilon=1$ chart on its negative branch; only the vertex $u=-1$ is missing. The spacelike components are reached by multiplying the chart by $j$ or $-j$.

### The Change of Coordinates

On the identity branch, comparing $u(s)$ with $u=\exp(\phi j)$ gives

$$
\frac{1-sj}{1+sj}=\exp\bigl(-2j\operatorname{artanh}s\bigr),
\qquad
s=-\tanh\frac{\phi}{2}, \quad \phi=-2\operatorname{artanh}s.
$$

On this branch $s$ runs over $(-1,1)$. The endpoints are the null directions, and the value $s=\pm\infty$ corresponds to the missing point $u=-1$. The hyperbolic angle is not periodic, so the chart is a coordinate on a line, not on a circle.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is global and algebraic, with a square root; the rational-chart form is rational and local, missing the negative real axis; the exponential form is global and transcendental, with a finite component label instead of a kernel. The exponential form is the only one in which the group law is addition, and the modulus–unit form the only one that is algebraic and global.

In $\mathbb{C}$ the exponential is onto $\mathbb{C}^\times$, the angle is periodic, and no discrete factor is needed. Here the image is one component and $\mathbb{D}^\times/\exp(\mathbb{D})\cong(\mathbb{Z}/2\mathbb{Z})^2$. The obstruction is a failure of existence, not a failure of uniqueness.

In a noncommutative algebra the amalgamation into one exponential fails; in the polar word of *Modulus–Unit Polar Decomposition of Biquaternions* the order of the factors carries information.

| Property | Modulus–unit | Rational-chart | Exponential |
|---|---|---|---|
| Algebraic or transcendental | algebraic | rational | transcendental |
| Global on the units | yes | no | yes |
| Unique without a choice | yes | no | yes |
| Non-uniqueness | none | a cut at $u=-1$ | none; the sign is discrete |
| Group law | componentwise product | tangent addition | addition, with the signs multiplying |
| Logarithm | none: a square root is used | none: the chart is rational | the exponent $Q_{\log}$, unique on each component |

The Euclidean polar factor of $M_Q$ is $M_\epsilon$: it is $I$ on the future cone, $-I$ on the past cone, and a reflection on the spacelike region. The continuous factor $\exp(\phi j)$ is absorbed into the positive factor. The algebraic unit factor $\epsilon\exp(\phi j)$ and the Euclidean orthogonal factor $M_\epsilon$ are therefore different objects: the algebraic one contains the hyperbolic angle, the Euclidean one contains only the discrete sign. The matrix polar decomposition is treated in *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Matrix Polar Decomposition*.

## The Exponential Coordinates

### The Coordinate Map

For each component sign $\epsilon$, the map

$$
\mathbb{R}^2\longrightarrow\epsilon\cdot(\text{future cone}),
\qquad
(\ln r,\phi)\longmapsto Q=\epsilon\exp(\ln r+\phi j)
$$

is a diffeomorphism: the inverse displayed below is smooth and the Jacobian is non-zero. The coordinates are the logarithmic scale $\ln r$ and the hyperbolic angle $\phi$; they are the coordinates $q_{\log}=\ln r$ and $q'_{\log}=\phi$ of the exponent. For $\epsilon Q=x+yj$ in the future cone, the inverse is

$$
\ln r=\tfrac12\ln(x^2-y^2), \qquad
\phi=\operatorname{artanh}\frac{y}{x}.
$$

The four charts cover $\mathbb{D}^\times$; their images are the four components, and their closures meet on the null cone, which is excluded.

On the identity component the coordinate lines are as follows.

| coordinate | image | geometry |
|---|---|---|
| $\ln r=\text{const}$ | $x^2-y^2=r^2$ | a hyperbola branch, a level set of the norm |
| $\phi=\text{const}$ | the ray $t(\cosh\phi,\sinh\phi)$, $t>0$ | a ray from the origin |

The other components are obtained by multiplying by $\epsilon$. The grid is hyperbolic polar. The curves of constant $\ln r$ are the hyperbolas of constant norm; the curves of constant $\phi$ are the rays of constant rapidity. There is no angular periodicity: $\phi$ runs over the whole line.

### The Jacobian and the Volume Element

The Jacobian of $(\ln r,\phi)\mapsto(x,y)=\exp(\ln r+\phi j)$ is

$$
J=\begin{pmatrix}\partial x/\partial\ln r&\partial x/\partial\phi\\ \partial y/\partial\ln r&\partial y/\partial\phi\end{pmatrix}
=\begin{pmatrix}x&y\\y&x\end{pmatrix},
\qquad
\det J=x^2-y^2=\langle\epsilon Q\rangle_{*}=r^2>0.
$$

For the full map $Q=\epsilon\exp(\ln r+\phi j)$ the Jacobian is multiplied by $M_\epsilon$, whose determinant is $+1$ for $\epsilon=\pm1$ and $-1$ for $\epsilon=\pm j$. The signed Jacobian is therefore $\det M_\epsilon\,r^2=\langle Q\rangle_{*}$: positive on the timelike components and negative on the spacelike ones.

The pullback of the indefinite metric on the chart is

$$
dx^2-dy^2=\langle\epsilon Q\rangle_{*}\bigl(d(\ln r)^2-d\phi^2\bigr)
=r^2\bigl(d(\ln r)^2-d\phi^2\bigr),
$$

because $dx=x\,d(\ln r)+y\,d\phi$ and $dy=y\,d(\ln r)+x\,d\phi$ cancel their cross terms. The chart is conformal for the indefinite metric with factor $\langle\epsilon Q\rangle_{*}=r^2>0$; on the full component the signed factor is $\langle Q\rangle_{*}$. There is no Euclidean conformal claim. The area element of the chart is

$$
dx\wedge dy=r^{2}\,d(\ln r)\wedge d\phi,
$$

with the sign of $\langle Q\rangle_{*}$ on the full component.

### The Harmonic Reading

The coordinates $\ln r$ and $\phi$ are linear, hence harmonic for the indefinite Laplacian $\square=\partial^2/\partial(\ln r)^2-\partial^2/\partial\phi^2$. The pair $(\ln r,\phi)$ is the global coordinate supplied by the logarithm on each component, and the exponential is its inverse. The logarithm is not global because its domain is one component of four; the obstruction is the discrete quotient $(\mathbb{Z}/2\mathbb{Z})^2$, not a period.

## Summary

### Main Results

| Result | Statement |
|---|---|
| Domain | $Q\in\mathbb{D}^\times$, that is $\langle Q\rangle_{*}=q^2-q'^2\neq0$ |
| Decomposition | $Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j)$ |
| Parameters | $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |
| Unit factor | $\epsilon\exp(\phi j)$ with $\lvert\langle u\rangle_{*}\rvert=1$ |
| Exponent | $Q_{\log}=\ln r+j\phi$, the logarithm of $\epsilon Q\in F$ |
| Existence | every unit has a decomposition |
| Uniqueness | the component sign and the exponent are both unique |
| Kernel | $\ker\exp=\{0\}$ |
| Fibre | one point on $F$, empty elsewhere: no lattice and no branch |
| Group law | the signs multiply and the two coordinates add |
| Group | $\mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ |
| Matrix picture | $M_Q=qI+q'K=M_\epsilon\exp(q_{\log}I+q'_{\log}K)$ |
| Coordinates | $(\ln r,\phi)$ on each component, with signed Jacobian $\det M_\epsilon\,r^2=\langle Q\rangle_{*}$ |
| Quotient | $\mathbb{D}^\times/F\cong(\mathbb{Z}/2\mathbb{Z})^2$ |
| Conformal factor | $dx^2-dy^2=r^2\bigl(d(\ln r)^2-d\phi^2\bigr)$; conformal for the indefinite metric only |

### Formulas

| Quantity | Formula |
|---|---|
| Element | $Q=q+jq'$ |
| Norm | $\langle Q\rangle_{*}=q^2-q'^2$ |
| Exponent | $Q_{\log}=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert+j\phi$ |
| Modulus | $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}>0$ |
| Unit factor | $\epsilon\exp(\phi j)$ |
| Decomposition | $Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j)$ |
| Kernel | $\ker\exp=\{0\}$ |
| Image | $F=\{\langle Q\rangle_{*}>0,\ q>0\}$ |
| Group law | $\epsilon$ multiplies in $(\mathbb{Z}/2\mathbb{Z})^2$, the exponent adds |

The split-complex exponential is injective, and its image is the future cone $F=\{\langle Q\rangle_{*}>0,\ q>0\}$. On that cone the logarithm is unique,

$$
Q_{\log}=\tfrac12\ln \langle Q\rangle_{*}+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

and there is no branch, no period, and the kernel is $\{0\}$.

Every invertible split-complex number has exactly one exponential polar decomposition

$$
Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j),
\qquad
Q_{\log}=q_{\log}+jq'_{\log}, \quad q_{\log}=\ln r=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert, \quad q'_{\log}=\phi,
$$

with $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}>0$, $\phi\in\mathbb{R}$ and $\epsilon\in\{\pm1,\pm j\}$. The exponent $Q_{\log}$ is the logarithm of the element $\epsilon Q$ in the future cone, and $\epsilon$ is the component sign that makes $\epsilon Q$ lie there. The unit factor $\epsilon\exp(\phi j)$ has norm of modulus $1$. The group law is componentwise on $\epsilon$ and additive on the exponent, so $\mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ as groups.

The logarithm exists on one component and fails on the other three. The decomposition applies the logarithm to $\epsilon Q$, not to $Q$; this is the exact opposite of the complex case, where the logarithm exists everywhere and fails to be unique.

In the matrix picture the exponential of $xI+yK$ is $\exp(x)(\cosh y\,I+\sinh y\,K)$, symmetric positive definite on the identity component, with a unique real symmetric logarithm; the Euclidean orthogonal factor is the discrete matrix $M_\epsilon$. The exponential coordinates map each component onto $\mathbb{R}^2$, with signed Jacobian $\langle Q\rangle_{*}$ and indefinite conformal factor $r^2$. The map is not Euclidean conformal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $\langle Q\rangle_{*}=q^2-q'^2$ | the norm |
| $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}$ | the modulus, a positive real |
| $q_{\log}=\ln r=\tfrac12\ln\lvert \langle Q\rangle_{*}\rvert$ | the logarithmic scale, the real coordinate of the exponent |
| $q'_{\log}=\phi$ | the hyperbolic angle, or rapidity, the $j$-coordinate of the exponent |
| $\epsilon\in\{\pm1,\pm j\}$ | the component sign |
| $Q_{\log}=q_{\log}+jq'_{\log}$ | the exponent of the decomposition: the logarithm of $\epsilon Q$, and of $Q$ itself when $\epsilon=1$ |
| $F=\{q>\lvert q'\rvert\}$ | the future cone, the image of the exponential |
| $P,R,L$ | the past cone and the two spacelike wedges, the other three components |
| $\exp$ | the exponential, defined in *Split-Complex Elementary Functions* |
| $\ker\exp=\{0\}$ | the kernel of the exponential |
| $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the reflection, $K^2=I$ |
| $M_Q=qI+q'K$ | the matrix of multiplication by $Q$ |
| $M_\epsilon$ | the matrix of multiplication by the component sign |
| $\operatorname{artanh}$ | the inverse hyperbolic tangent, $\lvert\cdot\rvert<1$ |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the eight cases, the reconstruction tables and the boundary family.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-split-complex-numbers.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the reading of the word through the two real coordinates of $Q$.
- [Split-Complex Elementary Functions](split-complex-elementary-functions.html), for the exponential, the logarithm and the future cone.
- [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), for the algebraic modulus–unit form.
- [Rational-Chart Polar Decomposition of Split-Complex Numbers](rational-chart-polar-decomposition-of-split-complex-numbers.html), for the rational coordinate on the unit factor.
- [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), for the group law and the Lie group structure.
- [Exponential Polar Decomposition of Complex Numbers](exponential-polar-decomposition-of-complex-numbers.html), for the case with no discrete factor.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the commutative four-dimensional case.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the noncommutative case, where the exponents do not add.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic functions and the split-complex exponential.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra and its exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the Lorentz group and its components.
