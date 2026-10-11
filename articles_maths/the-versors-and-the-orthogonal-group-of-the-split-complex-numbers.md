# __The Versors and the Orthogonal Group of the Split-Complex Numbers__

## Introduction

The **versors** of the split-complex numbers are the units of norm one, the elements of the unit hyperbola $\mathcal{H}=\{u:N(u)=1\}$. They form a group, and it is at once the group of $\mathbb{D}$-linear maps preserving the indefinite form — the group $SO(1,1)$ of the plane — and the spin group $\mathrm{Spin}(1,1)$ of the split plane, the square of the algebra's own product being the two-to-one cover of its identity component $SO^+(1,1)$. This article defines the versors, reads the group they form and its two branches, records the identification with the group of form-preserving maps, establishes the two-to-one cover and the half-angle that goes with it, and locates the group among the pin and spin groups of the algebra and at the split rung of the family, against the compact circle of the complex case.

The article does not define the two forms, which are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, nor the norm $N$, its polarisation $g$, the invertibility criterion, the group of units or the modulus (*Split-Complex Norm and Invertibility*). The unit hyperbola, its branches and their parametrisation, the exponential, the hyperbolic rotations, the classification of the maps preserving the form and the four components of the group are *Hyperbolic Rotations*, and *Split-Complex Exponential and Lie Group Structure*; they are cited and not restated. The two metrics of the plane are *The Two Metrics of the Split-Complex Numbers*. The general versor, the rotor, the Clifford group, the pin and spin groups and the general two-to-one cover are *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The quaternion and biquaternion rungs are *Quaternion Rotations and Reflections*, *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions* and *Biquaternion Versors and the Orthogonal Group*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^{2}-1)$ over $\mathbb{R}$, with basis $1$, $j$ and $j^{2}=+1$; elements are $A=a+ja'$ and $C=c+jc'$ with real $a,a',c,c'$, and conjugation is $\bar A=a-ja'$. The global reading is bar $=$ the involution $j\mapsto-j$, natural sign $=$ identity and Hermitian star $=$ bar (*Conventions in Mathematics*). The form that defines the versors is the indefinite Hermitian form $H(A,C)=A\bar C$, with diagonal $H(A)=N(A)=a^{2}-a'^{2}$; the four letters $B$, $N$, $H$, $K$ are reserved for the forms, so elements are written $A$ and $C$ (*The Two Forms and the Two Algebraic Norms of the Split-Complex Space*). The group of the title is written $O(1,1)$, its determinant-one half $SO(1,1)$ and its identity component $SO^+(1,1)$: this is the article that carries the algebraic naming of the group, the companion metric article being written with the matrix condition alone. The classification of the form-preserving maps, the four components and the non-compactness are *Hyperbolic Rotations*, cited and not re-derived.

## The Versors and Their Group

**Definition.** A **versor** of the split-complex numbers is a unit of the quadratic form $N$ of norm one,

$$
\mathbb{D}^{(1)}=\{u\in\mathbb{D}:N(u)=u\bar u=1\}=\mathcal{H}=\{u=a+ja':a^{2}-a'^{2}=1\},
$$

the unit hyperbola of *Hyperbolic Rotations*.

**Proposition (the versors form a group).** The set $\mathbb{D}^{(1)}$ is an abelian group under the multiplication of the algebra, with identity $1$ and inverse $\bar u$ for $u\in\mathbb{D}^{(1)}$; it is the unit hyperbola, with the two branches $\mathcal{H}^+$ and $\mathcal{H}^-$.

*Proof.* The norm is multiplicative and real (*Split-Complex Norm and Invertibility*): $N(uv)=N(u)N(v)$. Hence $N(1)=1$, and $N(u)=N(v)=1$ gives $N(uv)=1$; further $N(u^{-1})=N(u)^{-1}=1$ for $u\neq0$, and $u^{-1}=\bar u/N(u)=\bar u$ on the hyperbola. Associativity and commutativity are inherited from the ring.

**Remark (the shell of the indefinite form is a group, and it is a hyperbola).** The versor condition is read on the norm $N=H$, not on the plain algebraic norm $B(A)=A^{2}$. On the norm the form is multiplicative and real, so its shell is a group; here the shell is the hyperbola, of two branches and not compact, in contrast with the compact circle that is the shell of the definite norm of the complex case. The group is $\mathbb{D}^{(1)}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{R}$, with identity component $\mathcal{H}^+=\{e^{\phi j}:\phi\in\mathbb{R}\}\cong(\mathbb{R},+)$ (*Split-Complex Exponential and Lie Group Structure*, *Hyperbolic Rotations*).

**Remark (the shell of the plain form).** The plain algebraic norm $B(A)=A^{2}$ is $\mathbb{D}$-valued, and its shell $\{A:A^{2}=\pm1\}$ is the four-element set $\{1,-1,j,-j\}$, a group $\{1,-1\}\times\{1,j\}\cong(\mathbb{Z}/2\mathbb{Z})^{2}$, because $A^{2}=(a^{2}+a'^{2})+2aa'j$ forces $a^{2}+a'^{2}=1$ and $aa'=0$. The value $-1$ is not attained, since $a^{2}+a'^{2}\geq0$, so this shell is already the solution set of $A^{2}=1$. It is not the versor group: the versors are the units of norm one for the indefinite form $N$, whereas this four-element shell is exactly the group of $\mathbb{D}$-linear maps preserving the Euclidean metric (*The Two Metrics of the Split-Complex Numbers*).

## The Group of Linear Maps Preserving the Indefinite Form

**The multiplication action.** For $u\in\mathbb{D}^{(1)}$ let

$$
R_{u}:\mathbb{D}\to\mathbb{D}, \qquad R_{u}(A)=uA.
$$

The map $u\mapsto R_{u}$ is an injective homomorphism of groups, because $R_{uv}=R_{u}\circ R_{v}$ and $R_{1}=\mathrm{id}$, and it is injective since $R_{u}(1)=u$ recovers $u$. Each $R_{u}$ preserves the indefinite form,

$$
g(R_{u}A,R_{u}C)=N(u)\,g(A,C)=g(A,C),
$$

since $g(uA,uC)=u\bar u\,g(A,C)$ for the polarisation $g$ of the norm (*Split-Complex Norm and Invertibility*), so every versor acts by a map preserving the form. These are the hyperbolic rotations of the plane, whose parametrisation and identification with $SO(1,1)$ are *Hyperbolic Rotations*.

**Proposition (the versors are the group of $\mathbb{D}$-linear maps preserving the form).** The $\mathbb{D}$-linear maps preserving $g$ are exactly the multiplications $R_{u}$ with $N(u)=1$, and they form the group $SO(1,1)\cong\mathcal{H}=\mathbb{D}^{(1)}$.

*Proof.* A $\mathbb{D}$-linear map of the one-dimensional split-complex module over itself is $A\mapsto uA$ for some $u$, and it preserves $g$ exactly when $N(u)=1$, since the displayed computation is an equivalence. The identification of this group with $SO(1,1)$, and of its identity component with the one-parameter group of hyperbolic rotations, is the cited one (*Hyperbolic Rotations*).

**Remark (the isotropic lines are fixed).** The two null lines of the form, the real spans of the idempotents $\Pi_{1}$ and $\Pi_{2}$, are the isotropic lines of the indefinite form and the zero-divisor lines of the ring (*Split-Complex Zero Divisors*). The action $R_{u}$ fixes each of them: in the idempotent basis a versor $u=e^{\phi j}$ scales the two lines by the reciprocal positive factors $e^{\phi}$ and $e^{-\phi}$, so the rotations preserve the two isotropic directions individually while moving the level hyperbolas, and the reflection cosets interchange the two directions. The computation and the eigenvalues $e^{\pm\phi}$ are *Hyperbolic Rotations*, and the two lines are the null pair read in *The Two Metrics of the Split-Complex Numbers*.

**The full orthogonal group.** The $\mathbb{R}$-linear maps preserving $g$ are more numerous: with the matrix $M$ of the map in the real basis $1$, $j$, they are the solutions of the matrix condition

$$
M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1),
$$

that is the group $O(1,1)$, of four components. The versors give its proper half $SO(1,1)$, of two components; the other two cosets are formed by the reflections $A\mapsto u\bar A$ with $N(u)=1$ (*Hyperbolic Rotations*). The group of the title is thus $O(1,1)$, and the versors are its proper half.

**Remark (the sandwich is vacuous).** In a non-commutative algebra a unit may act on itself by the sandwich $A\mapsto uAu^{-1}$; here $uAu^{-1}=A$ for every versor, because the algebra is commutative, so the inner action is trivial and multiplication, not conjugation, is the natural action of the versors. The cover below is therefore read on the multiplication, and not on a sandwich.

## The Two-to-One Cover of the Hyperbola

**Theorem (the square map).** The map

$$
\sigma:\mathbb{D}^{(1)}\to\mathbb{D}^{(1)}_{0}, \qquad \sigma(u)=u^{2},
$$

is a surjective group homomorphism with kernel $\{1,-1\}$, and each element of the target has exactly two preimages, $u$ and $-u$. It is therefore a two-to-one cover of the identity component by the whole norm-one group.

*Proof.* The map is a homomorphism because the multiplication is commutative and associative, and its image lies in $\mathbb{D}^{(1)}$ because $N(u^{2})=N(u)^{2}=1$; the square has both idempotent coordinates $u_{\pm}^{2}>0$ and therefore lies in the identity component. It is surjective onto the identity component because every element of $\mathbb{D}^{(1)}_{0}$ has a square root there, a half hyperbolic angle being available; and $u^{2}=1$ with $N(u)=1$ holds exactly for the two elements $1$ and $-1$, since $j$ satisfies $j^{2}=1$ but has $N(j)=-1$ and so is not a versor.

**Theorem (it is the spin structure of the split plane).** Under the identification of the identity component $\mathbb{D}^{(1)}_{0}$ with the rotation group $SO^+(1,1)$ (*Hyperbolic Rotations*), the square map is the two-to-one cover $\mathrm{Spin}(1,1)\to SO^+(1,1)$, and the versor is the half-angle parameter: the versor of parameter $\phi/2$ squares to the element $e^{\phi j}$ that names the hyperbolic rotation of angle $\phi$. The versors are the spin group $\mathrm{Spin}(1,1)=\mathbb{D}^{(1)}$.

*Proof.* The image of $\sigma$ is the whole identity component, the kernel is $\{1,-1\}$, and the identification carries the multiplication of the hyperbola to the composition of rotations; the parameter of the square is twice the parameter of the versor, which is the half-angle statement.

The two versors $u$ and $-u$ therefore name the same rotation of the identity component, and no smaller set does: $-1$ is the only nontrivial element of the hyperbola killed by the square. This is the spin structure of the split plane, read entirely inside the algebra, the cover being the square of the algebra's own product.

**Remark (the contrast with the complex cover, and with the exponential).** For $\mathbb{C}$ the square map is a cover of the circle by itself, whose target is the whole connected group $U(1)\cong SO(2)$; here the group has two components and the square covers the identity component only, so the double cover $\mathrm{Spin}(1,1)\to SO^+(1,1)$ is a cover of a line, and the versor group is disconnected. The exponential belongs beside this contrast: the map $\phi\mapsto e^{\phi j}$ is a bijection $\mathbb{R}\to\mathbb{D}^{(1)}_{0}$ (*Split-Complex Exponential and Lie Group Structure*), not a periodic map, so the passage from the Lie algebra to the identity component loses nothing and there is no winding, whereas the complex exponential winds the imaginary axis around the circle. On the split plane the two-to-one phenomenon is carried entirely by the square, and the exponential is a bijection whose inverse is a single-valued logarithm on the identity component. The parameter $\phi$ of a rotation is its **rapidity**, the logarithm of the rotation, and the cover is the halving of that rapidity: $\exp(\tfrac{\phi}{2}j)^{2}=\exp(\phi j)$, so the exponential, with the rapidity as the logarithm, and the square are one and the same two-to-one statement read on the two sides of the cover.

**Remark (the contrast with the biquaternion covers).** In the quaternion and biquaternion algebras the corresponding two-to-one cover is produced by the sandwich, and the half-angle appears in the passage from the rotor to the rotation (*Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*, *Biquaternion Versors and the Orthogonal Group*). Here the algebra is commutative, the sandwich does nothing, and the same halving of the parameter is seen as the doubling of the argument under the square. The split-complex case is the rung on which the cover is visible in the multiplication alone, and the group it covers is one component of a group of two.

## The Place Among the Pin and Spin Groups

The general theory assigns to a quadratic space its versors, its rotors and the groups $\mathrm{Pin}$ and $\mathrm{Spin}$ (*The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*): a versor is a product of non-isotropic vectors, the even versors of norm one are the rotors, the rotors form the spin group and map onto the special orthogonal group, and the reflections are the odd versors.

**Proposition (the split versors are the rotors).** Read over $\mathbb{R}$, the split-complex algebra is the even part of the Clifford algebra $\mathrm{Cl}(1,1)$ of the indefinite plane, generated by an orthonormal pair $u$, $v$ with $u^{2}=+1$ and $v^{2}=-1$ (*Split-Complex Norm and Invertibility*); the volume element $\omega=uv$ satisfies $\omega^{2}=uvuv=-u^{2}v^{2}=-(+1)(-1)=+1$ and generates the even part, a copy of $\mathbb{D}$. The rotors of that Clifford algebra are the elements $\cosh\tfrac{\phi}{2}+\omega\sinh\tfrac{\phi}{2}$, and they are the versors $\mathrm{Spin}(1,1)=\mathbb{D}^{(1)}$. So the versors of the split-complex numbers are exactly the rotors, and their group is the spin group of the indefinite plane.

**The candidate shells of the indefinite form.** For the indefinite form the candidate pin and spin groups are its shells,

$$
\mathrm{Pin}_{N}=\{A:N(A)=\pm1\}, \qquad \mathrm{Spin}_{N}=\{A:N(A)=1\}=\mathbb{D}^{(1)}.
$$

Because $N$ is indefinite, both values $\pm1$ are attained, and the two sets are **different**: the norm-one shell is the unit hyperbola, of two branches, and the shell $\{N=\pm1\}$ adds the conjugate hyperbola $\{N=-1\}$, of two more branches. The larger shell is a group, since $N$ is multiplicative, but it strictly contains the versor group, and its elements of norm $-1$ reverse the form rather than preserve it. This is the contrast with the complex definite case, where the value $-1$ is not attained, the negative shell is empty and the pin and spin groups coincide with the circle; it matches instead the biquaternion quaternionic case, whose shell $\{N=\pm1\}$ is strictly larger than its norm-one part and yields two distinct groups.

**What the algebra does not carry.** A single non-isotropic vector is an odd versor, and its action on the plane is a reflection; the odd part of the Clifford algebra is not the even part and is not the split-complex algebra. So the reflections are not versors of $\mathbb{D}$, and the full $\mathrm{Pin}(1,1)$, whose odd half carries them, is not an object of the algebra: only $\mathrm{Spin}(1,1)=\mathbb{D}^{(1)}$ lies in it. The algebra reaches the rotations and not the reflections, and the reflections are recovered from its own conjugation only as the maps $A\mapsto u\bar A$, not as products of vectors. This is the same verdict as for the biquaternion algebra, where the only part of $\mathrm{Pin}(1,3)$ inside the algebra is $\mathrm{Spin}(1,3)=\mathbb{B}^{\times}_{1}$ (*Biquaternion Versors and the Orthogonal Group*), and the general statement is that the pin group lives in the Clifford envelope and not in the algebra.

**Remark (the plain form gives no versor group of the same kind).** For the plain bilinear form $B(A,C)=AC$ the quadratic form is $B(A)=A^{2}$, whose shell $\{A:A^{2}=\pm1\}=\{1,-1,j,-j\}$ is the four-element group of the first section; but that shell is not the versor group, and the realified $B$ is the definite Euclidean form, whose own shell is a circle that is not closed under the multiplication of the algebra. The versors of the split-complex numbers are therefore defined by the indefinite form $N$ alone, and the group they form is the spin group of that form.

## The Split Rung of the Versor Ladder

On each rung of the family the versors of norm one form the spin group of the form of that rung. The split rung sits beside the complex base and shares with it the commutativity of the algebra; what it changes is the sign of the square, and with it the shape of the unit set.

| algebra | versors of norm one | group | double cover of | kernel |
|---|---|---|---|---|
| $\mathbb{C}$ | the circle $U(1)$ | $\mathrm{Spin}(2)\cong U(1)$ | $SO(2)$ | $\{\pm1\}$, by the square |
| $\mathbb{D}$ | the unit hyperbola $\mathbb{D}^{(1)}$ | $\mathrm{Spin}(1,1)\cong\mathbb{D}^{(1)}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{R}$ | $SO^+(1,1)\cong\mathbb{R}$ | $\{\pm1\}$, by the square |
| $\mathbb{H}$ | the unit sphere $S^{3}$ | $\mathrm{Spin}(3)\cong Sp(1)\cong SU(2)$ | $SO(3)$ | $\{\pm1\}$, by the sandwich |
| $\mathbb{B}$ | the norm-one units $\mathbb{B}^{\times}_{1}$ | $\mathrm{Spin}(1,3)\cong SL(2,\mathbb{C})$ | $SO^+(1,3)$ | $\{\pm1\}$, by the sandwich |

The first two rows are the two commutative rungs: the circle of the definite base gives way to the hyperbola of the indefinite one, the connected compact group to a group of two components that is not compact, and the cover of the whole group to the cover of its identity component. The last two rows are the non-commutative rungs, whose cover is produced by the sandwich. The pattern of the ladder is that the versors of norm one form a group and double-cover the rotations; the split rung is the one on which the algebra is commutative, the unit set is a hyperbola, and the covered group is disconnected, so that the cover reaches only its identity component.

## Summary

The versors of the split-complex numbers are the units of norm one, the set $\mathbb{D}^{(1)}=\{u:N(u)=1\}$, which is the unit hyperbola $\mathcal{H}$ with its two branches; they form an abelian group, $\mathbb{D}^{(1)}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{R}$, with identity component $\{e^{\phi j}\}\cong\mathbb{R}$, because the form $N$ is real and multiplicative. The shell of the plain algebraic norm is the four-element group $\{1,-1,j,-j\}$, which is not the versor group; the versors are read on the indefinite form alone.

Multiplication by a versor, $R_{u}(A)=uA$, is a $\mathbb{D}$-linear map preserving the form, and the versors are exactly the group of such maps, identified with $SO(1,1)\cong\mathcal{H}$; the full group of $\mathbb{R}$-linear maps preserving the form is $O(1,1)$, of four components, of which the versors are the proper half and the reflections the other cosets. The sandwich is trivial on the commutative algebra, so the action is by multiplication.

The square map $u\mapsto u^{2}$ is a surjective homomorphism of the hyperbola onto its identity component with kernel $\{1,-1\}$, hence a two-to-one cover; under the identification of the identity component with $SO^+(1,1)$ it is the cover $\mathrm{Spin}(1,1)\to SO^+(1,1)$, and the versor carries half the hyperbolic angle of the rotation it names. Read over $\mathbb{R}$, the algebra is the even part of $\mathrm{Cl}(1,1)$, its versors are the rotors $\mathrm{Spin}(1,1)=\mathbb{D}^{(1)}$, and the pin shell $\{N=\pm1\}$ is strictly larger than the spin shell because the value $-1$ is attained. The odd versors carry the reflections and lie outside the algebra, so the full $\mathrm{Pin}(1,1)$ is not an object of the algebra. The split rung of the ladder sits beside the complex base, its circle replaced by a hyperbola and its connected group by a group of two components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=a+ja'$, $C=c+jc'$ | elements of $\mathbb{D}$, with $a,a',c,c'\in\mathbb{R}$ |
| $H(A,C)=A\bar C$ | the indefinite Hermitian form; diagonal $N(A)=a^{2}-a'^{2}$ |
| $B(A,C)=AC$ | the plain bilinear form; diagonal $B(A)=A^{2}$ |
| $g(A,C)=ac-a'c'$ | the polarisation of $N$, the indefinite form preserved by the versors |
| $\mathbb{D}^{(1)}=\{u:N(u)=1\}=\mathcal{H}$ | the versors, the unit hyperbola of two branches |
| $R_{u}(A)=uA$ | the multiplication action of a versor; preserves $g$ |
| $SO(1,1)\cong\mathcal{H}$ | the versor group is the group of $\mathbb{D}$-linear form-preserving maps |
| $M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1)$ | the condition for preserving $g$; the group $O(1,1)$, four components |
| $A\mapsto u\bar A$, $N(u)=1$ | the reflection cosets of $O(1,1)$ |
| $\sigma(u)=u^{2}$ | the two-to-one cover $\mathbb{D}^{(1)}\to\mathbb{D}^{(1)}_{0}$; kernel $\{1,-1\}$ |
| $\mathrm{Spin}(1,1)=\mathbb{D}^{(1)}$ | the spin group of the indefinite plane, the rotors of $\mathrm{Cl}(1,1)$ |
| $\mathrm{Pin}_{N}$, $\mathrm{Spin}_{N}$ | the shells $\{N=\pm1\}$, $\{N=1\}$ of the indefinite form; the pin shell is strictly larger than the spin shell, which is the versor group |
| $\mathrm{Pin}(1,1)$ | not an object of the algebra; its odd half carries the reflections |
| $\{1,-1,j,-j\}$ | the shell of the plain algebraic norm $A^{2}$, not the versor group |
| $\mathbb{D}^{(1)},U(1),S^{3},\mathbb{B}^{\times}_{1}$ | the versor groups of the ladder |

## Further Reading

- *The Two Forms and the Two Algebraic Norms of the Split-Complex Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-split-complex-space.md`), for the indefinite form and the plain form whose shells are compared here.
- *Split-Complex Norm and Invertibility* (`articles_maths/split-complex-norm-and-invertibility.md`), for the norm, its polarisation, the group of units, the modulus and the Clifford algebra $\mathrm{Cl}(1,1)$.
- *Split-Complex Exponential and Lie Group Structure* (`articles_maths/split-complex-exponential-and-lie-group-structure.md`), for the exponential, the unit-norm group $\mathbb{D}^{(1)}$, its identity component and the unit group as a Lie group.
- *Hyperbolic Rotations* (`articles_maths/hyperbolic-rotations.md`), for the unit hyperbola, the identification with $SO(1,1)$, the hyperbolic rotations, the classification of the form-preserving maps, the reflections and the four components of $O(1,1)$.
- *The Two Metrics of the Split-Complex Numbers* (`articles_maths/the-two-metrics-of-the-split-complex-numbers.md`), for the Euclidean and indefinite metrics, the $\mathbb{D}$-linear preservers of the first and the form-preserving group of the second.
- *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* (`articles_maths/versors-rotors-and-the-sandwich-action-with-signed-inner-conjugation.md`), for the general versor, the rotor and the two-to-one cover.
- *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* (`articles_maths/the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.md`), for the Clifford group, the pin and spin groups and Cartan–Dieudonné.
- *Quaternion Rotations and Reflections* (`articles_maths/quaternion-rotations-and-reflections.md`), for the unit quaternions and the double cover $S^{3}\to SO(3)$.
- *Biquaternion Versors and the Orthogonal Group* (`articles_maths/biquaternion-versors-and-the-orthogonal-group.md`) and *The Pin and Spin Groups of the General Plain Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-plain-algebra-of-biquaternions.md`), for the biquaternion rung and the odd slot that carries the reflections.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for versors, the spin group and the double cover in the low-dimensional cases, including the indefinite plane.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the classical groups and their covers.
