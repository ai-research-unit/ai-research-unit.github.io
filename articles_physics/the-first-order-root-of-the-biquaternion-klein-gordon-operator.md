# __The First-Order Root of the Biquaternion Klein–Gordon Operator__

## Introduction

The Klein–Gordon equation is second order. Its operator is the biquaternion norm of the gradient, $\Box=\langle\tilde\nabla\rangle_{\natural}$, and the equation is

$$
\left(\Box-\mu^2\right)\tilde\Phi=0,
\qquad
\mu=\frac{mc}{\hbar}.
$$

The companion article *The Klein–Gordon Equation in Biquaternionic Form* records that the operator is central and scalar, that the equation therefore decouples into four scalar equations, and that no scalar first-order operator in $\mathbb{B}$ has the operator as its square. The companion article *Klein–Gordon from the Dirac Square in Biquaternionic Form* records the other side: a first-order equation does exist, but it is spinor-valued, and its mass term couples two chiral halves. The two results together leave a question the corpus states as Open Question 3 of the Klein–Gordon article: is the spinor square root the only admissible first-orderisation, and if so, why four components?

This article answers the question by reading the norm form as a Clifford form. The answer has three parts, and each is a dimension statement rather than a dynamical one.

There are two inequivalent senses of "first-order root", and the article treats both. A **single square** is one operator $D$ with $D^2=(\Box-\mu^2)I$. A **factorisation** is a product $D_-D_+=(\Box-\mu^2)I$ of two first-order factors; the physical equation is one factor, and the product is the Klein–Gordon operator. The single square is the stronger notion, and the physical mass does not admit it. The factorisation is the weaker notion, and the physical mass requires it.

- **The root acts on a module of $\mathrm{Cl}_4(\mathbb{C})$.** A first-order operator $\Gamma^\mu\partial/\partial Q_\mu+B$ squares to $(\Box-\mu^2)I$ exactly when the four $\Gamma^\mu$ anticommute and square to $+1$. Four such generators generate $\mathrm{Cl}_4(\mathbb{C})\cong M_4(\mathbb{C})$, whose smallest module is $\mathbb{C}^4$. The minimal root therefore acts on four complex components, or eight real ones.
- **The biquaternion algebra supplies three of the four.** The three elements $i\vec e_x,i\vec e_y,i\vec e_z$ are Euclidean Clifford generators inside $\mathbb{B}$. No fourth element of $\mathbb{B}$ anticommutes with all three. The fourth generator must act on a second factor; in the regular picture that factor is the second minimal left ideal, and the operator that reaches it is a right multiplication. This is the precise reason the root lives in the two-sided operator algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$ and not in $\mathbb{B}\cong M_2(\mathbb{C})$.
- **The mass term is constrained.** The condition $\{B,\Gamma^\mu\}=0$ forces $B=c\Gamma_5$ with $c=\pm i\mu$. A single first-order operator therefore exists only with a **pseudoscalar** mass. A **scalar** mass commutes with the generators, so no single operator with a scalar mass squares to Klein–Gordon; the scalar mass admits only the factorisation $\mathsf D_-\mathsf D_+$. The physical mass is the scalar one, so the physical first-order equation is one factor of that factorisation.

The article is arranged as a ledger. The Clifford classification is standard; the identification of its three generators inside $\mathbb{B}$, and of the fourth with the two-sided direction, is the corpus's dictionary; the mass dichotomy and its reading as the reason for the chiral pair are the synthesis offered here. Nothing in the article predicts a mass or a coupling.

### Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and central imaginary $i$. The coordinates are $Q_\mu$, with $Q_t=ict'$ on the material sector. The gradient is $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$, and the d'Alembertian is the single one of the series,

$$
\Box=\langle\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}\left(\tilde\nabla^{\natural}\tilde\nabla\right)
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q
=\Delta_Q-c^{-2}\frac{\partial^2}{\partial t'^2}
\quad\text{on }\mathbb{M}_- .
$$

The Clifford generators used for the root satisfy

$$
\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I,
$$

with all four squares $+1$. This is the Euclidean Clifford algebra of the $Q$ coordinates, and it is the algebra that the all-plus norm requires. The corpus's gamma frame satisfies the mostly-minus relation $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I$ with $g=\mathrm{diag}(+1,-1,-1,-1)$; the two frames are related by

$$
\Gamma^0=\gamma^0,\qquad
\Gamma^k=i\gamma^k,\qquad k=x,y,z .
$$

The factor $i$ is the central imaginary, the same one that makes $Q_t$ imaginary. The rescaling is not cosmetic: the unrescaled symbol $\gamma^\mu\partial/\partial Q_\mu$ squares to $\partial^2/\partial Q_t^2-\Delta_Q$, which differs from $\Box$ by $-2\Delta_Q$. The Euclidean frame is a statement about the $Q$ coordinates, not a claim that spacetime is Euclidean.

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

with a vector remainder. The scalar part of this square is $\partial_t^2-\Delta_Q$, not $\Box$; the norm is the scalar part of the conjugate product, $\tilde\nabla\tilde\nabla^\natural=\Box e_t$, where the conjugation flips the sign of the spatial part. The first-order root is therefore not $\tilde\nabla$ itself: the gradient is a first-order operator whose square is not central, while the root is a first-order operator whose square is central, a multiple of the identity. The root is a different object, and it is matrix-valued.

### The symbol and the mass shell

On a plane wave the gradient acts as left multiplication by

$$
\tilde K=\frac{i\tilde P}{\hbar},
\qquad
\tilde P=i\frac{E}{c}e_t+\vec p ,
$$

and the symbol of the d'Alembertian is the norm of $\tilde K$,

$$
\Box\;\longmapsto\;\langle\tilde K\rangle_{\natural}
=\tilde K\tilde K^{\natural}
=-\frac{\tilde P\tilde P^{\natural}}{\hbar^2}.
$$

The mass shell is the level set

$$
\langle\tilde P\rangle_{\natural}=-m^2c^2
\quad\Longleftrightarrow\quad
\langle\tilde K\rangle_{\natural}=\mu^2
\quad\Longleftrightarrow\quad
E^2=\vec p^{\,2}c^2+m^2c^4 .
$$

The operator and its on-shell condition are the same norm, evaluated on the gradient and on the four-momentum. This is the structural fact that the rest of the article uses.

A first-order operator with symbol $\Gamma^\mu K_\mu+B$ is singular exactly when its determinant vanishes. If its square is $(\langle\tilde K\rangle_{\natural}-\mu^2)I$, the determinant vanishes exactly on the mass shell, so the first-order equation has nonzero plane-wave solutions exactly where the Klein–Gordon equation does.

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

The two questions are different. The determinant identity says that the scalar wave operator is the determinant of a first-order matrix; the root asks for one first-order operator whose square is the scalar operator. The massless root, when it exists, has $\det D=\pm\Box^2$, the same determinant as the left regular matrix of the gradient, up to sign. The massive root $R_\pm$ has $\det R_\pm=\pm(\Box-\mu^2)^2$, which reduces to the same expression at $\mu=0$. That is a consistency check, not a construction.

## The Root Condition

### The ansatz

Let

$$
D=\Gamma^\mu\frac{\partial}{\partial Q_\mu}+B,
\qquad
\Gamma^\mu,B\in M_n(\mathbb{C})\ \text{constant}.
$$

This is the most general first-order operator with constant coefficients and no zeroth-order derivative term beyond $B$. The matrices are constant because the classification below is a classification of the algebraic form; position-dependent coefficients are a separate problem, taken up in the open questions.

### The expansion

Because the partial derivatives commute, the quadratic term symmetrizes:

$$
D^2
=\frac12\{\Gamma^\mu,\Gamma^\nu\}\frac{\partial^2}{\partial Q_\mu\partial Q_\nu}
+\{\Gamma^\mu,B\}\frac{\partial}{\partial Q_\mu}
+B^2 .
$$

The symmetrization is the legitimate substitution of commuting derivatives for the product; it is not an assumption about the matrices. Requiring

$$
D^2=\left(\Box-\mu^2\right)I_n
$$

gives three conditions:

$$
\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I_n,
\qquad
\{\Gamma^\mu,B\}=0,
\qquad
B^2=-\mu^2I_n .
$$

The first is the Clifford relation. The second says the mass must anticommute with every generator. The third fixes the magnitude of the mass. The three are independent: the first is about the derivative part, the second about the mixing of the derivative and the mass, the third about the mass alone.

### The Euclidean sign

The Clifford relation has all-plus signs because $\Box$ has all-plus signs in the $Q$ coordinates. A mostly-minus frame does not satisfy it. If $\gamma^\mu$ satisfies $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ with $g=\mathrm{diag}(+1,-1,-1,-1)$, then the Euclidean generators are $\Gamma^0=\gamma^0$ and $\Gamma^k=i\gamma^k$, as in the conventions above. The factor $i$ is forced by the sign of the spatial derivatives in $\Box$, not chosen for convenience.

## Four Generators

### The Clifford algebra

Four generators with $\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}$ generate the complex Clifford algebra $\mathrm{Cl}_4(\mathbb{C})$, which is isomorphic to $M_4(\mathbb{C})$. The algebra is simple, so every nonzero representation is faithful, and its smallest module is $\mathbb{C}^4$. A representation on $\mathbb{C}^2$ would be a two-dimensional module for $M_4(\mathbb{C})$, which does not exist. Hence

$$
n\ge 4,
$$

and $n=4$ is both minimal and realised. The real dimension of the minimal module is eight, the same as the real dimension of $\mathbb{B}$.

The counting can be seen without naming the algebra. Four anticommuting matrices in $M_n(\mathbb{C})$ generate, together with their products, $16$ linearly independent matrices: the identity, the four generators, the six products $\Gamma^\mu\Gamma^\nu$ with $\mu<\nu$, the four products $\Gamma^\mu\Gamma_5$, and $\Gamma_5$. Sixteen independent matrices require $n^2\ge16$, hence $n\ge4$. The bound is attained by the Dirac matrices.

### Three inside the biquaternions

The biquaternion algebra contains three Euclidean Clifford generators:

$$
\Gamma^k=i\vec e_k,
\qquad
\left(\Gamma^k\right)^2=i^2\vec e_k^2=+e_t,
\qquad
\{\Gamma^j,\Gamma^k\}=i^2\{\vec e_j,\vec e_k\}=0,\quad j\neq k .
$$

They act by left multiplication on a minimal left ideal $S\cong\mathbb{C}^2$, and their images are the Pauli matrices,

$$
\mathsf M_2(i\vec e_x)=\sigma_1,
\qquad
\mathsf M_2(i\vec e_y)=\sigma_2,
\qquad
\mathsf M_2(i\vec e_z)=\sigma_3 .
$$

So $\mathbb{B}$ supplies three of the four generators, and the module $S$ is two-dimensional.

No fourth element of $\mathbb{B}$ anticommutes with all three. Write a general element as $X=a_0e_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. Anticommuting with $i\vec e_x$ is equivalent to anticommuting with $\vec e_x$, and

$$
\{X,\vec e_x\}=2a_0\vec e_x-2a_x e_t=0
$$

forces $a_0=a_x=0$. Anticommuting with $i\vec e_y$ then forces $a_y=0$, leaving $X=a_z\vec e_z$. But $\vec e_z$ commutes with $i\vec e_z$, so $X$ does not anticommute with the third generator. The only solution is $X=0$.

This is the coefficient proof of the Klein–Gordon article, read as a statement about the fourth generator. The obstruction is not that the algebra lacks room for a fourth direction; it is that the fourth direction cannot be a left multiplication.

### The factorised frame

The fourth generator acts on a second factor. The minimal module is

$$
\mathbb{C}^4\cong\mathbb{C}^2_{\mathrm{mult}}\otimes S,
$$

with $\mathbb{C}^2_{\mathrm{mult}}$ the multiplicity factor and $S$ the biquaternion spinor module. A frame that exhibits the factorisation is

$$
\Gamma^0=\sigma_1\otimes I_2,
\qquad
\Gamma^k=\sigma_3\otimes(i\vec e_k),
\qquad
\Gamma_5=\Gamma^0\Gamma^1\Gamma^2\Gamma^3=\sigma_2\otimes I_2 .
$$

The checks are exact. Each generator squares to the identity, distinct generators anticommute, and $\Gamma_5$ anticommutes with all four and squares to the identity. The matrices $\sigma_1,\sigma_2,\sigma_3$ act on the multiplicity factor; the elements $i\vec e_k$ act on $S$. The frame is a tensor product of the two actions, which is why it is a frame of the two-sided algebra and not of $\mathbb{B}$ alone.

The space of matrices that anticommute with all four generators is one-dimensional. If $B$ anticommutes with every $\Gamma^\mu$, then $B\Gamma_5$ commutes with every $\Gamma^\mu$. The generators generate $M_4(\mathbb{C})$, whose commutant is $\mathbb{C}I$, so $B\Gamma_5=cI$ and

$$
B=c\Gamma_5 .
$$

This is the fact the next section uses.

### The corpus frame and the Euclidean rescaling

The corpus's gamma frame is

$$
\gamma^0=iT_{e_t,e_x},
\qquad
\gamma^1=iT_{e_x,e_y},
\qquad
\gamma^2=iT_{e_y,e_y},
\qquad
\gamma^3=iT_{e_z,e_y},
\qquad
\gamma_5=-iT_{e_t,e_z},
$$

with $T_{a,b}=L_aR_b$. It satisfies the mostly-minus relation, and its squares are $(+1,-1,-1,-1)$. The Euclidean frame of this article is obtained by

$$
\Gamma^0=\gamma^0,
\qquad
\Gamma^k=i\gamma^k,
\qquad
\Gamma_5=-\gamma_5 .
$$

Both frames are frames of the same $\mathrm{Cl}_4(\mathbb{C})$, so they are similar. The factorised frame and the corpus frame are two representatives of one algebra, not two algebras. The factorised frame is used below because it displays the biquaternion factor and the multiplicity factor separately; the corpus frame is used when the dictionary to the two-sided operators is wanted.

The rescaling is forced by the symbol. On a plane wave,

$$
\gamma^\mu\frac{\partial}{\partial Q_\mu}\;\longmapsto\;\gamma^\mu K_\mu,
\qquad
\left(\gamma^\mu K_\mu\right)^2
=\left(\frac{\omega^2}{c^2}+|\vec k|^2\right)I,
$$

while

$$
\Box\;\longmapsto\;\frac{\omega^2}{c^2}-|\vec k|^2 .
$$

The unrescaled square differs from $\Box$ by $2|\vec k|^2$, the spatial part with the wrong sign. The Euclidean generators remove the sign:

$$
\left(\Gamma^\mu K_\mu\right)^2
=\langle\tilde K\rangle_{\natural}I
=\left(\frac{\omega^2}{c^2}-|\vec k|^2\right)I .
$$

The sign is a convention of the $ict'$ gradient, not a physical choice.

### The fourth direction is the second side

In the regular representation the biquaternion algebra acts on $\mathbb{B}\cong S\oplus S$ by left multiplication, and the two summands are the two minimal left ideals. Left multiplication preserves each summand. A fourth Clifford generator must interchange them: if it preserved each summand, it would be a left multiplication on $S$, and the coefficient proof excludes that.

The operator that interchanges the two summands is built from right multiplications by nilpotents. The corpus records this in *Element and Operator Representations: The Three Actions*: the right multiplication by the nilpotent moves between the two column ideals, while left multiplication preserves each. The algebra generated by the left action on $S$ and these right actions is the two-sided operator algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$. This is the precise sense in which the root needs $M_4$: the Klein–Gordon operator is central and needs no matrix algebra at all, but its Clifford module is the two-sided regular module.

The real dimension count is consistent. The module $\mathbb{C}^4$ has real dimension eight, the same as $\mathbb{B}$. The root does not enlarge the field space relative to a biquaternion field; it changes the module structure. Relative to a single complex scalar, of course, it is a fourfold complex enlargement.

## The Mass Condition and the Two Masses

### The condition

The second root condition is

$$
\{B,\Gamma^\mu\}=0\quad\text{for all }\mu .
$$

By the argument of the previous section, $B=c\Gamma_5$. The third condition then gives

$$
B^2=c^2\Gamma_5^2=c^2I=-\mu^2I,
\qquad
c=\pm i\mu .
$$

So the single-square roots are

$$
R_\pm=\mathsf D\pm i\mu\Gamma_5,
\qquad
\mathsf D=\Gamma^\mu\frac{\partial}{\partial Q_\mu},
\qquad
R_\pm^2=\left(\Box-\mu^2\right)I .
$$

The mass term is proportional to $\Gamma_5$. It is a **pseudoscalar** mass.

### The single square

The pseudoscalar mass is not an accident of the construction. It is the only mass that anticommutes with all four generators. In the chiral basis, where $\Gamma_5$ is diagonal, the term $i\mu\Gamma_5$ is diagonal: it couples the left-handed part to itself and the right-handed part to itself, with opposite signs. It does not mix the chiralities.

The corpus knows this channel. It is the $\chi$-type coupling of *The Dirac Equation in Biquaternionic Form*, the pseudoscalar potential that multiplies the central imaginary $i$ and is the $\gamma^5$-type in the matrix dictionary. The single first-order root is therefore not new machinery; it is the corpus's pseudoscalar channel read as a mass.

The term is parity-odd. A parity-odd mass is not the mass of the Dirac equation, and it is not the mass the Standard Model generates. The single root exists, but it is not the physical one.

### The scalar mass and the factorisation

The physical mass is a scalar: it multiplies the identity and commutes with every generator. It fails the second condition,

$$
\{\mu I,\Gamma^\mu\}=2\mu\Gamma^\mu\neq0,
$$

so no single operator of the form $\mathsf D+B$ with a scalar mass squares to the Klein–Gordon operator. Each factor alone carries a first-order remainder:

$$
\mathsf D_\pm=\mathsf D\pm\mu I,
\qquad
\mathsf D_\pm^2=\left(\Box+\mu^2\right)I\pm2\mu\mathsf D .
$$

The cross term is the price of the scalar mass. It cancels in the product:

$$
\mathsf D_-\mathsf D_+
=\left(\mathsf D-\mu I\right)\left(\mathsf D+\mu I\right)
=\left(\Box-\mu^2\right)I .
$$

The physical first-order equation is one factor, $\mathsf D_-\psi=0$ or $\mathsf D_+\psi=0$; the other factor carries the opposite mass. The product is the Klein–Gordon operator, so each factor implies Klein–Gordon without squaring to it. This is the precise sense in which the scalar mass needs a pair: not two independent equations, but a factorisation whose two factors carry opposite mass. The algebraic content of the chiral pair of the corpus is the same factorisation,

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

A central scalar field has a one-dimensional module. Four nonzero scalars commute, so they cannot satisfy the Clifford relation. Equivalently, a one-dimensional module cannot carry $M_4(\mathbb{C})$. The Klein–Gordon field itself, taken as a central scalar, therefore has no first-order root. A first-order root requires promoting the field to the Clifford module. This is the no-go of the Klein–Gordon article, recovered as a module-dimension statement.

The three cases are collected in the table.

| Field | Module | Mass matrix | Single square? | Structure |
|---|---|---|---|---|
| Central scalar | $\mathbb{C}$ | — | no | no root |
| Pseudoscalar-mass spinor | $\mathbb{C}^4$ | $i\mu\Gamma_5$ | yes | $R_\pm^2=(\Box-\mu^2)I$ |
| Scalar-mass spinor | $\mathbb{C}^4$ | $\mu I$ | no | $\mathsf D_-\mathsf D_+=(\Box-\mu^2)I$ |

## What the Root Does Not Carry

The root is a classification of form, and its boundaries are part of the result.

- **It is stronger than Klein–Gordon.** A first-order equation selects a subspace of the second-order solution space. The single root and the Dirac factor select different subspaces, and neither is equivalent to the second-order equation. The second-order equation has both frequency branches and all polarisations; a first-order equation has half of them.
- **The massless limit is singular.** At $\mu=0$ the single root reduces to $\mathsf D$, the massless Dirac operator, whose kernel is the two Weyl halves; the scalar-mass factorisation reduces to $\mathsf D^2=\Box$. The mass term is what distinguishes the two mass channels, so the massless limit does not select one of them.
- **The sign of the mass is not physical.** $R_+$ and $R_-$ are exchanged by $\Gamma_5\to-\Gamma_5$ or by $\mu\to-\mu$. Only the relative sign of the mass and the chirality is meaningful.
- **No mass and no coupling are predicted.** The classification says which first-order structures have the Klein–Gordon square. It does not say which one nature uses, and it does not determine $\mu$.
- **The coefficients are constant.** Position-dependent coefficients add commutator terms. The Clifford structure is deformed by the field strength, and the classification of the constant-coefficient case is the starting point, not the answer, for a gauged root.
- **The frame is Euclidean in the $Q$ coordinates.** The physical Minkowski frame is obtained by the rescaling $\Gamma^k=i\gamma^k$. The Euclidean form is a consequence of the $ict'$ convention, not a physical postulate.

## The Even and the Odd Face

The article's result can be stated as a division of labour between two matrix sizes.

- **The even face is $M_2$.** The Klein–Gordon operator is central; the determinant of the chiral block of the left regular matrix is $\Box$. The three generators $i\vec e_k$ and the determinant identity live at the $M_2(\mathbb{C})$ level; the chiral pair is written in the biquaternion module before the fourth generator is adjoined.
- **The odd face is $M_4$.** The first-order structure — the single square $R_\pm$ or the Dirac factor of the scalar-mass case — needs the fourth generator, the multiplicity factor, and the two-sided algebra. For the single square, $\det R_\pm=\pm(\Box-\mu^2)^2$, which reduces to $\Box^2$ at $\mu=0$ and matches the determinant of the left regular matrix of the gradient.

The division answers the $M_2$/$M_4$ question of the companion articles. The Klein–Gordon **equation** does not require $M_4$: its operator is central and its field can be a single complex scalar. The Klein–Gordon **root** does require $M_4$: the fourth Clifford direction is the second side of the algebra. The two statements are compatible because they are about different objects. The scalar equation lives in the centre; its first-order root lives in the two-sided algebra.

The regular representation's doubling is not a prediction of doubled particles. The two minimal left ideals are the two chiral copies of the same module; the doubling is the price of the fourth generator, not a doubling of the spectrum.

## Verification

The identities were recomputed before they were written. The factorised frame was built from the Pauli matrices and the $2\times2$ images of $i\vec e_k$; the corpus frame was built from $T_{a,b}=L_aR_b$ in the coefficient basis. The checks are collected in the table. The residuals are the largest absolute entries over the stated samples.

| Check | Result |
|---|---|
| $\Gamma^\mu\Gamma^\nu+\Gamma^\nu\Gamma^\mu-2\delta^{\mu\nu}I$ | $0$ (exact) |
| $\Gamma_5^2-I$ and $\Gamma_5\Gamma^\mu+\Gamma^\mu\Gamma_5$ | $0$ (exact) |
| $\Gamma_5=\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ | $0$ (exact) |
| Anticommutant of all four generators is one-dimensional | rank $15$, nullity $1$ |
| $R_+^2-(\Box-\mu^2)I$ on $50$ random complex $K$ | $3.7\times10^{-15}$ |
| $\mathsf D_-\mathsf D_+-(\Box-\mu^2)I$ on $50$ random $K$ | $2.0\times10^{-15}$ |
| $\left(\Gamma^\mu K_\mu\right)^2-\langle\tilde K\rangle_{\natural}I$ | $1.8\times10^{-15}$ |
| Corpus frame squares $(+1,-1,-1,-1)$ and anticommutators | $0$ (exact) |

The numerical checks are checks of polynomial identities at random points. The proof is the algebra of the preceding sections; the numbers guard against a sign or factor error in the transcription.

## Open Questions

1. **The gauged root.** Replace $\partial/\partial Q_\mu$ by $\partial/\partial Q_\mu+A_\mu$. The square acquires a commutator term, and the Clifford structure is deformed by the field strength. Does the root exist for every connection, or only for a restricted class? The non-abelian gauge article records that the field strength is not gauge invariant; the root's square would have to be a gauge-covariant object, and the Clifford classification would have to be applied fibrewise.
2. **Position-dependent mass.** A mass $\mu(Q)$ that varies in space or time gives $[\Gamma^\mu\partial_\mu,\mu]\neq0$. The single square and the factorisation respond differently. Which one survives, and at what order?
3. **The curved background.** The $Q$ coordinates are flat. On a curved background the partial derivatives become covariant derivatives, and the Clifford algebra is the tangent-space algebra. The dimension count is unchanged, but the spin connection enters the root.
4. **The pseudoscalar mass.** The single root is parity-odd. Is there a physical setting in which a pseudoscalar mass is the relevant one, or is the single root a mathematical possibility only? The corpus's $\chi$-type coupling suggests an axial channel, but no dynamics is supplied here.
5. **The real structure.** The article works over $\mathbb{C}$. The real form is $\mathrm{Cl}_{0,4}(\mathbb{R})\cong M_2(\mathbb{H})$, with module $\mathbb{H}^2$ of real dimension eight. The Majorana/Dirac question and the charge-conjugation pairing are real-structure questions that this article does not settle.
6. **The index.** The massless root $\mathsf D$ is odd under the chirality grading and $\Box$ is even. The index of $\mathsf D$ is an invariant of the graded module. Does the biquaternion chirality grading give a nontrivial index on a background with a gauge field?
7. **The Dirac factor versus the single root.** Both are four-component first-order equations that imply Klein–Gordon, with different mass channels. Is there a sense in which one is canonical, or is the choice a choice of mass channel? The classification says they are different channels; the dynamics would have to decide.

## Summary

The first-order root of the biquaternion Klein–Gordon operator exists, and its size is fixed by the norm form. The root acts on a module of $\mathrm{Cl}_4(\mathbb{C})$, whose minimal module is $\mathbb{C}^4$. The biquaternion algebra supplies three of the four Euclidean generators, $i\vec e_x,i\vec e_y,i\vec e_z$, and no fourth; the fourth acts on the multiplicity factor and, in the regular picture, is a right multiplication that swaps the two minimal left ideals. The root therefore lives in the two-sided operator algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$, while the Klein–Gordon operator itself remains central.

The mass term is constrained by the condition $\{B,\Gamma^\mu\}=0$. The only single-operator solution is $B=\pm i\mu\Gamma_5$, a pseudoscalar mass. A scalar mass commutes with the generators, so no single operator with a scalar mass squares to Klein–Gordon; the scalar mass admits only the factorisation $\mathsf D_-\mathsf D_+$, which is the corpus's chiral pair. The physical mass is the scalar one, so the physical first-order equation is one factor of that factorisation.

The scalar Klein–Gordon field, taken as a central scalar, has no first-order root. The results are a classification of form: no mass, no coupling, and no dynamics are predicted. The open questions are the gauged, curved, position-dependent, and real-structure extensions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $Q_\mu$ | Algebra coordinates, $Q_t=ict'$ on $\mathbb{M}_-$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\partial^2/\partial Q_t^2+\Delta_Q$ | d'Alembertian, series convention |
| $\mu=mc/\hbar$ | Mass parameter (inverse reduced Compton wavelength) |
| $\tilde P=iE/c\,e_t+\vec p$ | Material four-momentum |
| $\tilde K=i\tilde P/\hbar$ | Symbol of the gradient |
| $\langle\tilde K\rangle_{\natural}=\mu^2$ | Mass shell |
| $\Gamma^\mu$ | Euclidean Clifford generators, $\{\Gamma^\mu,\Gamma^\nu\}=2\delta^{\mu\nu}I$ |
| $\Gamma_5=\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ | Pseudoscalar generator |
| $\mathsf D=\Gamma^\mu\partial/\partial Q_\mu$ | Euclidean Dirac operator |
| $R_\pm=\mathsf D\pm i\mu\Gamma_5$ | Single-square roots, $R_\pm^2=(\Box-\mu^2)I$ |
| $\mathsf D_\pm=\mathsf D\pm\mu I$ | Scalar-mass factors, $\mathsf D_-\mathsf D_+=(\Box-\mu^2)I$ |
| $S\cong\mathbb{C}^2$ | Minimal left ideal (biquaternion spinor module) |
| $A_+(\tilde\nabla)$ | Chiral block of the left regular matrix, $\det A_+=\Box$ |
| $\mathsf M_4^L(\tilde Q)$ | Left regular matrix, $\det\mathsf M_4^L(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2$ |
| $L_a,R_b$ | Left and right multiplication operators |
| $T_{a,b}=L_aR_b$ | Two-sided cell |
| $\gamma^\mu$ | Corpus gamma frame, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I$ |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Corpus Clifford metric |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the identity $(\mathsf D-\mu)(\mathsf D+\mu)=\Box-\mu^2$ and the plane-wave spinors.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra, the gamma matrices, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the classification of Clifford algebras, the minimal modules, and the square root of the wave operator.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the complex and real Clifford algebras and their irreducible modules.
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the periodicity and the module dimensions.
- V. V. Kravchenko, *Quaternionic Analysis and Its Applications* (Birkhäuser, 2003), for the quaternionic Dirac operator and its relation to the Euclidean Clifford algebra.
- The corpus articles *The Klein–Gordon Equation in Biquaternionic Form*, *Klein–Gordon from the Dirac Square in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form*, *The Biquaternion D'Alembertian and Its Green's Functions*, and *Conventions in the Biquaternion Universe* for the conventions and the results this article builds on.
- The corpus articles *$M_4(\mathbb{C})_L$ Representation : The Two-Sided Operators on the Biquaternion Algebra*, *Element and Operator Representations: The Three Actions*, and *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes* for the two-sided algebra, the nilpotent that swaps the minimal left ideals, and the $M_2$/$M_4$ dictionary.
