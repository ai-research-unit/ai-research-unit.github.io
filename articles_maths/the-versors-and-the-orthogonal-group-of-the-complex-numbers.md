
# __The Versors and the Orthogonal Group of the Complex Numbers__

## Introduction

The **versors** of the complex numbers are the units of the definite algebraic norm, the elements of norm one, and they form the unit circle $\mathrm{U}(1)$. They are at once the group of linear maps preserving the definite form, which is the rotation group of the plane, and the spin group of the definite space, and the square of the algebra's own product is the two-to-one cover that constitutes the spin structure. This article defines the versors, reads the group they form, records the identification with the group of form-preserving maps, establishes the two-to-one cover and the halving of the parameter that goes with it, and locates the group among the pin and spin groups of the algebra and among the versor groups of the ladder.

The article does not define the two forms, which are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, nor the two algebraic norms $Q_1^{2}$ and $\lvert Q_1\rvert^{2}$ that are their diagonals. The norm, its multiplicativity, the invertibility criterion and the group of units are *Complex Norm and Invertibility*. The identification of $\mathrm{U}(1)$ with the rotation group, the reflections, the group $O(2)$ and the parameter of a rotation are *Rotations and Reflections in the Complex Plane*; they are cited and not restated. The general definition of a versor, the rotor, the Clifford group, the pin and spin groups and the general two-to-one cover are *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

**Conventions.** The algebra is $\mathbb{C}$ over $\mathbb{R}$, with basis $1$, $i$ and $i^{2}=-1$; elements are $Q_1=q_1+iq'_1$ and $Q_2=q_2+iq'_2$ with real $q_1,q'_1,q_2,q'_2$, and conjugation is $\bar Q_1=q_1-iq'_1$. The global reading is bar $=$ complex conjugation and Hermitian star $=$ bar, the complex block reading $\mathbb{C}$ over $\mathbb{R}$ and calling complex conjugation its one nontrivial involution, beside the identity (*Complex Algebra*, *Complexoid Subspaces*, *Conventions in Mathematics*). The definite form is the Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$, with diagonal $\langle Q_1\rangle_{*}=\lvert Q_1\rvert^{2}$; the brackets of the four general forms are reserved for the forms, so elements are written $Q_1$ and $Q_2$ (*The Two Forms and the Two Algebraic Norms of the Complexoid Space*).

## The Versors and Their Group

**Definition.** A **versor** of the complex numbers is a unit of the definite algebraic norm,

$$
\mathrm{U}(1)=\{\,u\in\mathbb{C}:H(u)=\lvert u\rvert^{2}=1\,\},
$$

the set of elements of norm one.

**Proposition (the versors form a group).** The set $\mathrm{U}(1)$ is an abelian group under the multiplication of the algebra, with identity $1$ and inverse $\bar u$ for $u\in \mathrm{U}(1)$; it is the unit circle of the plane.

*Proof.* The definite norm is multiplicative on $\mathbb{C}$ and real-valued (*Complex Norm and Invertibility*): $\langle uv\rangle_{*}=\lvert uv\rvert^{2}=\lvert u\rvert^{2}\lvert v\rvert^{2}=H(u)H(v)$. Hence $H(1)=1$, and if $H(u)=H(v)=1$ then $H(uv)=1$; further $H(u^{-1})=H(u)^{-1}=1$ for $u\neq0$, and $u^{-1}=\bar u/H(u)=\bar u$ on the circle. Associativity and commutativity are inherited from the field.

**Remark (the shell of the definite form is a group, unlike the plain one).** The versor condition is read on the definite algebraic norm $\lvert u\rvert^{2}=H(u)$, not on the plain algebraic norm $u^{2}=B(u)$. On the definite form the norm is multiplicative and positive definite, so its shell is a group. The complex definite case is the one in which the shell is a group for the simplest of reasons, the multiplicativity of a real definite norm on a field.

**Remark (the four elements of the plain shell).** The plain algebraic norm $\langle Q_1\rangle=Q_1^{2}$ is complex-valued, and its shell $\{Q_1:Q_1^{2}=\pm1\}$ is the four-element set $\{1,-1,i,-i\}$, a cyclic group of order four, because $Q_1^{2}$ is multiplicative on the commutative algebra. This set is not the versor group: the versors are the units of the definite norm, and the complex-linear maps preserving the plain bilinear form are only $\pm1$, the index-two subgroup. The two shells belong to the two forms, and the article follows the definite one.

## The Group of Linear Maps Preserving the Definite Form

**The multiplication action.** For $u\in \mathrm{U}(1)$ let

$$
R_{u}:\mathbb{C}\to\mathbb{C}, \qquad R_{u}(Q_1)=uQ_1.
$$

The map $u\mapsto R_{u}$ is an injective homomorphism of groups, because $R_{uv}=R_{u}\circ R_{v}$ and $R_{1}=\mathrm{id}$, and it is injective since $R_{u}(1)=u$ recovers $u$. Each $R_{u}$ preserves the definite form,

$$
H(R_{u}Q_1,R_{u}Q_2)=H(uQ_1,uQ_2)=\lvert u\rvert^{2}H(Q_1,Q_2)=H(Q_1,Q_2),
$$

so every versor acts by a map preserving the form. These are the rotations of the plane, and the identification of the image with the rotation group $\mathrm{SO}(2)$, together with the reading of the parameter, is recorded in *Rotations and Reflections in the Complex Plane*. The two-to-one cover read on this action is the subject of the next section.

**Proposition (the versors are the group of $\mathbb{C}$-linear maps preserving the form).** The $\mathbb{C}$-linear maps preserving $\langle\cdot,\cdot\rangle_{*}$ are exactly the multiplications $R_{u}$ with $\lvert u\rvert=1$, and they form the group $\mathrm{U}(1)\cong \mathrm{SO}(2)$.

*Proof.* A $\mathbb{C}$-linear map of the one-dimensional complex space is $Q\mapsto uQ$ for some $u$, and it preserves $H$ exactly when $\lvert u\rvert^{2}=1$; the identification with the rotation group is the cited one.

**The full orthogonal group.** The $\mathbb{R}$-linear maps preserving $H$ are more numerous: with the matrix $M$ of the map in the real basis $1$, $i$, they are the solutions of the matrix condition

$$
M^{\mathsf T}M=\mathrm{I}_{2},
$$

that is the group $O(2)$. The versors give the maps of determinant $+1$ in it; the maps of determinant $-1$ are the reflections $Q_1\mapsto u\bar Q_1$ with $\lvert u\rvert=1$ (*Rotations and Reflections in the Complex Plane*). The group of the title is thus $O(2)$, and the versors are its determinant-one half.

**Remark (the sandwich is vacuous).** In a non-commutative algebra a unit may act on itself by the sandwich $Q_1\mapsto uQ_1u^{-1}$; here $uQ_1u^{-1}=Q_1$ for every versor, because the algebra is commutative, so the inner action is trivial and multiplication, not conjugation, is the natural action of the versors (*Rotations and Reflections in the Complex Plane*). The double cover below is therefore read on the multiplication, and not on a sandwich.

## The Two-to-One Cover of the Circle

**Theorem (the square map).** The map

$$
\sigma:\mathrm{U}(1)\to \mathrm{U}(1), \qquad \sigma(u)=u^{2},
$$

is a surjective group homomorphism with kernel $\{1,-1\}$, and each element of the target has exactly two preimages, $u$ and $-u$. It is therefore a two-to-one cover of the circle by itself.

*Proof.* For $u,v\in \mathrm{U}(1)$ the identity $\sigma(uv)=(uv)^{2}=u^{2}v^{2}=\sigma(u)\sigma(v)$ holds by associativity and commutativity, and $H(u^{2})=H(u)^{2}=1$ by multiplicativity, so $\sigma$ is a homomorphism into $\mathrm{U}(1)$. Its kernel solves $u^{2}=1$; a field has at most two roots of $X^{2}-1$, and $\pm1$ are two, so the kernel is $\{1,-1\}$. For the surjectivity let $Q_1=q_1+iq'_1$ lie on the circle, $q_1^{2}+q'^{2}_1=1$. If $q_1\neq-1$ the element

$$
z=\sqrt{\frac{1+q_1}{2}}+i\,\frac{q'_1}{\sqrt{2(1+q_1)}}
$$

satisfies $z^{2}=Q_1$ and $H(z)=1$, as expanding the square and using $q_1^{2}+q'^{2}_1=1$ shows; if $q_1=-1$ then $Q_1=-1$ and $z=i$ is a square root on the circle. Every element of the circle is therefore a square, and its two preimages are $z$ and $-z$.

**Theorem (it is the spin structure of the definite space).** Under the identification of $\mathrm{U}(1)$ with the group $\mathrm{SO}(2)$ of maps preserving the form, by the multiplication action (*Rotations and Reflections in the Complex Plane*), the square map is the two-to-one cover $\mathrm{Spin}(2)\to \mathrm{SO}(2)$: the versor whose square names a rotation carries half the parameter of that rotation, and the two versors $u$ and $-u$ name the same one. Read on $\mathbb{C}$ as a complex space it is the spin structure of the one-dimensional definite space, and read on $\mathbb{C}$ as the real plane it is the spin structure of that plane.

*Proof.* The identification carries $u$ to the rotation $R_{u}$, and carries the multiplication of $\mathrm{U}(1)$ to the composition, so $R_{uv}=R_{u}\circ R_{v}$; composing it with $\sigma$ gives the map $u\mapsto R_{u^{2}}=R_{u}\circ R_{u}$, which by the previous theorem is surjective with kernel $\{1,-1\}$, hence two-to-one. The map $R_{u^{2}}$ is the square of $R_{u}$ in $\mathrm{SO}(2)$, so its parameter is twice that of $R_{u}$; the versor carries half the parameter of the map it covers. The parameter of a form-preserving map and its additivity are those of *Rotations and Reflections in the Complex Plane*.

The two versors $u$ and $-u$ therefore name the same map, and no smaller set does: $-1$ is the only nontrivial element killed by the square. This is the spin structure of the definite space in its lowest instance, and it is read entirely inside the algebra, the cover being the square of the algebra's own product.

**Remark (the cover in the multiplication).** Here the algebra is commutative, the sandwich does nothing, and the same halving of the parameter is seen as the doubling of the argument under the square. The complex case is the rung on which the cover is visible in the multiplication alone.

## The Place Among the Pin and Spin Groups

The general theory assigns to a quadratic space its versors, its rotors and the groups $\mathrm{Pin}$ and $\mathrm{Spin}$ (*The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*): a versor is a product of non-isotropic vectors, the even versors of norm one are the rotors, the rotors form the spin group and map onto the special orthogonal group with kernel $\{\pm1\}$, and the reflections are the odd versors.

**Proposition (the complex versors are the rotors).** Read over $\mathbb{R}$, the complex algebra is the even part of the Clifford algebra $\mathrm{Cl}_{2,0}$ of the definite plane, whose bivector $B=e_{1}e_{2}$ satisfies $B^{2}=-1$ and generates the even part, a copy of $\mathbb{C}$. The rotors of that Clifford algebra are the elements $p-Bq$ with $p,q\in\mathbb{R}$ and $p^{2}+q^{2}=1$, and they are $\mathrm{Spin}(2)\cong \mathrm{U}(1)$ (*Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*). Hence the versors of the complex numbers are exactly the rotors, and their group is the spin group of the definite plane.

**The candidate shells of the two forms.** For the definite form the candidate pin and spin groups are its shells,

$$
\mathrm{Pin}_{H}=\{Q_1:H(Q_1)=\pm1\}, \qquad \mathrm{Spin}_{H}=\{Q_1:H(Q_1)=1\}.
$$

Because $H$ is positive definite, the value $-1$ is not attained and the negative shell is empty; the two sets coincide and both are the circle $\mathrm{U}(1)$. The definite form therefore supplies one group and not two, and the versor group is at once its pin group and its spin group. 

**What the algebra does not carry.** A single non-isotropic vector is an odd versor, and its action on the plane is a reflection; the odd part of the Clifford algebra is not the even part and is not the complex algebra. So the reflections are not versors of $\mathbb{C}$, and the full pin group $\mathrm{Pin}(2)$, whose odd half carries them, is not an object of the algebra: only $\mathrm{Spin}(2)=\mathrm{U}(1)$ lies in it. The algebra reaches the rotations and not the reflections, and the reflections are recovered from its own conjugation only as maps ($Q_1\mapsto u\bar Q_1$), not as products of vectors. The general statement is that the pin group lives in the Clifford envelope and not in the algebra.

**Remark (the plain form gives no pin group of the same kind).** For the plain bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ the quadratic form is $\langle Q_1\rangle=Q_1^{2}$, whose shell $\{Q_1:Q_1^{2}=\pm1\}$ is the four-element group of the previous section; but the group of complex-linear maps preserving $B$ is only $\{\pm1\}$, and the realification of $B$ is indefinite, its level sets being hyperbolas and not groups. The versors of the complex numbers are therefore defined by the definite form alone, and the group they form is the spin group of that form.

## The Base of the Versor Ladder

The versors of norm one form, on each rung of the family, the spin group of the definite form of that rung.

| algebra | versors of norm one | group | double cover of | kernel |
|---|---|---|---|---|
| $\mathbb{C}$ | the circle $\mathrm{U}(1)$ | $\mathrm{Spin}(2)\cong \mathrm{U}(1)$ | $\mathrm{SO}(2)$ | $\{\pm1\}$, by the square |
| $\mathbb{H}$ | the unit sphere $S^{3}$ | $\mathrm{Spin}(3)\cong \mathrm{Sp}(1)\cong \mathrm{SU}(2)$ | $\mathrm{SO}(3)$ | $\{\pm1\}$, by the sandwich |

The first row is the present article: the versors are the circle, and the cover is the square of the multiplication. 

The versors of norm one form a group and double-cover the rotations. The complex rung is the base of the ladder and the only rung on which the algebra is commutative, so it is the only one on which the cover is read by the algebra's own product rather than by an inner action.

## Summary

The versors of the complex numbers are the units of the definite algebraic norm, the set $\mathrm{U}(1)=\{u:\lvert u\rvert^{2}=1\}$; they form an abelian group, the unit circle, because the definite norm is real, multiplicative and positive definite on the field. The shell of the plain algebraic norm is the four-element cyclic group $\{1,-1,i,-i\}$, which is not the versor group; the versors are read on the definite form $\langle\cdot,\cdot\rangle_{*}$ alone.

Multiplication by a versor, $R_{u}(Q_1)=uQ_1$, is a $\mathbb{C}$-linear map preserving $H$, and the versors are exactly the group of such maps, identified with the rotation group $\mathrm{SO}(2)$; the full group of $\mathbb{R}$-linear maps preserving $H$ is $O(2)$, given by $M^{\mathsf T}M=\mathrm{I}_{2}$, of which the versors form the determinant-one half and the reflections the other coset. The sandwich is trivial on the commutative algebra, so the action is by multiplication.

The square map $u\mapsto u^{2}$ is a surjective homomorphism of the circle with kernel $\{1,-1\}$, hence a two-to-one cover of the circle by itself; under the identification with $\mathrm{SO}(2)$ it is the cover $\mathrm{Spin}(2)\to \mathrm{SO}(2)$, and the versor carries half the parameter of the map it names. Read over $\mathbb{R}$, the algebra is the even part of $\mathrm{Cl}_{2,0}$, its versors are the rotors $\mathrm{Spin}(2)\cong \mathrm{U}(1)$, and the pin and spin shells of the definite form coincide with the versor group because the negative shell is empty. The odd versors carry the reflections and lie outside the algebra, so the full $\mathrm{Pin}(2)$ is not an object of the algebra. The complex rung is the base of the versor ladder.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1=q_1+iq'_1$, $Q_2=q_2+iq'_2$ | elements of $\mathbb{C}$, with $q_1,q'_1,q_2,q'_2\in\mathbb{R}$ |
| $H(Q_1,Q_2)=Q_1\bar Q_2$ | the definite Hermitian form; diagonal $\lvert Q_1\rvert^{2}$ |
| $B(Q_1,Q_2)=Q_1Q_2$ | the plain bilinear form; diagonal $Q_1^{2}$ |
| $\mathrm{U}(1)=\{u:\lvert u\rvert^{2}=1\}$ | the versors of the complex numbers, the unit circle |
| $R_{u}(Q_1)=uQ_1$ | the multiplication action of a versor; preserves $H$ |
| $\mathrm{U}(1)\cong \mathrm{SO}(2)$ | the versor group is the group of rotations, by multiplication |
| $M^{\mathsf T}M=\mathrm{I}_{2}$ | the condition for preserving $H$; the group $O(2)$ |
| $Q_1\mapsto u\bar Q_1$, $\lvert u\rvert=1$ | the reflection coset of $O(2)$ |
| $\sigma(u)=u^{2}$ | the two-to-one cover $\mathrm{U}(1)\to \mathrm{U}(1)$; kernel $\{1,-1\}$ |
| $\mathrm{Spin}(2)\cong \mathrm{U}(1)$ | the spin group of the definite plane, the rotors of $\mathrm{Cl}_{2,0}$ |
| $\mathrm{Pin}_{H}$, $\mathrm{Spin}_{H}$ | the shells $\{H=\pm1\}$, $\{H=1\}$ of the definite form; both equal $\mathrm{U}(1)$ |
| $\mathrm{Pin}(2)$ | not an object of the algebra; its odd half carries the reflections |
| $\{1,-1,i,-i\}$ | the shell of the plain algebraic norm $Q_1^{2}$, not the versor group |

## Further Reading

- *The Two Forms and the Two Algebraic Norms of the Complexoid Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.md`), for the definite form and the plain form whose shells are compared here.
- *Complex Norm and Invertibility* (`articles_maths/complex-norm-and-invertibility.md`), for the norm, its multiplicativity, the group of units and the polar split.
- *Rotations and Reflections in the Complex Plane* (`articles_maths/rotations-and-reflections-in-the-complex-plane.md`), for the identification $\mathrm{U}(1)\cong \mathrm{SO}(2)$, the reflections and the group $O(2)$.
- *Complex Exponential and Lie Group Structure* (`articles_maths/complex-exponential-and-lie-group-structure.md`), for the exponential, the one-parameter subgroups and the group of units.
- *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* (`articles_maths/versors-rotors-and-the-sandwich-action-with-signed-inner-conjugation.md`), for the general versor, the rotor, the plane case $\mathrm{Spin}(2)\cong \mathrm{U}(1)$ and the two-to-one cover.
- *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* (`articles_maths/the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.md`), for the Clifford group, the pin and spin groups and Cartan–Dieudonné.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for versors, the spin group and the double cover in the low-dimensional cases.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the classical groups and their covers.
