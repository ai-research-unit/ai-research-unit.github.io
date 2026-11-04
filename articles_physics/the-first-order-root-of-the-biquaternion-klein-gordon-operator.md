# __The First-Order Root of the Biquaternion Klein–Gordon Operator__

## Introduction

The biquaternion Klein–Gordon operator has a first-order root, but it has no single one. Squaring a first-order operator to the central scalar $\Box-\mu^2$ needs four mutually anticommuting generators, one of square $+1$ and three of square $-1$, the Lorentz signature. The algebra supplies the three, and the fourth multiplies on the right. The root is therefore not a table of numbers acting on a list of numbers: it is a sum of multiplications acting on both sides of the algebra, and the field stays an element of the algebra. With a pseudoscalar mass the single square exists. With the physical scalar mass only a factorisation exists, and the physical equation is one factor of it.

The equation is

$$
\left(\Box-\mu^2\right)\tilde\Phi=0,
\qquad
\mu=\frac{mc}{\hbar}.
$$

The companion *The Klein–Gordon Equation in Biquaternionic Form* records that the operator is central and scalar, that the equation decouples into four scalar equations, and that no scalar first-order operator in $\mathbb{B}$ has it as its square. The companion *Klein–Gordon from the Dirac Square in Biquaternionic Form* records the other side: a first-order equation exists, but its field carries an $L$ part and an $R$ part, and its mass couples the two. Together they leave Open Question 3 of the Klein–Gordon article: is that the only first-orderisation, and why four components?

There are two inequivalent senses of "first-order root", and the article treats both. A **single square** is one first-order operator whose square is $\Box-\mu^2$. A **factorisation** is a product of two first-order factors whose product is $\Box-\mu^2$; the physical equation is one factor, and the product is the Klein–Gordon operator. The single square is the stronger notion, and the physical mass does not admit it. The factorisation is the weaker notion, and the physical mass requires it.

The two notions give two first-order equations, and the article keeps them apart. Write $\mathsf D$ for the derivative part, defined in §*The Root Condition*; the single square is

$$
\mathsf D_{\mathrm{ps},\pm}\psi=\mathsf D\psi\pm\mu\,\psi\vec e_z,
\qquad
\mathsf D_{\mathrm{ps},\pm}^2=\Box-\mu^2,
$$

with a pseudoscalar mass, and the factorisation is

$$
\mathsf D_{\mathrm{sc},\pm}\psi=\mathsf D\psi\pm\mu\psi,
\qquad
\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}=\Box-\mu^2,
$$

with a scalar mass. They are different equations, not two spellings of one, and the physical mass selects the second.

Three results:

- **The root acts on four complex dimensions.** The derivative part $\mathsf D$ of a first-order operator $\mathsf D+\mathsf B$ squares to the scalar $\Box$ exactly when its four generators mutually anticommute, with one square $+1$ and three of square $-1$. Together with their products they give sixteen independent maps of the algebra, and sixteen independent maps need a carrier of at least four complex dimensions. The algebra itself is four-dimensional over $\mathbb{C}$, so the carrier is $\mathbb{B}$.
- **The algebra supplies three of the four.** The three spatial units supply the three spatial generators. No element of $\mathbb{B}$ anticommutes with all three, so the fourth generator cannot multiply only on the left; it multiplies on the right, and it is $\psi\mapsto i\psi\vec e_x$.
- **The mass term is constrained.** The condition that the mass anticommutes with all four generators leaves one direction: the mass is the multiplication $\psi\mapsto\mu\psi\vec e_z$. A single operator therefore exists only with a **pseudoscalar** mass. A **scalar** mass commutes with the generators, so it admits only the factorisation, and the physical first-order equation is one factor.

The count of sixteen maps is elementary linear algebra. The identification of the four generators with the two sides of the algebra is the corpus's dictionary, and the mass dichotomy read as the reason for the chiral pair is the synthesis offered here. Nothing in the article predicts a mass or a coupling.

## The Equation

$\Box$ is the biquaternion d'Alembertian of the series, one operator in both coordinate frames, and the article uses it without restating it (*Operator and Calculus Conventions*). It is read here in the Lorentz coordinates $x_0=ct'$ and $x_k$, related to the algebra coordinates by $Q_t=ix_0$ and $Q_k=x_k$. Derived from that relation, its Lorentz form is

$$
\Box=-\frac{1}{c^2}\frac{\partial^2}{\partial t'^2}+\Delta ,
$$

because the substitution turns $\partial^2/\partial Q_t^2$ into $-\partial^2/\partial x_0^2$ and leaves the three spatial derivatives alone. This is the form the rest of the article uses.

Throughout, $c$ is the speed of light in the medium and $\hbar$ the reduced Planck constant. The mass parameter $\mu=mc/\hbar$ must not be confused with the permeability of electromagnetism, which carries the same letter: the letter is overloaded in the corpus.

## The Operator and Its Symbol

### The gradient is not the root

The gradient is a first-order operator, and its square is not central: the conventions record the vector remainder (*Operator and Calculus Conventions*). A root must square to a multiple of the identity, so the gradient is not one. The root is a different object, and it acts on both sides of the algebra.

### The symbol and the mass shell

On a plane wave $e^{-ik_0x_0+i\vec k\cdot\vec x}$ every derivative is a multiple of the wave, and the derivative part acts as one fixed map of the algebra. At the wave covector $k_\mu=(\omega/c,\vec k)$ that map is

$$
\mathsf D(k)\psi=k_0\,i\psi\vec e_x-\sum_k k_k\,i\vec e_k\psi\vec e_y,
$$

and its square is a multiple of the identity,

$$
\mathsf D(k)^2\psi=\left(k_0^2-\lvert\vec k\rvert^2\right)\psi,
$$

which is the symbol of $\Box$. The mass shell is the level set

$$
k_0^2-\lvert\vec k\rvert^2=\mu^2
\quad\Longleftrightarrow\quad
\frac{\omega^2}{c^2}-\lvert\vec k\rvert^2=\frac{m^2c^2}{\hbar^2}
\quad\Longleftrightarrow\quad
E^2=\vec p^{\,2}c^2+m^2c^4 .
$$

The symbol of $\Box$ is the interval of the wave covector, and the mass shell is that symbol set to $\mu^2$. This is the structural fact the rest of the article uses.

The symbol of an operator whose square is $\Box-\mu^2$ is singular exactly on the shell, because its square is $(k_0^2-\lvert\vec k\rvert^2-\mu^2)$ times the identity. A first-order equation therefore has a nonzero plane-wave solution exactly where the Klein–Gordon equation does.

## The Root Condition

### The ansatz

The four generators are the maps

$$
G_0:\psi\mapsto i\psi\vec e_x,
\qquad
G_k:\psi\mapsto i\vec e_k\psi\vec e_y,
$$

and the derivative part is

$$
\mathsf D\psi=i\sum_\mu G_\mu\Bigl(\frac{\partial\psi}{\partial x_\mu}\Bigr),
$$

and a first-order operator of constant coefficients is $\mathsf D+\mathsf B$, where $\mathsf B$ is a fixed map of $\mathbb{B}$ that carries no derivative. Written out, the derivative part is

$$
\mathsf D\psi=-\frac{\partial\psi}{\partial x_0}\vec e_x-\sum_k\vec e_k\frac{\partial\psi}{\partial x_k}\vec e_y .
$$

Two imaginary units stand side by side in the first form: the inner $i$ belongs to the generator and the outer one to the operator. Their product is $i^2=-1$, which is why the second form carries no imaginary unit at all. The generator form is kept because it is the one whose anticommutation relations state the signature; the minus sign there is carried by the product of the units and is not a separate convention.

This is the form in which the root condition is solved, not the most general first-order operator: a general constant-coefficient first-order operator whose square is $\Box-\mu^2$ has coefficients that anticommute with the same signature, so it differs from this one by a change of basis of the algebra. The coefficients are constant because the classification below is a classification of the algebraic form; position-dependent coefficients are a separate problem, taken up in §*What the Root Does Not Carry*.

### The expansion

Because the partial derivatives commute, only the symmetric part of the second-order term survives: the antisymmetric part of a product of two generators multiplies the symmetric $\partial^2/\partial x_\mu\partial x_\nu$ and drops out. Hence

$$
(\mathsf D+\mathsf B)^2\psi
=-\tfrac12\sum_{\mu,\nu}\bigl(G_\mu G_\nu+G_\nu G_\mu\bigr)\Bigl(\frac{\partial^2\psi}{\partial x_\mu\partial x_\nu}\Bigr)
+i\sum_\mu\bigl(G_\mu\mathsf B+\mathsf B G_\mu\bigr)\Bigl(\frac{\partial\psi}{\partial x_\mu}\Bigr)
+\mathsf B^2\psi .
$$

This is an identity for every choice of the generators and of $\mathsf B$; it assumes nothing about them. Requiring $(\mathsf D+\mathsf B)^2\psi=\Box\psi-\mu^2\psi$ and matching the three monomials gives three conditions, written for maps of the algebra and with $1$ the identity map:

$$
G_0^2=1,
\qquad
G_k^2=-1,
\qquad
G_\mu G_\nu+G_\nu G_\mu=0\quad(\mu\neq\nu),
\qquad
G_\mu\mathsf B+\mathsf B G_\mu=0,
\qquad
\mathsf B^2=-\mu^2 .
$$

The first is the relation on the derivative part: the four generators square to $+1,-1,-1,-1$ and anticommute in pairs, which is the Lorentz signature. The second says the mass must anticommute with every generator. The third fixes the magnitude of the mass. The three are independent: the first is about the derivative part, the second about the mixing of the derivative and the mass, the third about the mass alone.

The signs are those of $\Box$ in the $x$ coordinates, where the time term is negative and the three spatial terms positive. The algebra coordinates carry the Euclidean transcription, in which all four generators square to $+1$ and the spatial ones acquire a factor $i$; that frame is not used here.

## Four Generators

### The carrier is four-dimensional

The four generators are maps of $\mathbb{B}$, and so is every product of them. Together with the identity they give sixteen maps: the identity, the four, the six products of two, the four products of three, and the product of all four. They are linearly independent (§*Verification*), so sixteen independent maps act on the algebra. A complex space of dimension $n$ carries $n^2$ independent complex-linear maps, so $n\ge4$. The algebra has $n=4$, and the bound is attained: the root acts on $\mathbb{B}$ itself.

This is the answer to the "why four components" of Open Question 3. The four components are not an added multiplicity; they are the four coefficients of a biquaternion.

### Three inside the algebra

Three of the four generators carry a left factor from the algebra: $G_k$ multiplies by $\vec e_k$ on the left and by $\vec e_y$ on the right. The algebra's own units supply them, because the three spatial units anticommute in pairs and each squares to $-\vec e_t$.

No element of $\mathbb{B}$ anticommutes with all three. Write a general element as $X=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_t\vec e_x-2a_x e_t=0,
$$

which forces $a_t=a_x=0$. Anticommuting with $\vec e_y$ then forces $a_y=0$, leaving $X=a_z\vec e_z$. But $a_z\vec e_z$ commutes with the third unit, so it does not anticommute with it. The only solution is $X=0$.

This is the coefficient proof of the Klein–Gordon article, read as a statement about the fourth generator. The obstruction is not that the algebra lacks room for a fourth direction; it is that a fourth direction cannot multiply only on the left.

### The fourth multiplication is on the right

The fourth generator is

$$
G_0:\psi\mapsto i\psi\vec e_x,
$$

a multiplication on the right. It commutes with every left multiplication, so no product of left multiplications can produce it, and it anticommutes with the three spatial generators through the right factor, $\vec e_y\vec e_x=-\vec e_x\vec e_y$.

The four use both sides, and together they give every map of the algebra: sixteen independent maps on a space of sixteen dimensions. The algebra has real dimension eight and complex dimension four, so the root does not enlarge the field space relative to a biquaternion field. It changes the action, not the carrier. Relative to a single complex scalar, of course, it is a fourfold complex enlargement, and §*The scalar field has no root* shows that a central scalar admits none.

## The Mass Condition and the Two Masses

### The condition

The second root condition is

$$
G_\mu\mathsf B+\mathsf B G_\mu=0\quad\text{for all }\mu .
$$

Expanding $\mathsf B$ in the sixteen maps, the four anticommutators force every coefficient except that of the product of the four to vanish, and the product is $\psi\mapsto-\psi\vec e_z$ (§*Verification*). Hence

$$
\mathsf B\psi=c\,\psi\vec e_z,
\qquad
\mathsf B^2\psi=-c^2\psi,
$$

and $\mathsf B^2=-\mu^2$ gives $c=\pm\mu$. The single-square roots are

$$
\mathsf D_{\mathrm{ps},\pm}\psi=\mathsf D\psi\pm\mu\,\psi\vec e_z,
\qquad
\mathsf D_{\mathrm{ps},\pm}^2=\Box-\mu^2 .
$$

The mass term is the multiplication $\psi\mapsto\mu\psi\vec e_z$. It is a **pseudoscalar** mass.

### The single square

The pseudoscalar mass is not an accident of the construction: it is the only mass that anticommutes with all four generators. It acts on the two parts separately, by opposite constants, so it does not mix $\psi_L$ with $\psi_R$.

The invariant statement is the anticommutator, not the shape of any display. The scalar mass commutes with $\mathsf D$; the pseudoscalar mass anticommutes with it. No change of basis alters which of the two holds, because the two conditions are statements about the algebra and not about a basis.

The corpus knows this channel. It is the pseudoscalar potential of *The Dirac Equation in Biquaternionic Form*, which multiplies the central imaginary $i$. The single first-order root is therefore not new machinery; it is the corpus's pseudoscalar channel read as a mass. A mass of that kind is not the mass of the Dirac equation, and it is not the mass the Standard Model generates. The single root exists, but it is not the physical one.

### The scalar mass and the factorisation

The physical mass is a scalar: it multiplies every element by the same constant and commutes with every generator. It fails the second condition,

$$
(G_\mu\mathsf B+\mathsf B G_\mu)\psi=2\mu\,G_\mu\psi\neq0
\quad\text{for }\mathsf B:\psi\mapsto\mu\psi,
$$

so no single operator of the form $\mathsf D+\mathsf B$ with a scalar mass squares to the Klein–Gordon operator. Each factor alone carries a first-order remainder:

$$
\mathsf D_{\mathrm{sc},\pm}\psi=\mathsf D\psi\pm\mu\psi,
\qquad
\mathsf D_{\mathrm{sc},\pm}^2=\Box+\mu^2\pm2\mu\mathsf D .
$$

The cross term is the price of the scalar mass. It cancels in the product:

$$
\mathsf D_{\mathrm{sc},-}\bigl(\mathsf D_{\mathrm{sc},+}\psi\bigr)
=\left(\Box-\mu^2\right)\psi .
$$

The physical first-order equation is one factor, $\mathsf D_{\mathrm{sc},-}\psi=0$ or $\mathsf D_{\mathrm{sc},+}\psi=0$; the other factor carries the opposite mass. The product is the Klein–Gordon operator, so each factor implies Klein–Gordon without squaring to it. This is the precise sense in which the scalar mass needs a pair: not two independent equations, but a factorisation whose two factors carry opposite mass. The algebraic content of the chiral pair of the corpus is the same factorisation,

$$
\tilde\nabla\tilde\Psi_R=\mu\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=\mu\tilde\Psi_R,
$$

with the same $\mu$ as above, which the companion writes as $m$ in natural units. Substituting the first into the second and using $\tilde\nabla^{\natural}\tilde\nabla=\Box$ gives $\Box\tilde\Psi_R=\mu^2\tilde\Psi_R$, so each part satisfies Klein–Gordon. The pair is the scalar-mass case written on the two parts of one element, not a second, independent root.

The dichotomy is therefore sharp:

- a **pseudoscalar** mass anticommutes with the generators and admits a single first-order operator whose square is Klein–Gordon;
- a **scalar** mass commutes with the generators and admits only the factorisation, whose physical factor is the Dirac equation.

The physical mass is the second. The corpus's use of the chiral pair is not an arbitrary choice of basis; it is the form of the factorisation forced by the scalar mass.

### The scalar field has no root

A field whose value is one complex number has one independent complex-linear map, the multiplication by a constant, and four independent generators need four of them, so such a field admits no first-order root. A root requires the field to be an element of the algebra. The Klein–Gordon equation is satisfied by both readings and only the second has a root: this is the no-go of the Klein–Gordon article recovered as a dimension count. The three cases are collected in the table.

| Field | Independent maps | Mass term | Equation | Single square? |
|---|---|---|---|---|
| One complex number | one | — | no first-order equation | no |
| Element of $\mathbb{B}$ | sixteen | $\psi\mapsto\mu\psi\vec e_z$ | $\mathsf D_{\mathrm{ps},\pm}\psi=0$ | yes, $\mathsf D_{\mathrm{ps},\pm}^2=\Box-\mu^2$ |
| Element of $\mathbb{B}$ | sixteen | $\psi\mapsto\mu\psi$ | $\mathsf D_{\mathrm{sc},\pm}\psi=0$, one factor | no, $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}=\Box-\mu^2$ |

### The determinant face

On a plane wave the symbol of $\mathsf D_{\mathrm{ps},\pm}$ is $\mathsf D(k)\pm\mu(\psi\mapsto\psi\vec e_z)$, and its determinant is

$$
\det\bigl(\mathsf D(k)\pm\mu(\psi\mapsto\psi\vec e_z)\bigr)
=\left(k_0^2-\lvert\vec k\rvert^2-\mu^2\right)^2,
$$

the square of the symbol of $\Box-\mu^2$. At $\mu=0$ the same value is the square of the symbol of $\Box$.

The determinant is a product of eigenvalues, and it is not a square root. The two questions are different. A determinant identity says that the square of the scalar symbol is the determinant of a first-order operator; a root needs one first-order operator whose square is the scalar operator. The two signs of the mass give one determinant, so the determinant is a consistency check on the classification and not a construction of the root.

## What the Root Does Not Carry

The classification is a statement of form, and its boundaries are part of the result.

1. **It is stronger than Klein–Gordon.** A first-order equation selects a subspace of the second-order solution space. The single root and the Dirac factor select different subspaces, and neither is equivalent to the second-order equation. At a fixed momentum on the shell the second-order equation admits every element, four complex dimensions, while the root admits a two-dimensional subspace; both retain the two frequency branches, so what the root halves is the room for the field at that momentum and not the spectrum. At $\mu=0$ the single root reduces to $\mathsf D$, whose kernel is two-dimensional with one state of each value of the label, while the scalar-mass factorisation reduces to $\mathsf D^2=\Box$; the massless limit does not select one channel.
2. **No mass and no coupling are predicted.** The classification says which first-order structures have the Klein–Gordon square; it does not say which one nature uses, and it does not determine $\mu$. The sign of the mass carries no content either: $\mathsf D_{\mathrm{ps},+}$ at $\mu$ and $\mathsf D_{\mathrm{ps},-}$ at $-\mu$ are one operator. Whether a pseudoscalar mass is realised is a dynamical question that the classification leaves open; the corpus's pseudoscalar potential suggests such a channel but supplies no dynamics.
3. **The coefficients are constant and the background flat.** A position-dependent coefficient adds a term in which the derivative acts on the coefficient, and a gauged derivative adds a field strength; the constant-coefficient classification is then the starting point rather than the answer. On a curved background the derivatives become covariant, and the classification applies in the tangent space at each point. The $x$ coordinates are flat; the algebra coordinates give the same operator and not a different root.
4. **The real structure and the index are open.** The article works over $\mathbb{C}$. Whether the four generators can be chosen real, and which real structure the field carries, is the charge-conjugation question, and the article does not settle it. The massless root converts an $L$ part into an $R$ part while $\Box$ preserves the value, so an index is available; whether it is nontrivial on a gauge background is open.

## The Equation and the Root

Two statements that look like one. The Klein–Gordon **equation** is central: its operator multiplies every element by the same scalar, so a single complex scalar satisfies it. The Klein–Gordon **root** is not central: it multiplies on both sides, so it acts on the whole algebra. The equation lives in the centre; the root lives on the two sides.

The two statements are compatible because they are about different objects. A scalar equation needs no second side; its first-order root does.

The doubling is not a doubling of particles. The two values of the label are the two parts of one element, and the root reads both.

## Verification

The identities were recomputed before they were written. The four generators were built as maps of $\mathbb{B}$ and applied to random elements. The derivative identities were checked on their symbols, at random wave covectors. The residuals are the largest absolute difference over the stated samples, and $\mu$ is a fixed real mass.

| Check | Result |
|---|---|
| the four generators square to $+1,-1,-1,-1$ and anticommute in pairs | $0$ (exact) |
| the sixteen products are linearly independent | rank $16$ |
| the product of the four generators is $\psi\mapsto-\psi\vec e_z$ | $0$ (exact) |
| the maps that anticommute with all four | one-dimensional, spanned by $\psi\mapsto\psi\vec e_z$ |
| no element of $\mathbb{B}$ anticommutes with the three spatial units | rank $4$ of $4$ |
| $G_0$ commutes with every left multiplication | $0$ (exact) |
| the mass $\psi\mapsto\mu\psi\vec e_z$ anticommutes with the four and squares to $-\mu^2$ | $0$ (exact) |
| $\mathsf D(k)^2\psi-(k_0^2-\lvert\vec k\rvert^2)\psi$ on $100$ random wave covectors | $1.8\times10^{-15}$ |
| $\mathsf D_{\mathrm{ps},\pm}^2-(\Box-\mu^2)$ on $100$ random wave covectors | $1.8\times10^{-15}$ |
| $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}-(\Box-\mu^2)$ on $100$ random wave covectors | $1.8\times10^{-15}$ |
| $\mathsf D_{\mathrm{sc},+}^2-(\Box+\mu^2+2\mu\mathsf D)$ | $1.8\times10^{-15}$ |
| the determinant of the symbol of $\mathsf D_{\mathrm{ps},\pm}$, minus the square of the symbol of $\Box-\mu^2$, on $100$ random wave covectors | $8.5\times10^{-14}$ |
| the massless kernel at $k_0^2-\lvert\vec k\rvert^2=0$: dimension two, one state of each value | $0$ (exact) |
| the label split of $100$ random elements: only the zero element in both parts | $0$ failures |

The numerical checks are checks of polynomial identities at random points. The proof is the algebra of the preceding sections; the numbers guard against a sign or factor error in the transcription.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The five are the frame cells written as matrices:
$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

They satisfy $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$, $(\gamma_0[\mathbb{M}_-])^2=+I_4$, $(\gamma_k[\mathbb{M}_-])^2=-I_4$, $\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0$ and $\gamma_5=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$. The product of the first four is $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{pau}}$, and $i$ times it is $\gamma_5$; the corpus's volume element $-iR_{\vec e_z}^{\mathrm{pau}}$ is $\gamma_5$ itself.

In the tensor frame the same five are the images under $L_{a}R_{b}\mapsto\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)$,
$$
\gamma_0[\mathbb{M}_-]=\sigma_1\otimes I_2,\qquad
\gamma_k[\mathbb{M}_-]=i\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2,
$$
and the split between the two sides is the cell table of §*Four Generators*.

The root and the mass conditions read in gammas as
$$
\mathsf D=i\sum_\mu\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu}=i\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu},\qquad
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\gamma_5=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{pau}},\qquad
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
$$

In the axis-free display:

$$
\mathsf D=i\sum_\mu\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu}=i\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu},\qquad
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\gamma_5=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{axf}},\qquad
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
$$

The only single-square mass term is $B=c\gamma_5$ with $c=\pm i\mu$; the second equality for $\mathsf D_{\mathrm{ps},\pm}$ uses $i\gamma_5=R_{\vec e_z}^{\mathrm{pau}}$.

The checks of §*Verification*, transcribed into these symbols, are $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}-2g_{\mu\nu}I_4$, $\gamma_5^2-I_4$, $\{\gamma_5,\gamma_\mu[\mathbb{M}_-]\}$, $\gamma_5-i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ and $(\sum_\mu \gamma_\mu[\mathbb{M}_-] k_\mu)^2-g_{\mu\nu}k_\mu k_\nu I_4$; the first and the last are polynomial identities in the symbol $k$, so they hold for every $k$, not only on shell.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.

## Summary

The first-order root of the biquaternion Klein–Gordon operator exists, it has two forms, and the algebra fixes which form the physical mass uses. Squaring a first-order operator to the central scalar $\Box-\mu^2$ requires four mutually anticommuting generators, one of square $+1$ and three of square $-1$. The three spatial units supply the three spatial generators, $\psi\mapsto i\vec e_k\psi\vec e_y$, and no element of the algebra supplies the fourth; the fourth multiplies on the right, $\psi\mapsto i\psi\vec e_x$. The root therefore acts on both sides of the algebra, which is where the four complex dimensions come from, while the Klein–Gordon operator itself stays central.

The mass is constrained by the anticommutator with the four generators. The maps that anticommute with all four are the multiples of $\psi\mapsto\psi\vec e_z$, so the only single-operator solution is $\psi\mapsto\pm\mu\psi\vec e_z$, a pseudoscalar mass. A scalar mass commutes with the generators, so no single operator with a scalar mass squares to Klein–Gordon; the scalar mass admits only the factorisation $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}$, which is the corpus's chiral pair. The physical mass is the scalar one, so the physical first-order equation is one factor of that factorisation.

The two equations are distinct, and the notation keeps them so: $\mathsf D_{\mathrm{ps},\pm}\psi=0$ is the single square, and $\mathsf D_{\mathrm{sc},\pm}\psi=0$ is the chiral pair. Only the second is physical.

A field whose value is one complex number has no first-order root. The results are a classification of form: no mass, no coupling and no dynamics are predicted. The open questions are the gauged, curved, position-dependent and real-structure extensions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The four units |
| $i$ | The central imaginary unit |
| $Q_\mu$ | The algebra coordinates |
| $x_\mu$ | The Lorentz coordinates |
| $\tilde\nabla$ | Biquaternionic gradient |
| $\Box$ | d'Alembertian; its Lorentz form is derived in §*The Equation* |
| $c$ | The speed of light in the medium |
| $\mu$ | The mass parameter, $\mu=mc/\hbar$, the inverse reduced Compton wavelength |
| $k_\mu$ | The wave covector of a plane wave |
| $\psi$ | A general element of $\mathbb{B}$, on which the root acts |
| $\psi_L,\psi_R$ | The two parts of an element, the two values of the label |
| $G_0:\psi\mapsto i\psi\vec e_x$ | Time generator, a multiplication on the right |
| $G_k:\psi\mapsto i\vec e_k\psi\vec e_y$ | The three spatial generators |
| $\mathsf D$ | Derivative part of the root, $\mathsf D^2=\Box$ |
| $\mathsf D(k)$ | Symbol of $\mathsf D$ at the wave covector $k$ |
| $\mathsf B$ | Zero-order term of a first-order operator, a fixed map with no derivative |
| $\mathsf D_{\mathrm{ps},\pm}\psi=\mathsf D\psi\pm\mu\psi\vec e_z$ | Single-square roots, pseudoscalar mass |
| $\mathsf D_{\mathrm{sc},\pm}\psi=\mathsf D\psi\pm\mu\psi$ | Scalar-mass factors, the chiral pair |
| $\tilde\Phi$ | The field of the Klein–Gordon equation, an element of $\mathbb{B}$ |
| the label | $L$ or $R$, two values, carried by the parts of an element |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the identity $(\mathsf D-\mu)(\mathsf D+\mu)=\Box-\mu^2$ and the plane-wave solutions.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra, the gamma matrices, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the classification of Clifford algebras, the minimal modules, and the square root of the wave operator.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the complex and real Clifford algebras and their irreducible modules.
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the periodicity and the module dimensions.
- V. V. Kravchenko, *Quaternionic Analysis and Its Applications* (Birkhäuser, 2003), for the quaternionic Dirac operator and its relation to the Euclidean Clifford algebra.
- The corpus articles *The Klein–Gordon Equation in Biquaternionic Form*, *Klein–Gordon from the Dirac Square in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form*, *The Biquaternion D'Alembertian and Its Green's Functions*, and *Algebra and Element Conventions* for the conventions and the results this article builds on.
- The corpus articles *Two-Sided Operators on the Biquaternion Algebra*, *Element and Operator Representations: The Three Actions*, and *The Polarized Module of the Biquaternion Algebra* for the two-sided algebra, the nilpotent that exchanges the two parts of an element, and the change of display between the two bases.

