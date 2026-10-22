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

The shape of the formula is forced by the image of the exponential. In $\mathbb{C}$ the exponential is onto $\mathbb{C}^\times$, so every nonzero $Q$ is $\exp(Q_{\log})$. In $\mathbb{D}$ the exponential is injective and its image is the future cone $F=\{Q:q>\lvert q'\rvert\}$ (*Split-Complex Special Functions*, §*The Split Complex Exponential and Logarithm*). A logarithm therefore exists exactly on $F$, and nowhere else. The four elements $\epsilon\in\{\pm1,\pm j\}$ permute the four components of $\mathbb{D}^\times$, and exactly one of the four products $\epsilon Q$ lies in $F$ (§*The Four Components*). The exponent is the logarithm of that product, and the discrete factor $\epsilon$ records the component of $Q$. It is not a period: the exponential has trivial kernel.

The element $Q_{\log}$ is the logarithm of $\epsilon Q$, the element that is exponentiated: $\exp(Q_{\log})=\epsilon Q$. It is a logarithm of $Q$ itself exactly when $\epsilon=1$. In coordinates, with $N=\langle Q\rangle_{*}=q^2-q'^2$, the derivation of §*The Data on the Future Cone*, applied to $\epsilon Q$, gives

$$
q_{\log}=\tfrac12\ln\lvert N\rvert=\ln r, \qquad
q'_{\log}=\operatorname{artanh}\frac{q'}{q}\ \ (N>0), \qquad
q'_{\log}=\operatorname{artanh}\frac{q}{q'}\ \ (N<0),
$$

the first branch covering the two timelike components and the second the two spacelike ones. The two coordinates, their formulas and their roles are tabulated in §*The Two Coordinates*.

The article derives the decomposition and the component sign (§*The Decomposition*), treats the logarithm and its domain (§*The Logarithm*), proves existence and uniqueness (§*Existence and Uniqueness*), gives examples (§*Worked Examples*), and then treats the matrix picture (§*The Matrix Picture*), the comparison with the two other polar forms (§*The Three Polar Decompositions*) and the exponential coordinates (§*The Exponential Coordinates*).

The symbols are those of *Split-Complex Algebra*, *Split-Complex Norm and Invertibility* and *Conventions in Mathematics*. Every numerical value displayed below was recomputed in double precision.

## The Decomposition

**Definition.** An **exponential polar decomposition** of $Q\in\mathbb{D}^\times$ is a writing

$$
Q=\epsilon\exp(Q_{\log}), \qquad \epsilon\in\{\pm1,\pm j\}, \quad Q_{\log}\in\mathbb{D},
$$

in which $\epsilon$ is the **component sign** and $Q_{\log}$ the **exponent**. In coordinates,

$$
q_{\log}=\operatorname{Re}Q_{\log}, \qquad q'_{\log}=\operatorname{Im}Q_{\log}.
$$

The subscript is a label, not an operation: $q_{\log}$ is the real coordinate of the exponent, not the logarithm of $q$.

### The Data on the Future Cone

Let $Q=q+jq'$ lie in the future cone $F$: $q>\lvert q'\rvert$, hence $q>0$ and $N=q^2-q'^2>0$. A logarithm of $Q$ is a number $Q_{\log}=x+jy$ with $\exp(Q_{\log})=Q$. The split Euler formula gives the two real equations

$$
\exp(x)\cosh y=q, \qquad \exp(x)\sinh y=q'.
$$

Squaring and subtracting eliminates $y$:

$$
\exp(2x)\bigl(\cosh^2y-\sinh^2y\bigr)=\exp(2x)=q^2-q'^2=N,
$$

so $x=\tfrac12\ln N$ is forced; it is real because $N>0$. Dividing the second equation by the first gives $\tanh y=q'/q$. Since $q>\lvert q'\rvert$, the ratio $q'/q$ lies in $(-1,1)$, and $y=\operatorname{artanh}(q'/q)$ is the unique solution. Conversely these values satisfy the two equations, because $\cosh(\operatorname{artanh}t)=1/\sqrt{1-t^2}$ and $\sinh(\operatorname{artanh}t)=t/\sqrt{1-t^2}$ with $t=q'/q$. Hence on the future cone

$$
Q_{\log}=\tfrac12\ln N+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

and the decomposition is $Q=\exp(Q_{\log})$. Writing

$$
r=\exp\Bigl(\tfrac12\ln N\Bigr)=\sqrt N>0, \qquad \phi=\operatorname{artanh}\frac{q'}{q}\in\mathbb{R},
$$

gives the same number in the two other forms:

$$
Q=r\bigl(\cosh\phi+j\sinh\phi\bigr)=r\exp(\phi j)=\exp(Q_{\log}).
$$

The first is the modulus–unit form; the last is the exponential polar decomposition, with component sign $\epsilon=1$.

This computation repeats the logarithm computation of *Split-Complex Special Functions*, §*The Split Complex Logarithm*, read as a decomposition; it does not define the exponential anew.

### The Four Components

**Lemma.** The four elements $\epsilon\in\{\pm1,\pm j\}$ act on the four components of $\mathbb{D}^\times$ simply transitively: for every $Q\in\mathbb{D}^\times$ there is exactly one $\epsilon$ with $\epsilon Q\in F$, and the four products $\epsilon Q$ lie in the four different components.

**Proof.** Write the idempotent coordinates

$$
Q_\pm=q\pm q', \qquad Q=Q_+\Pi_++Q_-\Pi_-, \qquad \Pi_\pm=\tfrac12(1\pm j).
$$

Multiplication is componentwise, $(QB)_\pm=Q_\pm B_\pm$, so $Q$ is invertible exactly when $Q_+Q_-=N\neq0$. The map $Q\mapsto(Q_+,Q_-)$ is a group isomorphism from $\mathbb{D}^\times$ onto $\mathbb{R}^\times\times\mathbb{R}^\times$. Each factor $\mathbb{R}^\times$ has two components, the positive and the negative half-line, so the product has $2\times2=4$ components, labelled by the sign pattern

$$
\bigl(\operatorname{sgn}Q_+,\operatorname{sgn}Q_-\bigr)\in\{+,-\}^2.
$$

The four elements have the four sign patterns:

| $\epsilon$ | $1$ | $-1$ | $j$ | $-j$ |
|---|---|---|---|---|
| $(\epsilon_+,\epsilon_-)$ | $(+,+)$ | $(-,-)$ | $(+,-)$ | $(-,+)$ |

For a general $Q$ the product $\epsilon Q$ has sign pattern $(\epsilon_+\operatorname{sgn}Q_+,\ \epsilon_-\operatorname{sgn}Q_-)$, because $(\epsilon Q)_\pm=\epsilon_\pm Q_\pm$. It lies in the future cone exactly when both signs are positive, that is exactly when $\epsilon_\pm=\operatorname{sgn}Q_\pm$. Exactly one of the four rows has that pair of signs. Hence exactly one $\epsilon$ works, and the four products $\epsilon Q$ carry the four sign patterns, so they lie in the four components.

The future cone is the $(+,+)$ component: $Q_+>0$ and $Q_->0$ mean $q+q'>0$ and $q-q'>0$, that is $q>\lvert q'\rvert$. The other three components are read the same way:

| region | condition | $(Q_+,Q_-)$ | component |
|---|---|---|---|
| future cone | $q>\lvert q'\rvert$ | $(+,+)$ | identity |
| past cone | $q<-\lvert q'\rvert$ | $(-,-)$ | $(-1)F$ |
| right spacelike | $q'>\lvert q\rvert$ | $(+,-)$ | $jF$ |
| left spacelike | $q'<-\lvert q\rvert$ | $(-,+)$ | $(-j)F$ |

### The Component Sign

The lemma gives the sign and the data in one table. The last two columns are obtained by applying §*The Data on the Future Cone* to $\epsilon Q$; they are derived after the table, not assumed.

| region | condition | $(Q_+,Q_-)$ | $\epsilon$ | $\epsilon Q$ | $q_{\log}$ | $q'_{\log}$ |
|---|---|---|---|---|---|---|
| future cone | $q>\lvert q'\rvert$ | $(+,+)$ | $1$ | $q+jq'$ | $\tfrac12\ln N$ | $\operatorname{artanh}\dfrac{q'}{q}$ |
| past cone | $q<-\lvert q'\rvert$ | $(-,-)$ | $-1$ | $-q-jq'$ | $\tfrac12\ln N$ | $\operatorname{artanh}\dfrac{q'}{q}$ |
| right spacelike | $q'>\lvert q\rvert$ | $(+,-)$ | $j$ | $q'+qj$ | $\tfrac12\ln(-N)$ | $\operatorname{artanh}\dfrac{q}{q'}$ |
| left spacelike | $q'<-\lvert q\rvert$ | $(-,+)$ | $-j$ | $-q'-qj$ | $\tfrac12\ln(-N)$ | $\operatorname{artanh}\dfrac{q}{q'}$ |

The norm of $\epsilon Q$ is the product of its idempotent coordinates,

$$
N(\epsilon Q)=(\epsilon_+Q_+)(\epsilon_-Q_-)=N,
$$

for $\epsilon=\pm1$, and $N(jQ)=q'^2-q^2=-N$, $N(-jQ)=-N$, for the spacelike rows. In the timelike rows $N>0$, in the spacelike rows $N<0$, so in every row $N(\epsilon Q)=\lvert N\rvert$. The formula of §*The Data on the Future Cone* applied to $\epsilon Q$ therefore gives

$$
q_{\log}=\tfrac12\ln N(\epsilon Q)=\tfrac12\ln\lvert N\rvert.
$$

The angle comes from the ratio of the two coordinates of $\epsilon Q$. For $\epsilon=\pm1$ the coordinates are $(\pm q,\pm q')$, so the ratio is $q'/q$. For $\epsilon=\pm j$ they are $(\pm q',\pm q)$, so the ratio is $q/q'$. The two cases are the two regimes of the table:

$$
q'_{\log}=
\begin{cases}
\operatorname{artanh}\dfrac{q'}{q}, & N>0,\\[2mm]
\operatorname{artanh}\dfrac{q}{q'}, & N<0.
\end{cases}
$$

In terms of the original $Q$ the sign is

$$
\epsilon=\operatorname{sgn}q\ \ (N>0), \qquad
\epsilon=j\operatorname{sgn}q'\ \ (N<0),
$$

which is the same rule as the table: $\operatorname{sgn}q=1$ gives $1$, $\operatorname{sgn}q=-1$ gives $-1$, $\operatorname{sgn}q'=1$ gives $j$, and $\operatorname{sgn}q'=-1$ gives $-j$.

### The Two Coordinates

The exponent has two real coordinates, and they play different roles.

| coordinate | formula | range | role |
|---|---|---|---|
| $q_{\log}=\operatorname{Re}Q_{\log}$ | $\tfrac12\ln\lvert N\rvert$ | $\mathbb{R}$ | logarithmic scale $\ln r$; one value, no branch |
| $q'_{\log}=\operatorname{Im}Q_{\log}$ | $\operatorname{artanh}\dfrac{q'}{q}$ if $N>0$; $\operatorname{artanh}\dfrac{q}{q'}$ if $N<0$ | $\mathbb{R}$ | hyperbolic angle $\phi$; one value on each component, no period |

The first coordinate is the same on the four components: it is fixed by the norm, $q_{\log}=\ln r=\tfrac12\ln\lvert N\rvert$, and carries the scale. The second depends on the component: the ratio is $q'/q$ on the two timelike components and $q/q'$ on the two spacelike ones, and it carries the hyperbolic angle. On each component the pair is unique, with no lattice of alternative values and no branch cut.

Read backwards, the pair gives the element:

$$
r=\exp(q_{\log})=\sqrt{\lvert N\rvert}, \qquad \phi=q'_{\log}, \qquad Q=r\,\epsilon\exp(\phi j).
$$

The exponent is a point $(q_{\log},q'_{\log})\in\mathbb{R}^2$, not a class modulo a lattice; the discrete data are the separate factor $\epsilon$.

### The Two Factors

The decomposition is also a product of a positive scale and a unit factor:

$$
Q=r\,\epsilon\exp(\phi j), \qquad
r=\exp(\ln r)=\sqrt{\lvert N\rvert}, \qquad
\epsilon\exp(\phi j)=\frac{Q}{r}.
$$

The scale is positive. The unit factor has norm $\operatorname{sgn}N$, because $N(\epsilon\exp(\phi j))=N(\epsilon)=\pm1$ according to the component, so it lies in the unit set $\{\lvert\langle u\rangle_{*}\rvert=1\}$. The four choices of $\epsilon$ label the four branches of that set, and $\phi$ is a coordinate on each branch. The table records the factors.

| factor | formula | range | coordinate | parameter |
|---|---|---|---|---|
| scale | $r=\exp(q_{\log})$ | $(0,\infty)$ | $q_{\log}=\ln r$ | $r>0$ |
| unit factor | $\epsilon\exp(\phi j)=Q/r$ | four branches, $\lvert N\rvert=1$ | $jq'_{\log}=j\phi$ | $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |

The unit factor is exactly the modulus–unit factor of *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, written in the exponential chart of its branch. The scale is non-compact and the unit factor is non-compact too: its identity branch is a line, not a circle.

### One Exponential and One Discrete Factor

The continuous part of the decomposition is one exponential:

$$
Q=\epsilon\exp(q_{\log})\exp(q'_{\log}j)=\epsilon\exp(Q_{\log}).
$$

The amalgamation uses the group law $\exp(Q_{1\log})\exp(Q_{2\log})=\exp(Q_{1\log}+Q_{2\log})$ and the commutativity of $\mathbb{D}$: the two scalar exponents $\ln r$ and $\phi j$ commute. The finite factor $\epsilon$ cannot be absorbed into the continuous exponential, because it changes the component. The decomposition therefore has one continuous exponent and one discrete component label.

In the coordinates $(\epsilon,q_{\log},q'_{\log})$ the group law is

$$
(\epsilon_1,q_{1\log},q'_{1\log})(\epsilon_2,q_{2\log},q'_{2\log})
=\bigl(\epsilon_1\epsilon_2,\ q_{1\log}+q_{2\log},\ q'_{1\log}+q'_{2\log}\bigr),
$$

because $\exp(Q_{1\log})\exp(Q_{2\log})=\exp(Q_{1\log}+Q_{2\log})$. The component multiplies in $(\mathbb{Z}/2\mathbb{Z})^2$, and the two coordinates add. Hence

$$
\mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2.
$$

### Why the Exponent Is Not a Logarithm of $Q$

The construction gives $\exp(Q_{\log})=\epsilon Q$, not $Q$. If $\epsilon=1$, then $Q_{\log}$ is a logarithm of $Q$. If $\epsilon\neq1$, then $Q$ is not an exponential at all: it lies in the component $\epsilon^{-1}F\neq F$, while the image of the exponential is $F$, so $Q$ has no logarithm. The factor $\epsilon$ is exactly what makes the logarithm exist, and the exponent is a logarithm of the element $\epsilon Q$.

This is the central difference from the complex case. There every nonzero element has a logarithm and the discrete factor is absent; here the logarithm exists on one component, and the discrete factor reaches the other three. The exponent is a point of $\mathbb{D}$, not a class modulo a lattice.

## The Logarithm

### The Inverse on the Future Cone

By *Split-Complex Special Functions*, §*The Split Complex Logarithm*, the exponential is injective and its image is $F$. Both facts are one line from the formula $\exp(x+jy)=\exp(x)(\cosh y+j\sinh y)$.

**Image.** Every exponential lies in $F$: its norm is $N(\exp(x+jy))=\exp(2x)>0$, and its real part is $\exp(x)\cosh y>0$. Conversely every element of $F$ is an exponential by §*The Data on the Future Cone*. Hence $\exp(\mathbb{D})=F$.

**Injectivity.** If $\exp(x_1+jy_1)=\exp(x_2+jy_2)$, then taking norms gives $\exp(2x_1)=\exp(2x_2)$, so $x_1=x_2$. The real and $j$-parts then give $\cosh y_1=\cosh y_2$ and $\sinh y_1=\sinh y_2$, hence $y_1=y_2$.

The inverse on $F$ is the logarithm. It is the element

$$
Q_{\log}=\tfrac12\ln\bigl(q^2-q'^2\bigr)+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

and the two compositions are exact inverses:

$$
\exp(Q_{\log})=Q \quad (Q\in F), \qquad
\log\bigl(\exp(Q_{\log})\bigr)=Q_{\log} \quad (Q_{\log}\in\mathbb{D}).
$$

There is no branch to choose, no principal value and no period. The kernel is $\{0\}$: if $\exp(Q_{\log})=1$, then $\exp(2q_{\log})=N(1)=1$ gives $q_{\log}=0$, and $\tanh q'_{\log}=0$ gives $q'_{\log}=0$. The exponential is not periodic, and $\exp(2\pi j)=\cosh(2\pi)+j\sinh(2\pi)\neq1$.

### The Domain of the Logarithm

The logarithm exists on one component of four and nowhere else.

| region | condition | logarithm of $Q$ |
|---|---|---|
| future cone | $q>\lvert q'\rvert$ | exists, unique, formula above |
| past cone | $q<-\lvert q'\rvert$ | none |
| spacelike wedges | $\lvert q'\rvert>\lvert q\rvert$ | none |
| null cone | $q=\pm q'$ | none |

The past cone and the spacelike wedges fail because they are the other components, while the image of the exponential is $F$; this is the content of §*The Four Components* and of the image statement above. The null cone is not in $\mathbb{D}^\times$: one idempotent coordinate vanishes, the norm vanishes, and the logarithm diverges rather than jumps. As $Q_-\to0^+$, for instance, $q'_{\log}=\tfrac12\ln\frac{q+q'}{q-q'}\to+\infty$. There is no branch cut and no periodicity to quotient out.

### The Fibre and the Quotient

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

## Existence and Uniqueness

**Theorem.** Every split-complex number $Q$ with $N\neq0$ has exactly one exponential polar decomposition

$$
Q=\epsilon\exp(Q_{\log}), \qquad Q_{\log}=q_{\log}+jq'_{\log}, \qquad
q_{\log}=\ln r, \quad q'_{\log}=\phi,
$$

with $\epsilon\in\{\pm1,\pm j\}$, $r>0$ and $\phi\in\mathbb{R}$; equivalently

$$
Q=r\,\epsilon\exp(\phi j), \qquad r=\sqrt{\lvert N\rvert}.
$$

The data are unique and are those of §*The Component Sign*:

$$
\epsilon=\operatorname{sgn}q\ (N>0),\quad \epsilon=j\operatorname{sgn}q'\ (N<0), \qquad
q_{\log}=\tfrac12\ln\lvert N\rvert, \qquad
q'_{\log}=
\begin{cases}
\operatorname{artanh}(q'/q), & N>0,\\
\operatorname{artanh}(q/q'), & N<0.
\end{cases}
$$

**Existence.** §*The Component Sign* gives $\epsilon$ with $\epsilon Q\in F$. §*The Data on the Future Cone* gives a number $Q_{\log}$ with $\exp(Q_{\log})=\epsilon Q$. Then $Q=\epsilon\exp(Q_{\log})=r\epsilon\exp(\phi j)$.

**Uniqueness.** Suppose $Q=\epsilon_1\exp(Q_{1\log})=\epsilon_2\exp(Q_{2\log})$ with $\epsilon_i\in\{\pm1,\pm j\}$ and $Q_{i\log}\in\mathbb{D}$. Multiplying by $\epsilon_i$ gives $\epsilon_iQ=\exp(Q_{i\log})\in F$ for $i=1,2$. By the uniqueness of the component sign in §*The Four Components*, $\epsilon_1=\epsilon_2$. Then $\exp(Q_{1\log})=\exp(Q_{2\log})$, and the injectivity of the exponential gives $Q_{1\log}=Q_{2\log}$. The coordinates of the exponent give $r=\exp(q_{\log})$ and $\phi=q'_{\log}$.

The decomposition is defined exactly on $\mathbb{D}^\times=\{Q:N\neq0\}$. On the null cone $N=0$ the modulus vanishes and no decomposition exists. The element $1+j$ is nonzero but has no decomposition; the domain is the group of units, not the set of nonzero elements.

## Worked Examples

### A Generic Split-Complex Number

Take $Q=5+3j$. Then $N=25-9=16$, $r=4$, and $Q$ lies in the future cone, so $\epsilon=1$. The two coordinates of the exponent are

$$
q_{\log}=\ln4=1.3862943611198906, \qquad
q'_{\log}=\operatorname{artanh}\frac{3}{5}=\ln2=0.6931471805599453,
$$

so $Q_{\log}=q_{\log}+jq'_{\log}=1.3862943611198906+0.6931471805599453\,j$.

The reconstruction is

$$
\exp(Q_{\log})=4\bigl(\cosh(\ln2)+j\sinh(\ln2)\bigr)=4(1.25+0.75j)=5+3j.
$$

### A Table of Examples

The error is the Euclidean modulus of the difference of the two coordinate pairs.

| $Q$ | $N$ | $r$ | $\epsilon$ | $\epsilon Q$ | $q_{\log}$ | $q'_{\log}$ | error |
|---|---|---|---|---|---|---|---|
| $5+3j$ | $16$ | $4$ | $1$ | $5+3j$ | $\ln4$ | $\ln2$ | $0$ |
| $-5-3j$ | $16$ | $4$ | $-1$ | $5+3j$ | $\ln4$ | $\ln2$ | $0$ |
| $3+5j$ | $-16$ | $4$ | $j$ | $5+3j$ | $\ln4$ | $\ln2$ | $0$ |
| $-3-5j$ | $-16$ | $4$ | $-j$ | $5+3j$ | $\ln4$ | $\ln2$ | $0$ |
| $1+2j$ | $-3$ | $\sqrt3$ | $j$ | $2+j$ | $0.5493061443$ | $0.5493061443$ | $2.2\times10^{-16}$ |
| $-1-2j$ | $-3$ | $\sqrt3$ | $-j$ | $2+j$ | $0.5493061443$ | $0.5493061443$ | $2.2\times10^{-16}$ |
| $-1+2j$ | $-3$ | $\sqrt3$ | $j$ | $2-j$ | $0.5493061443$ | $-0.5493061443$ | $2.2\times10^{-16}$ |
| $1-2j$ | $-3$ | $\sqrt3$ | $-j$ | $2-j$ | $0.5493061443$ | $-0.5493061443$ | $2.2\times10^{-16}$ |
| $j$ | $-1$ | $1$ | $j$ | $1$ | $0$ | $0$ | $0$ |
| $-j$ | $-1$ | $1$ | $-j$ | $1$ | $0$ | $0$ | $0$ |

The first four rows are the same future-cone element $5+3j$ reached by the four component signs. They have the same modulus and the same exponent and differ only by $\epsilon$. The four rows of $\pm1\pm2j$ show the two spacelike components and the two signs of the angle. The vertices $\pm j$ have exponent $0$ and are pure discrete factors. The label $\epsilon$ is not a period; it is the component of the unit factor.

### The Trivial Kernel and the Null Cone

The kernel is $\{0\}$ and there is no period:

$$
\exp(0)=1, \qquad
\exp(2\pi j)=\cosh(2\pi)+j\sinh(2\pi)=267.7467614837482+267.7448940410164\,j\neq1.
$$

The null cone is excluded. The element $1+j$ has $N=0$ and is nonzero but not invertible; its modulus vanishes, and no unit factor and no logarithm exist. The article never divides by $N$ on the null cone.

## The Matrix Picture

### The Exponential of a Symmetric Matrix

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

On the future cone the matrix $M_Q=\exp(q_{\log}I+q'_{\log}K)$ is symmetric positive definite, with eigenvalues $\exp(q_{\log}\pm q'_{\log})>0$. Its real symmetric logarithm is

$$
\log M_Q=\tfrac12\ln N\,I+\operatorname{artanh}\frac{q'}{q}\,K,
\qquad Q=q+jq',\quad q>\lvert q'\rvert.
$$

For a general $Q$ the matrix is $M_Q=M_\epsilon\exp(q_{\log}I+q'_{\log}K)$ with $M_\epsilon\in\{\pm I,\pm K\}$. The real symmetric logarithm exists only on the identity component; the other components are reached by the finite matrix $M_\epsilon$.

### The Euclidean Polar Factor

The Euclidean polar factor of $M_Q$ is $M_\epsilon$: it is $I$ on the future cone, $-I$ on the past cone, and a reflection on the spacelike region. The continuous factor $\exp(\phi j)$ is absorbed into the positive factor. The algebraic unit factor $\epsilon\exp(\phi j)$ and the Euclidean orthogonal factor $M_\epsilon$ are therefore different objects: the algebraic one contains the hyperbolic angle, the Euclidean one contains only the discrete sign. The matrix polar decomposition is treated in *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Matrix Polar Decomposition*.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $Q=ru$ | $r>0$, $\lvert\langle u\rangle_{*}\rvert=1$ | $\mathbb{D}^\times$ | unique | square root | $\mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2\mathbb{Z})^2$ |
| rational-chart | $Q=r\epsilon\dfrac{1-sj}{1+sj}$ | $r>0$, $\epsilon\in\{1,j,-j\}$, $s\neq\pm1$ | $\mathbb{D}^\times$ minus the negative real axis | unique on the chart | rational | local |
| exponential | $Q=r\epsilon\exp(\phi j)$ | $r>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ | $\mathbb{D}^\times$ | unique | exponential and logarithm | $(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ |

### The Modulus–Unit Form

The modulus–unit form is $Q=ru$ with $r=\sqrt{\lvert N\rvert}$ and $u=Q/r$. It is unique on $\mathbb{D}^\times$, uses the square root of the absolute norm, and is the product decomposition of the group of units. Its unit factor has norm $\operatorname{sgn}N$, so it lies on one of the four branches.

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

### The Coordinate Lines

On the identity component the coordinate lines are as follows.

| coordinate | image | geometry |
|---|---|---|
| $\ln r=\text{const}$ | $x^2-y^2=r^2$ | a hyperbola branch, a level set of the norm |
| $\phi=\text{const}$ | the ray $t(\cosh\phi,\sinh\phi)$, $t>0$ | a ray from the origin |

The other components are obtained by multiplying by $\epsilon$. The grid is hyperbolic polar. The curves of constant $\ln r$ are the hyperbolas of constant norm; the curves of constant $\phi$ are the rays of constant rapidity. There is no angular periodicity: $\phi$ runs over the whole line.

### The Jacobian and the Conformal Factor

The Jacobian of $(\ln r,\phi)\mapsto(x,y)=\exp(\ln r+\phi j)$ is

$$
J=\begin{pmatrix}\partial x/\partial\ln r&\partial x/\partial\phi\\ \partial y/\partial\ln r&\partial y/\partial\phi\end{pmatrix}
=\begin{pmatrix}x&y\\y&x\end{pmatrix},
\qquad
\det J=x^2-y^2=N(\epsilon Q)=r^2>0.
$$

For the full map $Q=\epsilon\exp(\ln r+\phi j)$ the Jacobian is multiplied by $M_\epsilon$, whose determinant is $+1$ for $\epsilon=\pm1$ and $-1$ for $\epsilon=\pm j$. The signed Jacobian is therefore $\det M_\epsilon\,r^2=N(Q)$: positive on the timelike components and negative on the spacelike ones.

The pullback of the indefinite metric on the chart is

$$
dx^2-dy^2=N(\epsilon Q)\bigl(d(\ln r)^2-d\phi^2\bigr)
=r^2\bigl(d(\ln r)^2-d\phi^2\bigr),
$$

because $dx=x\,d(\ln r)+y\,d\phi$ and $dy=y\,d(\ln r)+x\,d\phi$ cancel their cross terms. The chart is conformal for the indefinite metric with factor $N(\epsilon Q)=r^2>0$; on the full component the signed factor is $N(Q)$. There is no Euclidean conformal claim.

### The Harmonic Reading

The coordinates $\ln r$ and $\phi$ are linear, hence harmonic for the indefinite Laplacian $\square=\partial^2/\partial(\ln r)^2-\partial^2/\partial\phi^2$. The pair $(\ln r,\phi)$ is the global coordinate supplied by the logarithm on each component, and the exponential is its inverse. The logarithm is not global because its domain is one component of four; the obstruction is the discrete quotient $(\mathbb{Z}/2\mathbb{Z})^2$, not a period.

## Summary

The split-complex exponential is injective, and its image is the future cone $F=\{N>0,\ q>0\}$. On that cone the logarithm is unique,

$$
Q_{\log}=\tfrac12\ln N+j\operatorname{artanh}\frac{q'}{q},
\qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

and there is no branch, no period, and the kernel is $\{0\}$.

Every invertible split-complex number has exactly one exponential polar decomposition

$$
Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j),
\qquad
Q_{\log}=q_{\log}+jq'_{\log}, \quad q_{\log}=\ln r=\tfrac12\ln\lvert N\rvert, \quad q'_{\log}=\phi,
$$

with $r=\sqrt{\lvert N\rvert}>0$, $\phi\in\mathbb{R}$ and $\epsilon\in\{\pm1,\pm j\}$. The exponent $Q_{\log}$ is the logarithm of the element $\epsilon Q$ in the future cone, and $\epsilon$ is the component sign that makes $\epsilon Q$ lie there. The scale is $r$, the unit factor is $\epsilon\exp(\phi j)=Q/r$, and the discrete factor $\epsilon$ records the component. The group law is componentwise on $\epsilon$ and additive on the exponent, so $\mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ as groups.

The logarithm exists on one component and fails on the other three. The decomposition applies the logarithm to $\epsilon Q$, not to $Q$; this is the exact exchange of the complex case, where the logarithm exists everywhere and fails to be unique.

In the matrix picture the exponential of $xI+yK$ is $\exp(x)(\cosh y\,I+\sinh y\,K)$, symmetric positive definite on the identity component, with a unique real symmetric logarithm; the Euclidean orthogonal factor is the discrete matrix $M_\epsilon$. The exponential coordinates map each component onto $\mathbb{R}^2$, with signed Jacobian $N(Q)$ and indefinite conformal factor $r^2$. The map is not Euclidean conformal.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $N=\langle Q\rangle_{*}=q^2-q'^2$ | the norm |
| $r=\sqrt{\lvert N\rvert}$ | the modulus, a positive real |
| $q_{\log}=\ln r=\tfrac12\ln\lvert N\rvert$ | the logarithmic scale, the real coordinate of the exponent |
| $q'_{\log}=\phi$ | the hyperbolic angle, or rapidity, the $j$-coordinate of the exponent |
| $\epsilon\in\{\pm1,\pm j\}$ | the component sign |
| $Q_{\log}=q_{\log}+jq'_{\log}$ | the exponent of the decomposition: the logarithm of $\epsilon Q$, and of $Q$ itself when $\epsilon=1$ |
| $\exp$ | the exponential, defined in *Split-Complex Special Functions* |
| $\ker\exp=\{0\}$ | the kernel of the exponential |
| $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the reflection, $K^2=I$ |
| $M_Q=qI+q'K$ | the matrix of multiplication by $Q$ |
| $\operatorname{artanh}$ | the inverse hyperbolic tangent, $\lvert\cdot\rvert<1$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic functions and the split-complex exponential.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra, its idempotents and its exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the Lorentz group and its components.
