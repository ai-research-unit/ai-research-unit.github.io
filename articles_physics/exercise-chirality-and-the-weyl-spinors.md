# __Exercise: Chirality and the Weyl Spinors__

## Introduction

This is one of the articles of the Dirac exercise series accompanying the biquaternion Dirac equation, and the one that stays inside the algebra from the first line to the last. It is a worked exercise: the structures are taken from the parent article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and then applied. The value is in the solutions.

The following are assumed.

- The algebra, the units, the sectors and the conjugations are those of *Algebra and Element Conventions*; the two parts named by the subscript are those of *Special Element and Peirce Conventions*, §*The Spin and Spinor Convention*; the biquaternionic gradient and the d'Alembertian are those of *Operator and Calculus Conventions*; and the four forms are those of *Product and Form Conventions*. None of them is restated here.
- The field is one element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$. Its two parts $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$ carry the two parts named by the subscript, and they are named in Problem 1.
- The group $SL(2,\mathbb{C})$ is the set of unit elements, and $\pi$ is its double cover of $SO^{+}(1,3)$, acting on $\mathbb{B}_{\Phi}$ (*Norm and Unitary Conventions*, §*The Unitary Convention*; the parent article).
- The two actions. On one part the group acts by left multiplication, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U\tilde{Ξ}_{\mathrm{sp}}$; on the other by left multiplication with the coefficient conjugate, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\bar{\tilde U}\,\tilde{Ξ}_{\mathrm{sp}}$ (the parent article, §*The Two Halves*).
- The forms. The quaternionic form $\langle X,Y\rangle_{\natural}$, the Hermitian form $\langle X,Y\rangle_{*}$ and the biquaternion norm $\langle X\rangle_{\natural}$ (*Product and Form Conventions*, §*The Form Convention*; *Norm and Unitary Conventions*, §*The Norm Convention*). Their formulas are theirs and are not restated here.

Seven problems are worked below, one per section.

## Problem 1: The Two Values of the Chirality

**One declared direction, and nothing else.** A frame is declared once, by a unit vector $\vec u$ of the algebra, real and of square $\vec u^2=-e_t$. It is the only datum the exercise adds to the algebra, it is a property of the frame, and no element of any problem carries it.

**The value is the subscript.** The subscript takes two values and there are exactly two. The part of the minus value is written $\tilde{Ξ}_{\mathrm{sp},L}$ and the part of the plus value is written $\tilde{Ξ}_{\mathrm{sp},R}$, in the letters of §*The Slot Label, Which Is the Chirality* of *Operator Family Conventions*; the basis operator that carries it is the right multiplication $-iR_{\vec u}$, named once here as the conventions name it (*Special Element and Peirce Conventions*, §*The Spin and Spinor Convention*). The side is the chirality; the basis operator is an example of the right slot, and its value is what the subscript records. **That is the whole definition, and no formula is written for it**: the value is named, not computed.

**Three facts, in words.** Every element is the sum of one part of each value, and only the zero element is both. A product takes the letter of its right factor. Left multiplication keeps the letter, whatever the left factor.

**Lorentz invariance.** The group acts by left multiplication, so a unit element keeps the letter of each part, and the value of a part is unchanged by the Lorentz action. Residual $9\times10^{-16}$ over $100$ random left factors, and $1\times10^{-15}$ over $100$ products. Parity is not a left multiplication, and it is what exchanges the two values (the parent article, §*The Two Halves*).

**The two values are not told apart by the algebra.** Both values are carried by one and the same module, and a left multiplication acts on both in the same way; nothing in the algebra separates them until the conjugate action enters, and that action is the subject of Problem 3.

**The companion route.** The source recorded in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation* reaches the same two values from the light-cone basis. The two labellings agree through the correspondence between that chiral algebra and the Weyl system, which the source verifies row by row, and not by any decomposition of the field used here.

## Problem 2: The Two Weyl Halves and the Mass Term

This problem writes every mass through $k_m=m\,c/\hbar$ and every phase through $\omega r'_t/c$; the mass-shell paragraph gathers the two factors.

**The gradient.** The biquaternionic gradient $\tilde\nabla$ is one element and acts by left multiplication (*Operator and Calculus Conventions*, §*The Operators*). It therefore keeps each letter (Problem 1), and its quaternion conjugate $\tilde\nabla^{\natural}$ is a conjugation of the same operator and not a second derivative.

**The chiral pair.** The dynamics is the one-sided chiral pair of the parent article: two equations, one per value,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L} ,
$$

$$
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R} .
$$

The first acts on the part $\tilde{Ξ}_{\mathrm{sp},R}$, the second on the part $\tilde{Ξ}_{\mathrm{sp},L}$, and the second is the quaternion conjugate of the first. The mass is the term that carries one value to the other; it is the only such term, because a left multiplication preserves each value.

**The massless case.** Setting $m=0$, the two equations decouple:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0 .
$$

Each is a one-sided equation for one value, and neither contains the other part. Each is a **Weyl equation**, one per value, and the massless field is two independent one-sided fields.

**The massive case.** Apply $\tilde\nabla^{\natural}$ to the first equation and use the second:

$$
\tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\,\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m^{2}\tilde{Ξ}_{\mathrm{sp},R} .
$$

The product $\tilde\nabla^{\natural}\tilde\nabla$ is the d'Alembertian $\Box$, the quaternionic norm of the gradient, an operator of the algebra and not of a sector (*Operator and Calculus Conventions*, §*The Quaternionic Bilinear Product, Its Form and Its Norm*, where it is defined and where the uniqueness of the operator is stated). Hence

$$
\left(\Box-k_m^{2}\right)\tilde{Ξ}_{\mathrm{sp},R} = 0, \qquad \left(\Box-k_m^{2}\right)\tilde{Ξ}_{\mathrm{sp},L} = 0,
$$

and with $\frac{m\,c}{k_m}$ and $c$ restored the same statement is $(\Box - k_m^{2})\tilde{Ξ}_{\mathrm{sp}}=0$. The sign on the time term of $\Box$ is the series convention of the material sector, and the article uses that one operator and no second one. Thus the mass term, and only the mass term, relates the two parts: when $m=0$ each part separately obeys a one-sided equation; for $m\neq0$ it obeys the Klein–Gordon equation. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**Mass shell.** For a plane wave $\tilde{Ξ}_{\mathrm{sp}}\propto\exp(-ik_{t}^{\prime}x_0+i\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$ with $x_0 = r'_{t}$, the Klein–Gordon equation gives $k_{t}^{\prime\,2} = \vec k_\Phi^2 + k_m^{2}$. Equivalently, with the four-momentum $\tilde{P}_{\Phi} = iE/c\,e_t + \vec p\in\mathbb{B}_{\Phi}$ and $k =\frac{k_m\,P}{m\,c}$,

$$
\langle\tilde{P}_{\Phi}\rangle_{\natural} = \tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -\frac{E^2}{c^2} + \vec p^2 = -m^2c^2 \qquad(\vec p^2=|\vec p|^2),
$$

i.e. $E^2 = \vec p^2c^2 + m^2c^4$. Here $k_{\Phi}=\frac{k_m\,p}{m\,c}$ and $k_{t}^{\prime}=E/(\frac{m\,c^{2}}{k_m})$ are the momentum and energy wave numbers.

**The second Dirac equation.** Two equations carry the name, and they must not be read as one. The pair above is the **one-sided** form of the equation: both gradients act by left multiplication, the field is one element, and the mass is the coupling between the two values. The **two-sided** form of the equation is a single field equation on $F\in\mathbb{B}$, Kravchenko's form,

$$
\left(i\frac{\partial}{\partial r'_t}+D_3\right)F - mi\,\bar F\,\vec u = 0, \qquad D_3=\sum_k\vec e_k\frac{\partial}{\partial R_k},
$$

in which the derivative acts from the left, the coefficient conjugation $\bar{\cdot}$ acts with no side, and the mass term ends in a right multiplication by the declared unit $\vec u$. At $\vec u=\vec e_z$ this is the form the parent article prints. The two equations are related by the dictionary and are not the same operator: the mass of the pair is the coupling of one value to the other; the mass of the two-sided equation is a conjugation together with a direction. Chirality is why the second side is needed at all: left multiplication preserves each value, so no left multiplication, and no sum of left multiplications, carries one value into the other. The pair is the definition; the two-sided equation is its single-field compression, and the conjugation is the price of that compression.

Three conjugations must not be confused. The coefficient conjugation $\tilde{Ξ}_{\mathrm{sp}}\mapsto\bar{\tilde{Ξ}}_{\mathrm{sp}}$ is the antilinear map that relates the defining action to its conjugate; the Hermitian star $\tilde{Ξ}_{\mathrm{sp}}^*=\bar{\tilde{Ξ}}_{\mathrm{sp}}^{\,\natural}$ is its composition with the quaternion conjugation; and the parent's anti-Hermitian conjugation $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ is the algebra's real structure, with fixed space $\mathbb{B}_{\Phi}$. None of the three is the mass. The exercise therefore treats the mass term in the explicit pair, where it is unambiguous.

## Problem 3: A Boost and a Rotation of Each Half

The two distinguished unit elements are the frame rotor of a boost, $\tilde U_{\Psi,\mathrm b}$, and the rotor of a rotation, $\tilde u_{\mathrm r}$; their formulas are those of the notation table of *Algebra and Element Conventions*, §*Summary of Notation*, and the group they generate is that of *Norm and Unitary Conventions*, §*The Unitary Convention*. Two of their properties are used below: the boost rotor is Hermitian, with a real scalar part and an imaginary vector part, and the rotation rotor is a real quaternion. Both are of norm one.

**Boost.** A boost has a real scalar part and an imaginary vector part, so its coefficient conjugate negates the vector part: $\bar{\tilde U}_{\Psi,\mathrm b} = \tilde U_{\Psi,\mathrm b}^{\natural}$. Its norm is one, so $\tilde U_{\Psi,\mathrm b}^{\natural} = \tilde U_{\Psi,\mathrm b}^{-1}$. Hence

$$
\bar{\tilde U}_{\Psi,\mathrm b} = \tilde U_{\Psi,\mathrm b}^{-1},
$$

at residual $9\times10^{-16}$ over $200$ rapidities, and the two parts transform by **inverse** elements: one by left multiplication with $\tilde U_{\Psi,\mathrm b}$, the other by left multiplication with $\tilde U_{\Psi,\mathrm b}^{-1}$. A boost stretches one part where it contracts the other. This opposition of the two parts under boosts is the representation-theoretic content of the labels left and right.

**Rotation.** A rotation rotor is a real quaternion, so $\bar{\tilde u}_{\mathrm r} = \tilde u_{\mathrm r}$ and both parts transform by the **same** element. The two values are therefore isomorphic as modules of the compact subgroup, and they separate only under boosts, the defining representation of $SU(2)$ being self-conjugate and that of $SL(2,\mathbb{C})$ not.

**The exact relation for a general rotor.** For every unit element,

$$
\bar{\tilde U}=\bigl(\tilde U^{*}\bigr)^{-1},
$$

at residual $1\times10^{-15}$ over $1000$ unit elements. The proof is two lines: the bar and the quaternion sign commute, so $\bar{\tilde U}=\bigl(\tilde U^{\natural}\bigr)^{*}$, and at norm one $\tilde U^{\natural}=\tilde U^{-1}$.

The **Hermitian star** $\tilde U^{*}$ is a different conjugation and a different element: $\tilde U^{*}=\bar{\tilde U}^{\,\natural}$, which equals $\bar{\tilde U}$ for a rotation and differs for a boost, where $\bar{\tilde U}=\tilde U^{-1}$ while $\tilde U^{*}=\tilde U$. The parent states that the right-handed action is "equivalent to the coefficientwise-conjugate action, the two differing by conjugation with the invariant tensor"; the identity above is the exact statement of that equivalence, and it needs no tensor, because the inverse is what the conjugate action requires and only $(\tilde U^{*})^{-1}$ leaves the pairing of Problem 7 invariant.

## Problem 4: The Invariant Form and Self-Duality

**Invariance.** The quaternionic form is invariant under the Lorentz action:

$$
\langle\tilde UX,\tilde UY\rangle_{\natural}
=\mathrm{Sc}\bigl(X^{\natural}\tilde U^{\natural}\tilde UY\bigr)
=\mathrm{Sc}\bigl(X^{\natural}Y\bigr)
=\langle X,Y\rangle_{\natural}
$$

for every unit element, at residual $4\times10^{-15}$ over $100$ pairs. Only the norm-one condition is used, so the form is invariant under the whole group and not under a subgroup of it. The conjugate action preserves it as well, at residual $4\times10^{-15}$ over $100$ pairs, the coefficient conjugate of a unit element being a unit element.

**It vanishes on one value.** Two elements of the same value are never paired: $\mathrm{Sc}(X^{\natural}Y)=0$ when $X$ and $Y$ carry the same value, at residual $2\times10^{-16}$. The form pairs one value with the other.

**Nondegeneracy.** On the pair (one value, the other) the form is nondegenerate. At $\vec u=\vec e_z$ the minus value is spanned by $e_t+i\vec e_z$ and $\vec e_x-i\vec e_y$, and the plus value by $e_t-i\vec e_z$ and $\vec e_x+i\vec e_y$; the form takes the value $2$ on each pair of corresponding elements of the two lists and $0$ on each crossed pair (residual $<10^{-14}$), so it is nondegenerate.

**Self-duality.** A nondegenerate invariant bilinear form carries a value onto the dual of the other, and the pairing is symmetric, so it carries each value onto its own dual as well. The dual of a value is a value, and each value is self-dual.

This is **not** self-conjugacy. The conjugate action is a different action, and a value is not its conjugate; the two are related by the identity of Problem 3 and by nothing weaker. The distinction is the parent's warning that self-duality is not self-conjugacy, and it is why a pair of elements of one value has an invariant contraction while an element of one value and an element of the other need the separate mixed pairing of Problem 7.

**The four forms.** None of the four forms of *Product and Form Conventions* is antisymmetric. The invariant bilinear form the algebra supplies is the quaternionic one, it is symmetric, and the antisymmetric contraction of the older calculus is a property of the carrier and not one of the four.

## Problem 5: The Bilinear and the Four-Vector

The parent article introduces the bilinear of two elements of one value,

$$
\tilde{Q} = w\,v^{*},
$$

and its transformation law is immediate:

$$
(w\,v^{*})\;\longmapsto\;(Uw)(Uv)^{*}=U\,(w\,v^{*})\,U^{*}.
$$

**Hermiticity and the general four-vector map.** The element $w v^{*}$ is Hermitian if and only if $w$ and $v$ are proportional by a real factor; in general it is an element of the full algebra $\mathbb{B}$, not of the Hermitian subspace. The bilinear that lands in the Hermitian subspace $\mathbb{B}_{\Psi}$ (real dimension four) is the **Hermitian part**

$$
H(w,v) = \tfrac12\left(w\,v^{*} + v\,w^{*}\right)\in\mathbb{B}_{\Psi} .
$$

For $v = \pm w$ this reduces to $H = \pm ww^{*}$, and the parent's unsymmetrised $\tilde{Q} = wv^{*}$ is then already Hermitian. In general one must symmetrize. The four-vector associated with the pair is

$$
V(w,v) = i\,H(w,v) \in \mathbb{B}_{\Phi} ,
$$

where the last inclusion uses $i\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$.

**Biquaternion norm.** Write $H = r_t\,e_t + i\vec r_\Psi$. Then $V = i r_t\,e_t - \vec r_\Psi$, and

$$
\langle V\rangle_{\natural} = \langle iH\rangle_{\natural} = -\langle H\rangle_{\natural} = -r_t^2 + \vec r_\Psi^2 \qquad(\vec r_\Psi^2=|\vec r_\Psi|^2),
$$

which is the $(3,1)$ Minkowski form of $\mathbb{B}_{\Phi}$. The check is the single-element case: for $v = w$ of one value one has $H = ww^{*}$, whose quaternionic norm vanishes (residual $<10^{-14}$ over $100$ elements), so

$$
\langle V\rangle_{\natural} = 0 .
$$

A single element of one value therefore determines a **null** four-vector — its flag direction.

**Explicit example.** At $\vec u=\vec e_z$ take $w = v = \tfrac12\left(e_t+i\vec e_z\right)$, of the minus value. Then

$$
H = ww^{*} = \tfrac12\left(e_t+i\vec e_z\right), \qquad V = iH = \tfrac{i}{2}\,e_t-\tfrac12\,\vec e_z,
$$

of components $(q_t,q_x,q_y,q_z) = \left(\tfrac{i}{2},0,0,-\tfrac12\right)$ and norm $\langle V\rangle_{\natural} = \left(\tfrac{i}{2}\right)^2+\tfrac14 = 0$ (residual $<10^{-15}$).

**Why the two elements must share a value.** For $w$ and $v$ of one value the product $wv^{*}$ is of rank one; for two general elements of the algebra it is of rank two. The shared value is what makes the product rank one, and the symmetrisation above is what the general pair needs before a four-vector is read from it.

## Problem 6: The Double Cover on a Concrete Rotation

Take a rotation about $\vec e_z$ by angle $\theta$, with rotor $\tilde u_{\mathrm r}(\theta)$.

**On the field.** At $\theta = 2\pi$ the rotor is $\tilde u_{\mathrm r}(2\pi) = \cos\pi\,e_t = -e_t$, so the left multiplication sends every field to its negative, $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}$, which is not the identity. At $\theta = 4\pi$ the rotor is $\tilde u_{\mathrm r}(4\pi) = \cos 2\pi\,e_t = e_t$, and the field returns to itself.

**On the four-vector.** The four-vector action is the two-sided operator with the rotor. At $\theta = 2\pi$,

$$
(-e_t)\,V\,(-e_t)^{*} = (-e_t)\,V\,(-e_t) = e_t\,V\,e_t = V,
$$

using $(-e_t)^{*} = -e_t$. So a $2\pi$ rotation acts as the identity on every four-vector, identically and not approximately. At $\theta = 4\pi$ the rotor is $e_t$ and both actions are the identity.

**The general statement.** The two behaviours are the two entries of the parent's table:

$$
\pi:\;SL(2,\mathbb{C})\longrightarrow SO^{+}(1,3), \qquad
\ker\pi = \{\pm e_t\}\cong\mathbb{Z}/2\mathbb{Z},
$$

while the field action $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U\tilde{Ξ}_{\mathrm{sp}}$ has trivial kernel, since $-e_t$ is not $e_t$. Hence

$$
\boxed{\;SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}\;},
$$

and $SL(2,\mathbb{C})$ is the double cover.

## Problem 7: The One-Sided Action and the Two-Sided Operator

**From the one-sided action to the two-sided operator.** Let $w,v$ be of one value and form $V = V(w,v) = i\cdot\tfrac12(wv^{*}+vw^{*})\in\mathbb{B}_{\Phi}$. Under the field action $w\mapsto Uw$, $v\mapsto Uv$, the bilinear transforms as

$$
V \;\longmapsto\; U\,V\,U^{*},
$$

which is exactly the two-sided operator of the material sector. One element of the field contributes one factor, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U\tilde{Ξ}_{\mathrm{sp}}$ (linear, one-sided); the four-vector is built from two of them and therefore carries two factors, $UVU^{*}$ (quadratic, two-sided). This is the origin of the difference in kind between the two actions, and it is the sense in which the four-vector is a *pair* of elements.

**The sign that cancels and the sign that does not.** Replace $\tilde U$ by $-\tilde U$. On four-vectors $(-U)V(-U)^{*} = UVU^{*}$, because the two signs cancel; on the field $(-U)\tilde{Ξ}_{\mathrm{sp}} = -U\tilde{Ξ}_{\mathrm{sp}}\neq U\tilde{Ξ}_{\mathrm{sp}}$ for every nonzero field. Hence $\ker\pi = \{\pm e_t\}$ on $\mathbb{B}_{\Phi}$ but the kernel of the field action is trivial: the field action does not descend to $SO^{+}(1,3)$.

**Composition.** Successive rotors compose by multiplication in both pictures: $\tilde U_2(\tilde U_1\tilde{Ξ}_{\mathrm{sp}}) = (\tilde U_2\tilde U_1)\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde U_2(\tilde U_1V\tilde U_1^{*})\tilde U_2^{*} = (\tilde U_2\tilde U_1)V(\tilde U_2\tilde U_1)^{*}$. The difference is only the doubled factor, and hence the cancelling sign, in the four-vector formula.

**The mixed pairing.** Finally, the Hermitian form on one value and the other, with $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U\tilde{Ξ}_{\mathrm{sp}}$ and $\xi\mapsto\bar{\tilde U}\xi$, is invariant:

$$
\boxed{\;\langle\tilde U\tilde{Ξ}_{\mathrm{sp}},\;\bar{\tilde U}\xi\rangle_{*}
= \mathrm{Sc}\bigl(\tilde U\tilde{Ξ}_{\mathrm{sp}}\,(\bar{\tilde U}\xi)^{*}\bigr)
= \mathrm{Sc}\bigl(\tilde U\,\tilde{Ξ}_{\mathrm{sp}}\xi^{*}\,\bar{\tilde U}^{\,*}\bigr)
= \mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}\xi^{*}\bigr)
= \langle\tilde{Ξ}_{\mathrm{sp}},\xi\rangle_{*}\;},
$$

at residual $5\times10^{-15}$, because $\bar{\tilde U}^{\,*} = \tilde U^{-1}$ by the identity of Problem 3, and because the scalar part of a product is unchanged when the product is conjugated by an element and its inverse. The action is **not** the Hermitian-star one, $\xi\mapsto\tilde U^{*}\xi$: with $\tilde U^{*}$ in place of $\bar{\tilde U}$ the element would be conjugated by $\tilde U$ on both sides, $\mathrm{Sc}(\tilde U\,\tilde{Ξ}_{\mathrm{sp}}\xi^{*}\,\tilde U)$, which is not $\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}\xi^{*})$ in general, and the pairing would be invariant only for the elements of the compact subgroup, where the two conjugations agree. This is the Dirac scalar bilinear.

## Limiting Cases

The solutions have the expected limits.

- **Rapidity limits.** As $\theta_{\mathrm{rpd}}\to0$ both parts become indistinguishable, reflecting that the chiral splitting is a property of the full Lorentz group, not of its compact subgroup; for large $\theta_{\mathrm{rpd}}$ the parts diverge exponentially, one part stretched by $\exp(\theta_{\mathrm{rpd}}/2)$ and the other contracted by $\exp(-\theta_{\mathrm{rpd}}/2)$.
- **$v = \pm w$ (one element):** $H = \pm ww^{*}$ has vanishing norm, so $V$ is null. For a generic pair, $V$ is timelike or spacelike according to the sign of $\langle V\rangle_{\natural} = -r_t^2+\vec r_\Psi^2$.
- **$\theta = 2\pi$ versus $4\pi$:** the field picks up $-1$ at $2\pi$ and returns at $4\pi$, while the four-vector is unchanged at both — the double cover in its simplest instance.

## What the Solutions Illustrate

**1. The parent's structures are sufficient, once the field is one element.** All seven problems use only the algebra, the declared direction, the two values, and the forms. The only extra structure is the declared direction of the frame, which is a property of the frame and not of the algebra.

**2. Chirality is a real-structure notion.** The two values are invisible to the algebra as a complex algebra, where a left multiplication acts on both alike; they become visible only through the conjugate action, which the coefficient conjugation supplies.

**3. The four-vector is the bilinear shadow of the field.** The two-sided operator on $\mathbb{B}_{\Phi}$ arises from the one-sided action through the Hermitian part; the vector action is two factors of the field, and that is why it is quadratic where the field action is linear.

**4. The double cover is a kernel statement.** $\ker\pi = \{\pm e_t\}$ on the four-vectors, but trivial on the field; the difference is one factor of the rotor versus two.

## Notes on the Parent Article

Three points arose where the parent either leaves a definition to convention or uses a shorthand that is not general. They are recorded here as findings; the choices used above are stated explicitly.

1. **Right-handed action, exact form.** The parent says the right-handed action is "equivalent to the coefficientwise-conjugate action, the two differing by conjugation with the invariant tensor"; it does not give the identity. The precise identity is $\bar{\tilde U}=(\tilde U^{*})^{-1}$, verified numerically, and it is a statement about elements and needs no tensor: the bar and the quaternion sign commute, and at norm one the quaternion sign is the inverse. Two points of notation had to be settled for it. The conjugation that carries the conjugate action is the **coefficientwise** one, $\bar{\tilde U} = (\tilde U^{*})^{\natural}$; the star by itself is the Hermitian conjugation, which gives $\tilde U^{*}$ and not the inverse. And the inverse is what the conjugate action needs, since only $(\tilde U^{*})^{-1}$ leaves the Hermitian pairing invariant.

2. **The field-to-vector map for a general pair.** The parent writes $\tilde{Q} = uv^{*}$ (its $u,v$ are the $w,v$ used here) and warns that for a generic pair $iuv^{*}$ does not lie in $\mathbb{B}_{\Phi}$ and is therefore not a four-vector; it then supplies the symmetrised map $H = \tfrac12(wv^{*}+vw^{*})\in\mathbb{B}_{\Psi}$, with four-vector image $V = iH\in\mathbb{B}_{\Phi}$. The exercise uses that symmetrised map. The shorthand $\tilde{Q} = wv^{*}$ is general, but the identification of $i\tilde{Q}$ with a four-vector is not, and neither is the rank-one property, which needs the two elements to share a value.

3. **The biquaternion mass term and the conjugate action.** The parent's massive equation is the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, whose mass term relates the two parts, with the anti-Hermitian conjugation $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ the algebra's real structure rather than the mass. The exercise keeps its mass term in the explicit pair, where it is unambiguous. The parent exhibits the conjugate action neither as an action on $\mathbb{B}$ nor as an isomorphism between the two readings of the field.

A fourth point, the form of the invariant pairing inside the algebra, is the parent's open question 3; Problem 4 answers it, and the answer is the quaternionic form.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. The five frame basis operators are, in the Peirce display,

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

On the chiral pair $(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})$, with the left-handed block first, the same five objects are the matrices

$$
\gamma_0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\qquad
\gamma_k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},
$$

where $\sigma_k$ is the matrix of $i\vec e_k$, and these are the Peirce arrays. In the axis-free display, which is the display of the body, the same five are
$$
\gamma_0=\begin{pmatrix}0&-i&0&0\\i&0&0&0\\0&0&0&i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
the signed permutations $\gamma_0=iR_{\mathrm{axf},\vec e_x}$ and $\gamma_k=iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_{\nu(k)}}$, carried into the Peirce arrays by $C_{\Pi}$. These are the arrays of the four coordinate basis operators of the display, $\gamma_0=C_t$ and $\gamma_k=C_k$, together with the chirality basis operator $\gamma_5$.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame basis operator of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The standard identities.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$:

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

The four contraction sums are fixed by the metric, because a basis operator's square is. With the summed index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, they are $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\alpha\gamma_\beta\gamma_\delta$. With every index low only the first keeps a closed form, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$; the other three are index-dependent and are computed, not transcribed.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Seven problems were solved. (1) The subscript takes two values and there are exactly two; every element is the sum of one part of each, and only the zero element is both; a product takes the letter of its right factor, and left multiplication keeps it, so the value of a part is Lorentz invariant. (2) The massless pair decouples into two independent one-sided equations, one per value; the mass term couples the values, and each part obeys $(\Box-k_m^{2})\tilde{Ξ}_{\mathrm{sp}} = 0$, with mass shell $k_{t}^{\prime\,2} = \vec k_\Phi^2+k_m^{2}$. The one-sided chiral pair is one of the two Dirac equations of the corpus; the two-sided form carries the same chirality coupling in a single equation, with the mass term a conjugation together with a right multiplication by the declared unit. (3) Under a boost the two parts transform by inverse elements, because $\bar{\tilde U}_{\Psi,\mathrm b}=\tilde U_{\Psi,\mathrm b}^{-1}$; under a rotation they transform by the same element, because a rotation rotor is real; in general $\bar{\tilde U}=(\tilde U^{*})^{-1}$. (4) The quaternionic form is invariant, symmetric and nondegenerate, vanishes on each value and pairs one value with the other, so each value is self-dual without being self-conjugate. (5) The bilinear gives $V = i\cdot\tfrac12(wv^{*}+vw^{*})\in\mathbb{B}_{\Phi}$, transforming by the two-sided operator $UVU^{*}$; one element gives a null four-vector, and the vector action is the product of two field factors. (6) A $2\pi$ rotation acts as $-e_t$ on the field and as the identity on four-vectors, and a $4\pi$ rotation as the identity on both: the double cover $SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}$. (7) The two-sided operator is the bilinear shadow of the one-sided action; the sign cancels in the former but not in the latter, and the Hermitian form on one value and the other is invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$ |
| $\mathbb{B}_{C}, \mathbb{B}_{H}$ | Complex subspace (centre), real-quaternion subspace |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Anti-Hermitian (material), Hermitian (informational) subspaces |
| $\langle X\rangle_{\natural} = XX^{\natural}$ | Biquaternion norm; $\langle X,Y\rangle_{\natural}=\mathrm{Sc}(X^{\natural}Y)$ its form |
| $\langle X,Y\rangle_{*} = \mathrm{Sc}(XY^{*})$ | Hermitian form |
| $\vec u$ | The declared unit vector of the frame, $\vec u^2=-e_t$ |
| $-iR_{\vec u}$ | The chirality basis operator of the declared frame |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The two parts of the field, of values $-1$ and $+1$ |
| $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial R_\mu$ | Biquaternionic gradient |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | The d'Alembertian, the quaternionic norm of the gradient |
| $D_3=\sum_k\vec e_k\,\partial/\partial R_k$ | Three-dimensional Cauchy–Riemann operator of the two-sided equation |
| $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}$ | Boost rotor ($\mathbb{B}_{\Psi}$) |
| $\tilde u_{\mathrm r} = \cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}$ | Rotation rotor ($\mathbb{B}_{H}$) |
| $\bar{\tilde U}=(\tilde U^{*})^{-1}$ | The conjugate action for a unit element |
| $H = \tfrac12(wv^{*}+vw^{*})$, $V = iH$ | Hermitian part and four-vector from a pair of elements |
| $SL(2,\mathbb{C})$, $\pi$ | Unit elements; double cover of $SO^{+}(1,3)$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors and the mass term.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- The companion articles of this series: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), and [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html).
