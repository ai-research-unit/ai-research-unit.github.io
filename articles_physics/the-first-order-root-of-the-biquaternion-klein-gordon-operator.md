# __The First-Order Root of the Biquaternion Klein–Gordon Operator__

## Introduction

The biquaternion Klein–Gordon operator has a first-order root, but it has no single one. Squaring a first-order operator to the central scalar $\Box-\mu^2$ needs four mutually anticommuting generators with $(iR_{e_x})^2=+1$ and $(iL_{e_k}R_{e_y})^2=-1$, the Lorentz signature; the biquaternion algebra supplies the three spatial ones, and the fourth needs a second factor. That factor doubles the minimal module to four complex dimensions. Write $iL_{e_\mu}R_{e_{\nu(\mu)}}$ for the four generators and $-iR_{e_z}$ for their volume element. With a pseudoscalar mass the single square exists; with the physical scalar mass only a factorisation exists, and the physical equation is one factor of it. The root therefore lives in the two-sided algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$, while $\Box$ itself remains central.

Here $iL_{e_\mu}R_{e_{\nu(\mu)}}$ is the generator cell of the coordinate $x_\mu$: $\nu(t)=x$ and $\nu(k)=y$, so that the time direction is carried by $iR_{e_x}=iL_{e_t}R_{e_x}$ and the three space directions by $iL_{e_k}R_{e_y}$ with $k=1,2,3$.

The equation is

$$
\left(\Box-\mu^2\right)\tilde\Phi=0,
\qquad
\mu=\frac{mc}{\hbar}.
$$

The companion *The Klein–Gordon Equation in Biquaternionic Form* records that the operator is central and scalar, that the equation decouples into four scalar equations, and that no scalar first-order operator in $\mathbb{B}$ has it as its square. The companion *Klein–Gordon from the Dirac Square in Biquaternionic Form* records the other side: a first-order equation exists, but it is spinor-valued and its mass couples two chiral halves. Together they leave Open Question 3 of the Klein–Gordon article: is the spinor root the only first-orderisation, and why four components?

There are two inequivalent senses of "first-order root", and the article treats both. A **single square** is one operator $D$ with $D^2=(\Box-\mu^2)I$. A **factorisation** is a product $D_-D_+=(\Box-\mu^2)I$ of two first-order factors; the physical equation is one factor, and the product is the Klein–Gordon operator. The single square is the stronger notion, and the physical mass does not admit it. The factorisation is the weaker notion, and the physical mass requires it.

Three results:

- **The root acts on four complex components.** The derivative part of a first-order operator $i\bigl(iR_{e_x}\partial/\partial Q_0-\sum_k iL_{e_k}R_{e_y}\partial/\partial Q_k\bigr)+B$, with the Lorentz generators, squares to the scalar $\Box I$ exactly when the four $iL_{e_\mu}R_{e_{\nu(\mu)}}$ mutually anticommute with $(iR_{e_x})^2=+1$ and $(iL_{e_k}R_{e_y})^2=-1$. They generate $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, whose smallest module is $\mathbb{C}^4$, of real dimension eight.
- **The algebra supplies three of the four.** The three $\vec e_k$ supply the spatial Clifford system inside $\mathbb{B}$. No fourth element of $\mathbb{B}$ anticommutes with all three, so the fourth acts on a second factor. In the regular picture that factor is the right copy $\mathbb{B}_R$, and the root lives in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$.
- **The mass term is constrained.** The condition $\{B,iL_{e_\mu}R_{e_{\nu(\mu)}}\}=0$ forces $B=c\,-iR_{e_z}$ with $c=\pm i\mu$. A single operator exists only with a **pseudoscalar** mass. A **scalar** mass commutes with the generators, so it admits only the factorisation, and the physical first-order equation is one factor.

The Clifford classification is standard. The identification of its generators with cells of the two-sided algebra is the corpus's dictionary, and the mass dichotomy read as the reason for the chiral pair is the synthesis offered here. Nothing in the article predicts a mass or a coupling.

### The d'Alembertian

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and central imaginary $i$. The coordinates are $Q_\mu$, with $Q_t=ict'$ on the material sector. The gradient is $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$, and the d'Alembertian is the single one of the series,

$$
\Box=\langle\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}\left(\tilde\nabla^{\natural}\tilde\nabla\right)
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q
=\Delta_Q-c^{-2}\frac{\partial^2}{\partial t'^2}
\quad\text{on }\mathbb{M}_- .
$$

In the $x$ coordinates $x_0=ct'$, $x_k$, where $Q_t=ix_0$ and $Q_k=x_k$, the same operator is
$$
\Box=-\sum_{\mu,\nu}g_{\mu\nu}\partial^2/\partial Q_\mu\partial Q_\nu
=-\frac{1}{c^2}\frac{\partial^2}{\partial t'^2}+\Delta ,
\qquad
g=\mathrm{diag}(+1,-1,-1,-1).
$$
The $Q$ form is the Euclidean transcription, obtained by $\partial/\partial Q_t=-ic^{-1}\partial/\partial t'$.

Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, and $\hbar$ is the reduced Planck constant.

## The Operator and Its Symbol

### The norm of the gradient

The d'Alembertian is central: it is a multiple of the identity as an operator, and it acts coefficient by coefficient,

$$
\Box\tilde Q_{\mathrm f}=\sum_\mu\left(\Box Q_{\mathrm f,\mu}\right)e_\mu .
$$

The gradient itself does not have this property. Its square is

$$
\tilde\nabla^2=\left(\frac{\partial^2}{\partial Q_t^2}-\Delta_Q\right)e_t+2\frac{\partial}{\partial Q_t}\vec\nabla,
$$

with a vector remainder. The scalar part of this square is $\partial^2/\partial Q_t^2-\Delta_Q$, not $\Box$; the norm is the scalar part of the conjugate product, $\tilde\nabla\tilde\nabla^\natural=\Box e_t$, where the conjugation flips the sign of the spatial part. The first-order root is therefore not $\tilde\nabla$ itself: the gradient is a first-order operator whose square is not central, while the root is a first-order operator whose square is central, a multiple of the identity. The root is a different object, and it is matrix-valued.

### The symbol and the mass shell

On a plane wave the gradient acts as left multiplication by the symbol $\tilde K_{\mathrm s}$. The sign of the exponential is immaterial below, because every condition is quadratic in the symbol. The corpus four-wavevector is $\tilde K=i\omega/c\,e_t+\vec k$, and the symbol is its $i$ multiple,

$$
\tilde K=\frac{\tilde P}{\hbar}=\frac{i\omega}{c}e_t+\vec k,
\qquad
\tilde K_{\mathrm s}=i\tilde K=\frac{i\tilde P}{\hbar}=-\frac{\omega}{c}e_t+i\vec k ,
\qquad
\tilde K_{\mathrm s}=K_te_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z .
$$

The norm of the symbol is the symbol of the d'Alembertian,

$$
\Box\;\longmapsto\;\langle\tilde K_{\mathrm s}\rangle_{\natural}
=\tilde K_{\mathrm s}\tilde K_{\mathrm s}^{\natural}
=\frac{\omega^2}{c^2}-|\vec k|^2 ,
$$

and the mass shell is the level set

$$
\langle\tilde K_{\mathrm s}\rangle_{\natural}=\mu^2
\quad\Longleftrightarrow\quad
\frac{\omega^2}{c^2}-|\vec k|^2=\frac{m^2c^2}{\hbar^2}
\quad\Longleftrightarrow\quad
E^2=\vec p^{\,2}c^2+m^2c^4 .
$$

Equivalently, on the shell $\langle\tilde K\rangle_{\natural}=-\mu^2$ and $\langle\tilde P\rangle_{\natural}=-m^2c^2$, with $\tilde P=iE/c\,e_t+\vec p$. The operator and its on-shell condition are the same norm, evaluated on the gradient and on the four-momentum. This is the structural fact that the rest of the article uses.

In the $x$ coordinates the four-wavevector has components $k_\mu=(\omega/c,\vec k)$, the spatial sign carried by the frame, $(iL_{e_k}R_{e_y})^2=-I$, rather than by a raised label. On the plane wave the root $i\bigl(iR_{e_x}\partial/\partial Q_0-\sum_k iL_{e_k}R_{e_y}\partial/\partial Q_k\bigr)$ has symbol $iR_{e_x}k_{0}-\sum_k iL_{e_k}R_{e_y}k_{k}$, whose square is $\sum_{\mu,\nu}g_{\mu\nu}k_\mu k_\nu I=(\omega^2/c^2-|\vec k|^2)I$, the symbol of $\Box$. A first-order operator with symbol $iR_{e_x}k_{0}-\sum_k iL_{e_k}R_{e_y}k_{k}+B$ is singular exactly when its determinant vanishes. If its square is $(\langle\tilde K_{\mathrm s}\rangle_{\natural}-\mu^2)I$, the determinant vanishes exactly on the mass shell, so the first-order equation has nonzero plane-wave solutions exactly where the Klein–Gordon equation does.

## The Root Condition

### The ansatz

Let

$$
D=i\,iL_{e_\mu}R_{e_{\nu(\mu)}}\frac{\partial}{\partial x_\mu}+B=i\,iR_{e_x}\frac{1}{c}\frac{\partial}{\partial t'}+i\,iL_{e_k}R_{e_y}\frac{\partial}{\partial x_k}+B,
\qquad
iL_{e_\mu}R_{e_{\nu(\mu)}},B\in M_n(\mathbb{C})\ \text{constant}.
$$

This is the most general first-order operator with constant coefficients and no derivative term beyond the first order. The matrices are constant because the classification below is a classification of the algebraic form; position-dependent coefficients are a separate problem, taken up in §*What the Root Does Not Carry*.

### The expansion

Because the partial derivatives commute, the quadratic term symmetrizes:

$$
D^2
=-\sum_{\mu,\nu}g_{\mu\nu}\frac{\partial^2}{\partial x_\mu\partial x_\nu}
+i\{iL_{e_\mu}R_{e_{\nu(\mu)}},B\}\frac{\partial}{\partial x_\mu}
+B^2 .
$$

The symmetrization is the legitimate substitution of commuting derivatives for the product; it is not an assumption about the matrices. Requiring

$$
D^2=\left(\Box-\mu^2\right)I_n
$$

gives three conditions: the derivative part reproduces the Clifford relation, the mass anticommutes with every generator, and its magnitude is fixed,
$$
\{iR_{e_x},B\}=\{iL_{e_k}R_{e_y},B\}=0,
\qquad
B^2=-\mu^2I_n .
$$

The first is the Clifford relation. The four cells $iR_{e_x}$ and $iL_{e_k}R_{e_y}$ carry the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$; see the appendix.

The second says the mass must anticommute with every generator. The third fixes the magnitude of the mass. The three are independent: the first is about the derivative part, the second about the mixing of the derivative and the mass, the third about the mass alone.

The signs are those of $\Box$ in the $x$ coordinates, where the metric is $g=\mathrm{diag}(+1,-1,-1,-1)$. The $Q$ coordinates carry the Euclidean transcription, in which all four generators square to $+1$ and the spatial ones acquire a factor $i$; that frame is not used here.

## Four Generators

### The Clifford algebra

Four generators with $\{iL_{e_\mu}R_{e_{\nu(\mu)}},iL_{e_\nu}R_{e_{\nu(\nu)}}\}=2g_{\mu\nu}$ generate the complex Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$. The algebra is simple, so every nonzero representation is faithful, and its smallest module is $\mathbb{C}^4$. A representation on $\mathbb{C}^2$ would be a two-dimensional module for $M_4(\mathbb{C})$, which does not exist. Hence

$$
n\ge 4,
$$

and $n=4$ is both minimal and realised. The real dimension of the minimal module is eight, the same as the real dimension of $\mathbb{B}$.

The counting can be seen without naming the algebra. Four anticommuting matrices in $M_n(\mathbb{C})$ generate, together with their products, $16$ linearly independent matrices: the identity, the four generators, the six products $iL_{e_\mu}R_{e_{\nu(\mu)}}\,iL_{e_\nu}R_{e_{\nu(\nu)}}$ with $\mu<\nu$, the four products $iL_{e_\mu}R_{e_{\nu(\mu)}}\,-iR_{e_z}$, and $-iR_{e_z}$. Sixteen independent matrices require $n^2\ge16$, hence $n\ge4$. The bound is attained by the five cell generators below.

The minimal realisation is explicit, and it uses both sides of the algebra. With $L_{a}R_{b}$,

$$
iL_{e_t}R_{e_x},
\qquad
iL_{e_x}R_{e_y},
\qquad
iL_{e_y}R_{e_y},
\qquad
iL_{e_z}R_{e_y},
\qquad
-iL_{e_t}R_{e_z},
$$

and the split of each cell between the two sides is

| $T$ | $L$ | $R$ |
|---|---|---|
| $iL_{e_t}R_{e_x}$ | $L_{e_t}=I$ | $R_{e_x}$ |
| $iL_{e_k}R_{e_y}$ | $iL_{e_k}$ | $R_{e_y}$ |
| $-iL_{e_t}R_{e_z}$ | $L_{e_t}=I$ | $-iR_{e_z}$ |

The fourth generator has $L=I$: it is a pure right multiplication, which is why the biquaternion algebra alone does not contain it. The three space generators have both factors. The split is what the next two subsections use: the three space generators carry a left factor from $\mathbb{B}$, the fourth carries only a right factor.

### Three inside the biquaternions

The biquaternion algebra contains three mutually anticommuting generators of square $-1$:

$$
\vec e_k^2=-e_t,
\qquad
\{\vec e_j,\vec e_k\}=0,\quad j\neq k .
$$

They act by left multiplication on a minimal left ideal $S\cong\mathbb{C}^2$, and their images are $-i$ times the Pauli matrices,

$$
\mathsf M_2(\vec e_x)=-i\sigma_1,
\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,
\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3 .
$$

So $\mathbb{B}$ supplies three of the four generators, and the module $S$ is two-dimensional.

No fourth element of $\mathbb{B}$ anticommutes with all three. Write a general element as $X=a_0e_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_0\vec e_x-2a_x e_t=0,
$$

which forces $a_0=a_x=0$. Anticommuting with $\vec e_y$ then forces $a_y=0$, leaving $X=a_z\vec e_z$. But this commutes with the third generator, so it does not anticommute with it. The only solution is $X=0$.

This is the coefficient proof of the Klein–Gordon article, read as a statement about the fourth generator. The obstruction is not that the algebra lacks room for a fourth direction; it is that the fourth direction cannot be a left multiplication.

### The fourth direction is the second side

The fourth generator acts on a second factor. The minimal module is

$$
\mathbb{C}^4\cong\mathbb{C}^2_{\mathrm{mult}}\otimes S,
$$

with $\mathbb{C}^2_{\mathrm{mult}}$ the multiplicity factor and $S$ the biquaternion spinor module. In this frame the four generators read

$$
iR_{e_x}=\sigma_1\otimes I_2,
\qquad
iL_{e_k}R_{e_y}=i\sigma_2\otimes\sigma_k,
\qquad
-iR_{e_z}=-\sigma_3\otimes I_2 .
$$

The first acts on the multiplicity factor alone and as the identity on $S$; the three space generators act on $S$ by $\sigma_k=\mathsf M_2(i\vec e_k)$, dressed by $i\sigma_2$ on the multiplicity, so their product squares to $-1$. The multiplicity factor is what $\mathbb{B}$ alone does not supply. Adjoining it is the passage to the two-sided algebra.

The cell form exhibits the same fact. The fourth generator is

$$
iL_{e_t}R_{e_x}=R_{i\vec e_x},
$$

a right multiplication, and it commutes with every left multiplication, so it lies in the commutant $\mathbb{B}_R$ of the left copy $\mathbb{B}_L$. A right multiplication is invisible to $\mathbb{B}_L$; this is the precise sense in which the fourth direction is the second side. The algebra generated by $\mathbb{B}_L$ and $\mathbb{B}_R$ is

$$
\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})\cong M_4(\mathbb{C}).
$$

The three space generators are cells that use both sides, $iL_{e_k}R_{e_y}$, and the anticommutator with $iR_{e_x}$ comes from the right factors, $R_{e_y}R_{e_x}=-R_{e_x}R_{e_y}$.

The real dimension count is consistent. The module $\mathbb{C}^4$ has real dimension eight, the same as $\mathbb{B}$. The root does not enlarge the field space relative to a biquaternion field; it changes the module structure. Relative to a single complex scalar, of course, it is a fourfold complex enlargement.

## The Mass Condition and the Two Masses

### The condition

The second root condition is

$$
\{B,iL_{e_\mu}R_{e_{\nu(\mu)}}\}=0\quad\text{for all }\mu .
$$

The anticommutant of the four generators is one-dimensional. If $B$ anticommutes with every $iL_{e_\mu}R_{e_{\nu(\mu)}}$, then $B\,-iR_{e_z}$ commutes with every $iL_{e_\mu}R_{e_{\nu(\mu)}}$. The four generate $M_4(\mathbb{C})$, whose commutant is $\mathbb{C}I$, so $B\,-iR_{e_z}=cI$ and $B=c\,-iR_{e_z}$.

The third condition then gives

$$
B^2=c^2\,(-iR_{e_z})^{2}=c^2I=-\mu^2I,
\qquad
c=\pm i\mu .
$$

So the single-square roots are

$$
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\,-iR_{e_z},
\qquad
\mathsf D=i\,iL_{e_\mu}R_{e_{\nu(\mu)}}\frac{\partial}{\partial x_\mu},
\qquad
\mathsf D_{\mathrm{ps},\pm}^2=\left(\Box-\mu^2\right)I .
$$

The mass term is proportional to $-iR_{e_z}$. It is a **pseudoscalar** mass.

### The single square

The pseudoscalar mass is not an accident of the construction. It is the only mass that anticommutes with all four generators. In the basis where $-iR_{e_z}$ is diagonal, the term $i\mu\,-iR_{e_z}$ is diagonal: it couples the left-handed part to itself and the right-handed part to itself, with opposite signs. It does not mix the chiralities.

The invariant statement is the anticommutator, not the matrix shape. The scalar mass commutes with $\mathsf D$; the pseudoscalar mass anticommutes with it. No change of frame alters which of the two holds, because the two conditions are statements about the algebra and not about a basis.

The corpus knows this channel. It is the $\chi$-type coupling of *The Dirac Equation in Biquaternionic Form*, the pseudoscalar potential that multiplies the central imaginary $i$ and is the $-iR_{e_z}$-type in the matrix dictionary. The single first-order root is therefore not new machinery; it is the corpus's pseudoscalar channel read as a mass.

The sign is fixed by the conventions:

$$
-iR_{e_z}=\rho(\chi),
$$

so the pseudoscalar mass reads $i\mu\,-iR_{e_z}\leftrightarrow i\mu\chi$ in the biquaternion dictionary. The chirality operator of the corpus is $\chi$; the matrix $-iR_{e_z}$ is its representative in the Lorentz frame, where $-iL_{e_t}R_{e_z}$.

The term is parity-odd. A parity-odd mass is not the mass of the Dirac equation, and it is not the mass the Standard Model generates. The single root exists, but it is not the physical one.

### The scalar mass and the factorisation

The physical mass is a scalar: it multiplies the identity and commutes with every generator. It fails the second condition,

$$
\{\mu I,iL_{e_\mu}R_{e_{\nu(\mu)}}\}=2\mu\,iL_{e_\mu}R_{e_{\nu(\mu)}}\neq0,
$$

so no single operator of the form $\mathsf D+B$ with a scalar mass squares to the Klein–Gordon operator. Each factor alone carries a first-order remainder:

$$
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
\qquad
\mathsf D_{\mathrm{sc},\pm}^2=\left(\Box+\mu^2\right)I\pm2\mu\mathsf D .
$$

The cross term is the price of the scalar mass. It cancels in the product:

$$
\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}
=\left(\mathsf D-\mu I\right)\left(\mathsf D+\mu I\right)
=\left(\Box-\mu^2\right)I .
$$

The physical first-order equation is one factor, $\mathsf D_{\mathrm{sc},-}\psi=0$ or $\mathsf D_{\mathrm{sc},+}\psi=0$; the other factor carries the opposite mass. The product is the Klein–Gordon operator, so each factor implies Klein–Gordon without squaring to it. This is the precise sense in which the scalar mass needs a pair: not two independent equations, but a factorisation whose two factors carry opposite mass. The algebraic content of the chiral pair of the corpus is the same factorisation,

$$
\tilde\nabla\tilde\Psi_R=\mu\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=\mu\tilde\Psi_R,
$$

whose $2\times2$ block matrix, multiplied by its opposite-mass partner, has $(\Box-\mu^2)I$ on the diagonal. The pair is the scalar-mass case written in the biquaternion chiral basis, not a second, independent root.

The dichotomy is therefore sharp:

- a **pseudoscalar** mass anticommutes with the generators and admits a single first-order operator whose square is Klein–Gordon;
- a **scalar** mass commutes with the generators and admits only the factorisation, whose physical factor is the Dirac equation.

The physical mass is the second. The corpus's use of the chiral pair is not an arbitrary choice of basis; it is the biquaternion form of the factorisation forced by the scalar mass.

### The scalar field has no root

A central scalar field has a one-dimensional module. Four nonzero scalars commute, so they cannot satisfy the Clifford relation. Equivalently, a one-dimensional module cannot carry $M_4(\mathbb{C})$. The Klein–Gordon field itself, taken as a central scalar, therefore has no first-order root. A first-order root requires promoting the field to the Clifford module. This is the no-go of the Klein–Gordon article, recovered as a module-dimension statement. The three cases are collected in the table.

| Field | Module | Mass matrix | Single square? | Structure |
|---|---|---|---|---|
| Central scalar | $\mathbb{C}$ | — | no | no root |
| Pseudoscalar-mass spinor | $\mathbb{C}^4$ | $i\mu\,-iR_{e_z}$ | yes | $\mathsf D_{\mathrm{ps},\pm}^2=(\Box-\mu^2)I$ |
| Scalar-mass spinor | $\mathbb{C}^4$ | $\mu I$ | no | $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}=(\Box-\mu^2)I$ |

### The determinant face

The corpus records two determinant identities for the gradient:

$$
\det A_+(\tilde\nabla)=\Box,
\qquad
\det\mathsf M_4^L(\tilde\nabla)=\Box^2,
$$

where $A_+(\tilde\nabla)$ is the chiral block of the left regular matrix. These are identities of the **even** face: a second-order scalar operator is the determinant of a first-order matrix. They are not a square root in the matrix sense. The determinant is a product of eigenvalues; a massless root is a single operator $D$ with

$$
D^2=\Box\,I .
$$

The two questions are different. The determinant identity says that the scalar wave operator is the determinant of a first-order matrix; the root asks for one first-order operator whose square is the scalar operator. The massless root has $\det\mathsf D=\Box^2$, the same determinant as the left regular matrix of the gradient. The massive root has

$$
\det\mathsf D_{\mathrm{ps},\pm}=\left(\Box-\mu^2\right)^2,
$$

which reduces to $\Box^2$ at $\mu=0$. The determinant depends on $\mu$ only through $\mu^2$, so the two roots $\pm i\mu$ give the same value. This is a consistency check on the classification, not a construction of the root.

## What the Root Does Not Carry

The classification is a statement of form, and its boundaries are part of the result.

1. **It is stronger than Klein–Gordon.** A first-order equation selects a subspace of the second-order solution space. The single root and the Dirac factor select different subspaces, and neither is equivalent to the second-order equation. The second-order equation has both frequency branches and all polarisations; a first-order equation has half of them. At $\mu=0$ the single root reduces to $\mathsf D$, whose kernel is the two Weyl halves, while the scalar-mass factorisation reduces to $\mathsf D^2=\Box$; the massless limit does not select one channel.
2. **No mass, no coupling, and no sign is predicted.** The classification says which first-order structures have the Klein–Gordon square; it does not say which one nature uses, and it does not determine $\mu$. The sign of the mass is not physical either: $\mathsf D_{\mathrm{ps},+}$ and $\mathsf D_{\mathrm{ps},-}$ are exchanged by $\mu\to-\mu$, so only the relative sign of the mass and the chirality is meaningful. Whether a pseudoscalar mass is realised is a dynamical question that the classification leaves open; the corpus's $\chi$-type coupling suggests an axial channel but supplies no dynamics.
3. **The coefficients are constant and the background flat.** Position-dependent coefficients add commutator terms, and a gauged derivative adds a field strength; the Clifford structure is then deformed, and the constant-coefficient classification is the starting point rather than the answer. On a curved background the partial derivatives become covariant derivatives and the Clifford algebra is the tangent-space algebra; the dimension count is unchanged, but the spin connection enters the root. The $x$ coordinates are flat; the $Q$ form is the Euclidean transcription of the same operator, not a different root.
4. **The real structure and the index are open.** The article works over $\mathbb{C}$. The two real forms of the Lorentzian complex algebra are $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ and $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$; the choice between them is the Majorana/Dirac question, and the charge-conjugation pairing is a real-structure question that this article does not settle. The massless root is odd under the chirality grading and $\Box$ is even, so the index of $\mathsf D$ is an invariant of the graded module; whether the biquaternion grading gives a nontrivial index on a gauge background is open.

## The Even and the Odd Face

The article's result can be stated as a division of labour between two matrix sizes.

- **The even face is $M_2$.** The Klein–Gordon operator is central; the determinant of the chiral block of the left regular matrix is $\Box$. The three generators $\vec e_k$ and the determinant identity live at the $M_2(\mathbb{C})$ level; the chiral pair is written in the biquaternion module before the fourth generator is adjoined.
- **The odd face is $M_4$.** The first-order structure — the single square $\mathsf D_{\mathrm{ps},\pm}$ or the Dirac factor of the scalar-mass case — needs the fourth generator, the multiplicity factor, and the two-sided algebra. For the single square, $\det\mathsf D_{\mathrm{ps},\pm}=(\Box-\mu^2)^2$, which reduces to $\Box^2$ at $\mu=0$ and matches the determinant of the left regular matrix of the gradient.

The division answers the $M_2$/$M_4$ question. The Klein–Gordon **equation** does not require $M_4$: its operator is central and its field can be a single complex scalar. The Klein–Gordon **root** does require $M_4$: the fourth Clifford direction is the second side of the algebra. The two statements are compatible because they are about different objects. The scalar equation lives in the centre; its first-order root lives in the two-sided algebra.

The regular representation's doubling is not a prediction of doubled particles. The two minimal left ideals are the two chiral copies of the same module; the doubling is the price of the fourth generator, not a doubling of the spectrum.

## Verification

The identities were recomputed before they were written. The cell frame was built from $L_{a}R_{b}$; the tensor description was built from the Pauli matrices and the $2\times2$ images of $\vec e_k$. The residuals are the largest absolute entries over the stated samples.

| Check | Result |
|---|---|
| $\{iL_{e_\mu}R_{e_{\nu(\mu)}},iL_{e_\nu}R_{e_{\nu(\nu)}}\}-2g_{\mu\nu}I$ | $0$ (exact) |
| $(-iR_{e_z})^{2}-I$ and $\{-iR_{e_z},iL_{e_\mu}R_{e_{\nu(\mu)}}\}$ | $0$ (exact) |
| $-iR_{e_z}-i\,iR_{e_x}\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}$ | $0$ (exact) |
| Tensor form satisfies the same Clifford relations | $0$ (exact) |
| Anticommutant of all four generators is one-dimensional | rank $15$, nullity $1$ |
| $\mathsf D_{\mathrm{ps},+}^2-(\Box-\mu^2)I$ on $100$ random $K$ | $2.4\times10^{-15}$ |
| $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}-(\Box-\mu^2)I$ on $100$ random $K$ | $3.6\times10^{-15}$ |
| $\left(iR_{e_x}k_{0}-\sum_k iL_{e_k}R_{e_y}k_{k}\right)^2-g_{\mu\nu}k_\mu k_\nu I$ | $2.5\times10^{-15}$ |
| $\det\mathsf D_{\mathrm{ps},\pm}-(\Box-\mu^2)^2$ on $100$ random $K$ | $2.3\times10^{-13}$ |
| Frame squares $(+1,-1,-1,-1)$ and anticommutators | $0$ (exact) |

The numerical checks are checks of polynomial identities at random points. The proof is the algebra of the preceding sections; the numbers guard against a sign or factor error in the transcription.

## Summary

The first-order root of the biquaternion Klein–Gordon operator exists, and its size is fixed by the norm form. The root acts on a module of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, whose minimal module is $\mathbb{C}^4$. The biquaternion algebra supplies the three spatial generators $\vec e_x,\vec e_y,\vec e_z$, and no fourth; the fourth (time) generator acts on the multiplicity factor and, in the regular picture, is the right multiplication $R_{i\vec e_x}$, which lies in the commutant $\mathbb{B}_R$. The root therefore lives in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$, while the Klein–Gordon operator itself remains central.

The mass term is constrained by $\{B,iL_{e_\mu}R_{e_{\nu(\mu)}}\}=0$. The only single-operator solution is $B=\pm i\mu\,-iR_{e_z}$, a pseudoscalar mass. A scalar mass commutes with the generators, so no single operator with a scalar mass squares to Klein–Gordon; the scalar mass admits only the factorisation $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}$, which is the corpus's chiral pair. The physical mass is the scalar one, so the physical first-order equation is one factor of that factorisation.

The scalar Klein–Gordon field, taken as a central scalar, has no first-order root. The results are a classification of form: no mass, no coupling, and no dynamics are predicted. The open questions are the gauged, curved, position-dependent, and real-structure extensions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $Q_\mu$ | Algebra coordinates, $Q_t=ict'$ on $\mathbb{M}_-$ |
| $x_\mu$ | Lorentz coordinates, $x_0=ct'$, $x_k$ spatial |
| $g_{\mu\nu}$ | Lorentz metric, $\mathrm{diag}(+1,-1,-1,-1)$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\partial^2/\partial Q_t^2+\Delta_Q=-\sum_{\mu,\nu}g_{\mu\nu}\partial^2/\partial Q_\mu\partial Q_\nu$ | d'Alembertian, series convention and Lorentz form |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $\mu=mc/\hbar$ | Mass parameter (inverse reduced Compton wavelength) |
| $\tilde P=iE/c\,e_t+\vec p$ | Material four-momentum |
| $\tilde K=\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Corpus four-wavevector |
| $\tilde K_{\mathrm s}=i\tilde K$ | Symbol of the gradient; $K_\mu$ its components |
| $\langle\tilde K_{\mathrm s}\rangle_{\natural}=\mu^2$ | Mass shell |
| $iL_{e_\mu}R_{e_{\nu(\mu)}}$ | Generators of the root, $\{iL_{e_\mu}R_{e_{\nu(\mu)}},iL_{e_\nu}R_{e_{\nu(\nu)}}\}=2g_{\mu\nu}I$ |
| $-iL_{e_t}R_{e_z}$ | Pseudoscalar generator, $-iL_{e_t}R_{e_z}=\rho(\chi)$ |
| $\mathsf D=i\bigl(iR_{e_x}\partial/\partial x_0-\sum_k iL_{e_k}R_{e_y}\partial/\partial x_k\bigr)$ | Lorentz-frame Dirac operator, $\mathsf D^2=\Box I$ |
| $iR_{e_x}k_{0}-\sum_k iL_{e_k}R_{e_y}k_{k}$ | Symbol of $\mathsf D$ on a plane wave, $k_\mu=(\omega/c,\vec k)$ |
| $\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\,-iR_{e_z}$ | Single-square roots |
| $\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I$ | Scalar-mass factors |
| $S\cong\mathbb{C}^2$ | Minimal left ideal (biquaternion spinor module) |
| $L_a,R_b$ | Left and right multiplication operators |
| $L_{a}R_{b}$ | Two-sided cell |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the identity $(\mathsf D-\mu)(\mathsf D+\mu)=\Box-\mu^2$ and the plane-wave spinors.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra, the gamma matrices, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the classification of Clifford algebras, the minimal modules, and the square root of the wave operator.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the complex and real Clifford algebras and their irreducible modules.
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the periodicity and the module dimensions.
- V. V. Kravchenko, *Quaternionic Analysis and Its Applications* (Birkhäuser, 2003), for the quaternionic Dirac operator and its relation to the Euclidean Clifford algebra.
- The corpus articles *The Klein–Gordon Equation in Biquaternionic Form*, *Klein–Gordon from the Dirac Square in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form*, *The Biquaternion D'Alembertian and Its Green's Functions*, and *Algebra and Element Conventions* for the conventions and the results this article builds on.
- The corpus articles *Two-Sided Operators on the Biquaternion Algebra*, *Element and Operator Representations: The Three Actions*, and *Spinors as Peirce Coordinates in the Biquaternion Algebra* for the two-sided algebra, the nilpotent that swaps the minimal left ideals, and the $M_2$/$M_4$ dictionary.

## Appendix — The Gamma Formulation

The gammas are the five cells of the body, written as matrices:
$$
\gamma_0=iL_{e_t}R_{e_x},\qquad
\gamma_1=iL_{e_x}R_{e_y},\qquad
\gamma_2=iL_{e_y}R_{e_y},\qquad
\gamma_3=iL_{e_z}R_{e_y},\qquad
\gamma_5=-iL_{e_t}R_{e_z}.
$$
They satisfy $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$, $(\gamma_0)^2=+I_4$, $(\gamma_k)^2=-I_4$ and $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$.

In the tensor frame the same five are
$$
\gamma_0=\sigma_1\otimes I_2,\qquad
\gamma_k=i\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2,
$$
and the split between the two sides is the cell table of §*Four Generators*.

The root and the mass conditions read in gammas as
$$
\mathsf D=i\gamma_\mu\frac{\partial}{\partial x_\mu},\qquad
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\gamma_5,\qquad
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
$$
with $B=c\gamma_5$ the only single-square mass and $c=\pm i\mu$.

The numerical checks of §*Verification* are stated in the same symbols: $\{\gamma_\mu,\gamma_\nu\}-2g_{\mu\nu}I$, $\gamma_5^2-I$, $\{\gamma_5,\gamma_\mu\}$, $\gamma_5-i\gamma_0\gamma_1\gamma_2\gamma_3$ and $(\sum_\mu \gamma_\mu k_\mu)^2-g_{\mu\nu}k_\mu k_\nu I$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The four contraction sums are frame statements, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.
