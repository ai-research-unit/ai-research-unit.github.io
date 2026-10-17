# __The Non-Negative Cone and the Coordinatewise Order of the Reduced Biquaternions__

## Introduction

The reduced biquaternion algebra carries, besides its product and its four forms, a cone of positivity that the four real coordinates alone define. An element $Q_\pm=q_++iq'_++j(q_-+iq'_-)$ is declared **non-negative** when all four of its coordinates are non-negative, and the set of the non-negative elements is the **coordinatewise cone**

$$
\mathcal{C}_{+}=\bigl\{Q_\pm=q_++iq'_++j(q_-+iq'_-):\ q_+,q'_+,q_-,q'_-\ge0\bigr\}=\mathbb{R}_{+}^{4},
$$

the positive orthant of the real four-space read in the basis $1,i,j,ij$. The order it defines, $Q_{\pm,1}\succeq Q_{\pm,2}\iff Q_{\pm,1}-Q_{\pm,2}\in\mathcal{C}_{+}$, is the **coordinatewise order**, and it is the order the engineering literature uses when it calls a reduced biquaternion matrix *non-negative*: over an algebra of matrices, the requirement is that each of the four coefficient matrices be a real non-negative matrix, which is the entrywise reading of this cone. The cone is fixed once the real basis is fixed, and it is an order structure of the space, not of the product: it is **not** the cone of an involutive algebra, **not** the null cone of the zero divisors, and **not** the forward cone of the split-complex algebra, and the four are kept apart throughout.

**The results.** $\mathcal{C}_{+}$ is a closed, pointed, generating, **simplicial** convex cone with nonempty interior, whose extreme rays are the four coordinate rays and which is **self-dual** for the Euclidean inner product $\operatorname{Re}K$. It is **not** compatible with the multiplication, and the failure is total: the product of two non-negative elements need not be non-negative, and even the square of a non-negative element can leave the cone. The cone nevertheless meets the null cone, and it meets it in its interior: the first idempotent ray $\mathbb{R}_{+}\Pi_+$ lies in $\mathcal{C}_{+}$, the second does not, and the **strictly positive** element $(1+i)(1+j)=2(1+i)\Pi_+$ is a zero divisor of norm $0$. The multiplications that carry the cone into itself are exactly those by the elements of the **split-complex orthant**
$$
\mathcal{O}=\bigl\{h=h_{0}+h_{2}j:\ h_{0},h_{2}\ge0\bigr\}=\mathbb{R}_{+}\oplus\mathbb{R}_{+}j,
$$
a proper subcone of $\mathcal{C}_{+}$ of real dimension two, which is also the set of the elements whose left multiplication matrix is entrywise non-negative; so the coordinatewise order is preserved by multiplication only along $\mathcal{O}$, and the algebra is not an ordered algebra for it. In the idempotent coordinates the cone is the image of the orthant under the isomorphism $\varphi$, and on the split-complex plane $\mathbb{R}\{1,j\}$ its trace is the cone on the coordinate axes, not the forward cone of the split-complex algebra.

**Boundaries.** The space, the basis and the idempotents are *Reduced Biquaternion Space*; the two complex coordinates and the change of basis are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*; the four real coordinates are *The Four-Vector Element Representation of the Reduced Biquaternions*. The four forms and the algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*; the Euclidean norm $\sqrt{K}$ and the topological reading are *The Euclidean Topology of the Reduced Biquaternion Algebra*. The zero divisors and the null cone are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the classes of element and the cone of squares of the real companion are *The Classes of Element of the Split-Complex Algebra*; the square roots in the reduced biquaternion algebra, where every element has a root, are *Square Roots of a General Element in the Algebra of the Reduced Biquaternions*. The multiplication operators are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*. The general theory of the order is *Ordered Vector Spaces and the Order Unit*, *Positive Operators on an Ordered Space*, *The Cone of Positive Operators* and *Positive Definite Forms on an Ordered Space*; the order of an algebra under its involution is *Ordered Involutive Algebras* and *The Left and Right Multiplication Operators on an Ordered Algebra*, and the comparison between the two orders is the point of the present article.

**Conventions.** The element is $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$, the basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$, the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and the isomorphism with the direct product is $\varphi(Q_\pm)=(Q_{++},Q_{--})$. The four forms are the general plain bilinear $\langle\cdot,\cdot\rangle$, the general quaternionic bilinear $\langle\cdot,\cdot\rangle_{\natural}$, the general plain sesquilinear $\langle\cdot,\cdot\rangle_{*}$ and the general quaternionic sesquilinear $\langle\cdot,\cdot\rangle_{\natural*}$, the last two Hermitian and the last positive definite, with $\langle Q_\pm\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}=q_+^{2}+(q'_+)^{2}+q_-^{2}+(q'_-)^{2}$; the Euclidean inner product of the space is the real part $\operatorname{Re}K$. The order is written $\succeq$ and its cone $\mathcal{C}_{+}$; the split-complex orthant is $\mathcal{O}$ and never $\mathcal{C}_{+}$. The reduced norm of the product is $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-)$, and the null cone is $\mathcal{N}=\{Q_\pm\neq0:\langle Q_\pm\rangle_{\natural}=0\}$.

## The Coordinatewise Order

**The non-negative elements form a closed, pointed, generating, simplicial cone with nonempty interior, and the order they define is a partial order of the real four-space.**

**Definition.** The **coordinatewise cone** of the reduced biquaternion algebra is the set of the elements whose four real coordinates are non-negative, and the **coordinatewise order** is
$$
Q_{\pm,1}\succeq Q_{\pm,2}\iff Q_{\pm,1}-Q_{\pm,2}\in\mathcal{C}_{+},
$$
the difference being taken in the four real coordinates and the requirement being that the four of them be non-negative.

**Theorem (the cone axioms).** The set $\mathcal{C}_{+}$ is a convex cone: it is closed under addition and under multiplication by non-negative reals, it contains the origin, and it is **pointed**, $\mathcal{C}_{+}\cap(-\mathcal{C}_{+})=\{0\}$; it is **generating**, $\mathcal{C}_{+}-\mathcal{C}_{+}=\mathbb{B}_{\mathrm{r}}$; and it is **closed** with nonempty interior, the interior being the set of the elements all of whose four coordinates are strictly positive.

*Proof.* The coordinatewise sum and the non-negative scaling of non-negative quadruples stay non-negative, which is the cone axioms. The pointedness is that a quadruple whose four entries and whose four negatives are non-negative is zero. The generation is that every element is the difference of its coordinatewise positive part and its coordinatewise negative part, $Q_\pm=Q_{\mathrm{pos}}-Q_{\mathrm{neg}}$ with both parts in $\mathcal{C}_{+}$. The closedness is the closedness of the four half-lines; the interior is the set of the quadruples whose four coordinates are strictly positive, which is open and contained in the cone. The vocabulary is that of *Ordered Vector Spaces and the Order Unit*.

**Theorem (the extreme rays and the simplicial form).** The extreme rays of $\mathcal{C}_{+}$ are the four coordinate rays
$$
\mathbb{R}_{+}1,\qquad \mathbb{R}_{+}i,\qquad \mathbb{R}_{+}j,\qquad \mathbb{R}_{+}ij,
$$
and $\mathcal{C}_{+}$ is the **simplicial cone** generated by them,
$$
\mathcal{C}_{+}=\mathbb{R}_{+}1+\mathbb{R}_{+}i+\mathbb{R}_{+}j+\mathbb{R}_{+}ij,
$$
with the four generators linearly independent over $\mathbb{R}$.

*Proof.* An element of $\mathcal{C}_{+}$ is the non-negative combination of the four basis elements displayed with its four coordinates as coefficients, which is the generation; the four rays are extreme because a basis vector cannot be written as a non-negative combination of the others, a single nonzero coordinate forcing the others to vanish; and the linear independence is that of the basis. A cone generated by linearly independent vectors is simplicial.

**Corollary (the cone is not Lorentzian).** Because the four generators are the coordinate axes and not the two idempotent rays, the cone is a simplicial cone of full dimension $4$; it is not the light cone of the form $\langle\cdot,\cdot\rangle_{*}$, which is a cone with a smooth quadric section, and the two are compared on the split-complex plane in §*The Two Complex Coordinates*.

## The Cone and the Multiplication

**The cone is not compatible with the product: the product and even the square of a non-negative element can leave it.**

**Definition.** The product is **compatible with the order** when $Q_{\pm,1}\succeq0$ and $Q_{\pm,2}\succeq0$ imply $Q_{\pm,1}Q_{\pm,2}\succeq0$; the cone is then closed under multiplication, and the order is an order of the algebra.

**Theorem (the incompatibility).** The cone $\mathcal{C}_{+}$ is **not** closed under multiplication, and it is not closed under squaring.

*Proof.* The element $Q_\pm=1+2i$ has coordinates $(1,2,0,0)$ and is non-negative; its square is
$$
(1+2i)^{2}=1+4i+4i^{2}=-3+4i,
$$
with coordinates $(-3,4,0,0)$, whose first coordinate is negative, so $(1+2i)^{2}\notin\mathcal{C}_{+}$. The product of two non-negative elements need not be non-negative, and the same element witnesses that the square of a non-negative element need not be non-negative.

**Corollary (the cone of squares is not the cone).** The image of the squaring map is not $\mathcal{C}_{+}$: the square of the non-negative element $1+2i$ lies outside the cone, so the set of the squares is not the coordinatewise orthant. The cone of squares of the split-complex companion, which is the forward cone $\{h_{0}+h_{2}j: h_{0}\ge|h_{2}|\}$, is likewise not the intersection of $\mathcal{C}_{+}$ with the split-complex plane, and the two differ there by the section taken below.

**Remark (no cone of squares is coordinatewise).** The mechanism is the two square roots of $-1$: the algebra contains $i$ and $ij$, and their squares are $-1$, so an element with a large imaginary coordinate can square to an element with a negative real coordinate. A cone of squares is therefore bounded by null directions of the quadratic forms, and not by the coordinate hyperplanes.

### The Null Cone Inside the Cone

**The cone meets the null cone, and it meets it inside its interior.**

**Theorem (the intersection with the null cone).** The zero divisors of the algebra that are non-negative are exactly the non-zero elements of the first idempotent quadrant,
$$
\mathcal{C}_{+}\cap\mathcal{N}=\bigl\{q\Pi_+:\ q\in\mathbb{C},\ \operatorname{Re}q\ge0,\ \operatorname{Im}q\ge0,\ q\neq0\bigr\}=\mathbb{R}_{+}\Pi_++\mathbb{R}_{+}(i\Pi_+).
$$

*Proof.* The zero divisors are $\mathbb{C}^{\times}\Pi_+\cup\mathbb{C}^{\times}\Pi_-$ (*Zero Divisors of the Algebra of the Reduced Biquaternions*). An element $q\Pi_+=\tfrac{q}{2}(1+j)$ has coordinates $\bigl(\tfrac{\operatorname{Re}q}{2},\tfrac{\operatorname{Im}q}{2},\tfrac{\operatorname{Re}q}{2},\tfrac{\operatorname{Im}q}{2}\bigr)$, non-negative exactly when $\operatorname{Re}q\ge0$ and $\operatorname{Im}q\ge0$. An element $q\Pi_-=\tfrac{q}{2}(1-j)$ has coordinates $\bigl(\tfrac{\operatorname{Re}q}{2},\tfrac{\operatorname{Im}q}{2},-\tfrac{\operatorname{Re}q}{2},-\tfrac{\operatorname{Im}q}{2}\bigr)$, non-negative only when $\operatorname{Re}q=\operatorname{Im}q=0$; so the second idempotent line meets $\mathcal{C}_{+}$ only at the origin, and the intersection is the first quadrant of the first line.

**Corollary (the idempotents).** The idempotent $\Pi_+=\tfrac12(1+j)$ is non-negative, with coordinates $\bigl(\tfrac12,0,\tfrac12,0\bigr)$, and it is a zero divisor; the idempotent $\Pi_-=\tfrac12(1-j)$ is not non-negative, its fourth coordinate being $-\tfrac12$. The two idempotents, which are the extreme rays of the forward cone of the split-complex companion, are therefore separated by the coordinatewise order: one lies on the cone, the other outside it.

**Theorem (a strictly positive zero divisor).** The element
$$
(1+i)(1+j)=1+i+j+ij=2(1+i)\Pi_+
$$
is **strictly positive**, all four of its coordinates being $1$, and it is a **zero divisor** of reduced norm $0$; so the interior of $\mathcal{C}_{+}$ meets the null cone.

*Proof.* The product is $1+i+j+ij$ by the multiplication table, with coordinates $(1,1,1,1)$, all strictly positive; and in the idempotent coordinates $Q_{++}=Q_++Q_-=(1+i)+(1+i)=2(1+i)$ and $Q_{--}=Q_+-Q_-=0$, so the element is $Q_{++}\Pi_+$, of vanishing reduced norm $\langle\cdot\rangle_{\natural}=Q_{++}Q_{--}=0$, hence a zero divisor. The element lies in the interior of the cone and on the null cone at once.

**Remark (the order does not see the zero divisors).** In an ordered algebra the positive cone is meant to be compatible with the product, so that the positive elements have positive products and no interior point is a zero divisor. Here the strictly positive element $(1+i)(1+j)$ is a zero divisor, so **no** multiplicative compatibility can hold, and the coordinatewise order cannot be the order of an ordered algebra. The failure is not a defect of a particular cone: the zero divisors of $\mathbb{B}_{\mathrm{r}}$ are a union of two real planes through the origin, and the orthant of any real basis meets one of them in a set of full dimension.

## The Cone and the Forms

**The cone is self-dual for the Euclidean inner product $\operatorname{Re}K$, and its order-unit norm is the maximum norm of the coordinates.**

**Definition.** The **dual cone** of $\mathcal{C}_{+}$ with respect to a real bilinear form $g$ is
$$
\mathcal{C}_{+}^{\ast}=\bigl\{Q_{\pm,2}: g(Q_{\pm,1},Q_{\pm,2})\ge0\ \text{for every}\ Q_{\pm,1}\succeq0\bigr\};
$$
the cone is **self-dual** for $g$ when $\mathcal{C}_{+}^{\ast}=\mathcal{C}_{+}$.

**Theorem (the self-duality for the Euclidean inner product).** The Hermitian form $\langle Q_{\pm,1},Q_{\pm,2}\rangle_{\natural*}=Q_{1+}\bar Q_{2+}+Q_{1-}\bar Q_{2-}$ of the quaternionic sesquilinear product is positive definite, and its real part is the Euclidean product of the coordinate quadruples,
$$
\operatorname{Re}\langle Q_{\pm,1},Q_{\pm,2}\rangle_{\natural*}=q_{1+}q_{2+}+q'_{1+}q'_{2+}+q_{1-}q_{2-}+q'_{1-}q'_{2-}.
$$
For the Euclidean inner product $\operatorname{Re}K$ the dual cone is the cone itself,
$$
\mathcal{C}_{+}^{\ast}=\mathcal{C}_{+},
$$
so the cone is self-dual, equivalently autopolar.

*Proof.* The quadratic form $\langle Q_\pm,Q_\pm\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}$ is the sum of the four squares of the real coordinates, so $\operatorname{Re}K$ is a positive definite symmetric bilinear form, and it has the identity Gram matrix in the real basis $1,i,j,ij$; its pairing is the Euclidean product of the coordinate quadruples. If $Q_{\pm,2}$ is non-negative then $\operatorname{Re}\langle Q_{\pm,1},Q_{\pm,2}\rangle_{\natural*}\ge0$ for every non-negative $Q_{\pm,1}$, so $\mathcal{C}_{+}\subseteq\mathcal{C}_{+}^{\ast}$. Conversely if some coordinate $w_{k}$ of $Q_{\pm,2}$ is negative, testing on the corresponding basis vector $e_{k}\succeq0$ gives $\operatorname{Re}\langle e_{k},Q_{\pm,2}\rangle_{\natural*}=w_{k}<0$, so $Q_{\pm,2}\notin\mathcal{C}_{+}^{\ast}$; hence $\mathcal{C}_{+}^{\ast}\subseteq\mathcal{C}_{+}$. The autopolarity is the finite-dimensional case of *Positive Definite Forms on an Ordered Space*. The form $\langle\cdot,\cdot\rangle_{\natural*}$ and its real part are distinguished throughout: $\langle\cdot,\cdot\rangle_{\natural*}$ is the Hermitian two-variable form of *The Four Products, Their Forms and Their Algebraic Norms*, of which only the quadratic form $\langle Q_\pm\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}$ is real-valued on a single element, and $\operatorname{Re}K$ is the inner product that defines the orthogonality of the space.

**Remark (the other three forms).** The self-duality is a statement about the real part of $\langle\cdot,\cdot\rangle_{\natural*}$ alone. The form $\langle\cdot,\cdot\rangle_{*}$ is indefinite of signature $(2,2)$, so its positive set is not a cone; the forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are complex-valued, so they define no sign, and their real parts are indefinite quadrics of signature $(2,2)$ (*The Four Products, Their Forms and Their Algebraic Norms*). The coordinatewise order is therefore attached to the Euclidean inner product and to no other of the four.

**Definition.** An **order unit** of $\mathcal{C}_{+}$ is a non-negative element $u$ such that every $Q_\pm$ satisfies $-\lambda u\preceq Q_\pm\preceq\lambda u$ for some $\lambda>0$.

**Theorem (the order unit and the order-unit norm).** The element
$$
u=1+i+j+ij
$$
is an order unit, the order interval it defines is the cube
$$
[-u,u]=\bigl\{Q_\pm:\ \max\bigl(|q_+|,|q'_+|,|q_-|,|q'_-|\bigr)\le1\bigr\},
$$
and the order-unit norm is the maximum norm of the coordinates,
$$
\lVert Q_\pm\rVert_{u}=\inf\{\lambda>0: -\lambda u\preceq Q_\pm\preceq\lambda u\}=\max\bigl(|q_+|,|q'_+|,|q_-|,|q'_-|\bigr).
$$

*Proof.* The element $u$ has all four coordinates equal to $1$, and $-\lambda u\preceq Q_\pm\preceq\lambda u$ is the four coordinate inequalities $|q_+|,|q'_+|,|q_-|,|q'_-|\le\lambda$; the least such $\lambda$ is the maximum of the four moduli, which is finite for every $Q_\pm$, so $u$ is an order unit and the norm is the displayed maximum. The order interval is the cube of side two. The vocabulary and the norm are those of *Ordered Vector Spaces and the Order Unit*.

**Remark (the cube against the Euclidean ball).** The order-unit norm $\lVert\cdot\rVert_{u}$ and the Euclidean norm $\lVert Q_\pm\rVert=\sqrt{\langle Q_\pm\rangle_{\natural*}}$ of *The Euclidean Topology of the Reduced Biquaternion Algebra* are two norms on the same space, equivalent as all norms of a finite-dimensional space are; the unit ball of the first is the cube and the unit ball of the second is the round ball, and both are compatible with the order topology of the cone, which is the Euclidean topology.

## The Multiplication Operators That Preserve the Cone

**The multiplications that carry the cone into itself are exactly those by the elements of the split-complex orthant, and they are fewer than the non-negative elements.**

**Definition.** A linear map $S$ of $\mathbb{B}_{\mathrm{r}}$ is **positive** for the cone $\mathcal{C}_{+}$ when $X\succeq0$ implies $SX\succeq0$, that is $S(\mathcal{C}_{+})\subseteq\mathcal{C}_{+}$.

**Theorem (the general ordered-algebra statement).** In an ordered algebra $A$ whose cone is closed under the involutive congruences, the left and the right multiplications by a positive element are positive operators, $a\succeq0\implies L_{a}\succeq0$ and $R_{a}\succeq0$.

The statement is that of *The Left and Right Multiplication Operators on an Ordered Algebra* and *Ordered Involutive Algebras*, and it is proved there from the congruence axiom of the ordered involutive algebra. The cone of those articles is the cone generated by the involutive squares $c^{\ast}c$, not the coordinatewise cone, and the two orders differ; the theorem is quoted here to mark the difference, and the positive multiplications for the coordinatewise order are computed from the matrix of the operator and not from the axioms.

**Theorem (the cone-preserving elements).** For the coordinatewise cone, the left multiplication $L_{Q_\pm}$ carries $\mathcal{C}_{+}$ into itself if and only if
$$
Q_\pm\in\mathcal{O}=\{h_{0}+h_{2}j:\ h_{0},h_{2}\ge0\},
$$
that is if and only if $q_+\ge0$, $q'_+=0$, $q_-\ge0$ and $q'_-=0$; and the same condition characterises the right multiplications, the two coinciding because the algebra is commutative. Equivalently, the matrix of $L_{Q_\pm}$ in the basis $1,i,j,ij$ is entrywise non-negative exactly for those $Q_\pm$.

*Proof.* The cone is generated by the four basis vectors, so $L_{Q_\pm}(\mathcal{C}_{+})\subseteq\mathcal{C}_{+}$ holds if and only if the four images of the basis vectors are non-negative. In the basis $1,i,j,ij$ the operator has the columns
$$
L_{Q_\pm}(1)=Q_\pm=(q_+,q'_+,q_-,q'_-),\qquad L_{Q_\pm}(i)=(-q'_+,q_+,-q'_- ,q_-),\qquad L_{Q_\pm}(j)=(q_-,q'_- ,q_+,q'_+),\qquad L_{Q_\pm}(ij)=(-q'_- ,q_-,-q'_+,q_+),
$$
computed from the multiplication table. The four columns are non-negative if and only if $q_+,q'_+,q_-,q'_- \ge0$ from the first, $-q'_+\ge0$ and $-q'_-\ge0$ from the second, and these together with the first row give $q_+\ge0$, $q_-\ge0$, $q'_+=0$, $q'_-=0$; the third and the fourth columns are then automatic. The form $Q_\pm=h_{0}+h_{2}j$ with $h_{0}=q_+$ and $h_{2}=q_-$ is the same statement. The word *positive* for the operator and for the element is thus attached to two different cones, and the theorem separates them.

**Corollary (the positivity-preserving elements form a proper subcone).** The set $\mathcal{O}$ is a closed convex cone of real dimension two, pointed and simplicial with extreme rays $\mathbb{R}_{+}1$ and $\mathbb{R}_{+}j$, and it is a **proper** subcone of $\mathcal{C}_{+}$:
$$
\mathcal{O}\subsetneq\mathcal{C}_{+}.
$$

*Proof.* $\mathcal{O}$ is generated by the two independent rays $1$ and $j$, hence simplicial of dimension two; it is contained in $\mathcal{C}_{+}$ because $h_{0}+h_{2}j$ has coordinates $(h_{0},0,h_{2},0)$; and it is proper because $i\in\mathcal{C}_{+}$ and $i\notin\mathcal{O}$. The element $i$ is non-negative and its multiplication does **not** preserve the cone, $i^{2}=-1\notin\mathcal{C}_{+}$, which is the same failure as in §*The Cone and the Multiplication*.

**Corollary (the multiplicative core).** The orthant $\mathcal{O}$ is exactly the set of the elements $h$ with $h\,\mathcal{C}_{+}\subseteq\mathcal{C}_{+}$; it is the **multiplicative core** of the cone, and the elements of $\mathcal{C}_{+}\setminus\mathcal{O}$ are non-negative but not positivity-preserving.

*Proof.* The condition $h\mathcal{C}_{+}\subseteq\mathcal{C}_{+}$ is the condition on the right multiplication $R_{h}=L_{h}$ of the theorem. The core is smaller than the cone, so the cone is not multiplicatively closed and the algebra is not ordered by $\mathcal{C}_{+}$.

## The Two Complex Coordinates

**In the idempotent coordinates the cone is the image of the orthant under the isomorphism, a simplicial cone with four facets, and on the split-complex plane its trace is not the forward cone of the split-complex algebra.**

**Theorem (the cone in the idempotent coordinates).** Writing $Q_{++}=Q_++Q_-=u_1+iu_2$ and $Q_{--}=Q_+-Q_-=v_1+iv_2$, one has
$$
Q_\pm\in\mathcal{C}_{+}\iff u_1+v_1\ge0,\quad u_2+v_2\ge0,\quad u_1-v_1\ge0,\quad u_2-v_2\ge0,
$$
so $\varphi(\mathcal{C}_{+})$ is a simplicial cone of $\mathbb{C}\oplus\mathbb{C}$ with the four facets above, and the cone is **not** a coordinatewise orthant in the idempotent coordinates.

*Proof.* The isomorphism reads $Q_+=\tfrac12(Q_{++}+Q_{--})$ and $Q_-=\tfrac12(Q_{++}-Q_{--})$, so $q_+=\tfrac12(u_1+v_1)$, $q'_+=\tfrac12(u_2+v_2)$, $q_-=\tfrac12(u_1-v_1)$ and $q'_-=\tfrac12(u_2-v_2)$; the four non-negativity conditions are the four displayed inequalities. They are four independent real linear inequalities, so the image is a simplicial cone with four facets, and it is not the coordinatewise orthant of $\mathbb{C}^{2}$, which would impose the four separate inequalities $u_1,u_2,v_1,v_2\ge0$.

**Remark (the split-complex plane).** On the plane $\mathbb{R}\{1,j\}$, on which $q'_+=q'_-=0$, the cone is $\{q_+\ge0,\ q_-\ge0\}$, and in the idempotent coordinates $u=q_++q_-$, $v=q_+-q_-$ it is
$$
\{q_+\ge0,\ q_-\ge0\}=\{u\ge|v|\}.
$$
The **forward cone** of the split-complex algebra, the image of its squaring map on which a square root exists, is the cone on the two idempotents, $\{q_+\ge|q_-|\}=\{u\ge0,\ v\ge0\}$ (*The Classes of Element of the Split-Complex Algebra*). The two cones are different: the coordinatewise cone is the cone on the coordinate axes $1$ and $j$, the forward cone is the cone on the idempotents $\Pi_+$ and $\Pi_-$, and the coordinatewise cone strictly contains the forward cone. The null cone of the plane is the pair of idempotent rays, and the coordinatewise cone meets it along the first ray alone, in agreement with the general computation of §*The Null Cone Inside the Cone*. The hyperbolic reading of the plane is *Reduced Biquaternions and Hyperbolic Geometry*.

**Remark (the two orders of the split-complex companion).** The distinction is not special to the reduced biquaternion algebra: on the split-complex algebra the cone of squares and the coordinatewise cone are likewise different, and the Hermitian form selects a third cone, the Hermitian cone, which for the split-complexoid algebra is the ray of the non-negative reals (*The Hermitian Form and the Cone of the Split-Complexoid Algebra*). The three notions of positivity — the cone of the form, the cone of the squares and the coordinatewise cone — coincide in the field $\mathbb{C}$ and separate in the split algebras.

## Worked Examples

**A non-negative element whose square leaves the cone.** For $Q_\pm=1+2i$ the coordinates are $(1,2,0,0)$, so $Q_\pm\succeq0$; the square is $(1+2i)^{2}=-3+4i$, whose coordinates $(-3,4,0,0)$ are not all non-negative. The element is a unit, $\langle Q_\pm\rangle_{\natural}=1^{2}-(2i)^{2}=1+4=5\neq0$, so the failure is not caused by a zero divisor: the cone is not multiplicative even on its units.

**The two idempotents.** For $\Pi_+=\tfrac12(1+j)$ the coordinates are $\bigl(\tfrac12,0,\tfrac12,0\bigr)$, all non-negative, and $\Pi_+\succeq0$; it is a zero divisor, $\Pi_+\Pi_-=0$, and it lies on the boundary of the cone. For $\Pi_-=\tfrac12(1-j)$ the coordinates are $\bigl(\tfrac12,0,-\tfrac12,0\bigr)$, and the fourth is negative, so $\Pi_-\not\succeq0$ although $\Pi_-$ is the reflection of $\Pi_+$ under the natural sign.

**A strictly positive zero divisor.** For $Q_\pm=(1+i)(1+j)=1+i+j+ij$ the coordinates are $(1,1,1,1)$, all strictly positive, so $Q_\pm$ is an interior point of the cone; the idempotent coordinates are $Q_{++}=2(1+i)$ and $Q_{--}=0$, so $\langle Q_\pm\rangle_{\natural}=0$ and $Q_\pm$ is a zero divisor. The example shows that the interior of the cone is not the set of the units.

**The cone-preserving elements.** For $h=1+j$ the coordinates are $(1,0,1,0)$, so $h\in\mathcal{O}$ and $h$ preserves the cone: $h\cdot i=1\cdot i+j\cdot i=i+ij$, of coordinates $(0,1,0,1)$, non-negative, as the theorem predicts. For $h=i$ the coordinates are $(0,1,0,0)$, so $h\in\mathcal{C}_{+}\setminus\mathcal{O}$, and $h\cdot i=-1$ leaves the cone; the element is non-negative but not positivity-preserving.

**A generic positivity-preserving element.** For $h=2+3j$ the coordinates are $(2,0,3,0)$, so $h\in\mathcal{O}$; multiplying the basis vector $ij$ gives $h\,ij=2ij+3j\,ij=2ij+3i$, of coordinates $(0,3,0,2)$, non-negative, and the same holds on the other three basis vectors, so the whole cone is carried into itself.

## Verification

The following identities were checked by recomputation on random elements and matrices of at most a few dozen entries, the deviations found at the level of the floating-point noise.

- The four columns of the matrix of $L_{Q_\pm}$ in the basis $1,i,j,ij$ agree with the products $Q_\pm\cdot1$, $Q_\pm\cdot i$, $Q_\pm\cdot j$ and $Q_\pm\cdot ij$, and the matrix is entrywise non-negative exactly when $Q_\pm=h_{0}+h_{2}j$ with $h_{0},h_{2}\ge0$.
- The square of the non-negative element $1+2i$ is $-3+4i$, outside the cone; the product of the two non-negative elements $i$ and $i$ is $-1$, outside the cone.
- An element $q\Pi_+$ is non-negative exactly when $\operatorname{Re}q\ge0$ and $\operatorname{Im}q\ge0$; the element $q\Pi_-$ is non-negative only for $q=0$; the element $(1+i)(1+j)=2(1+i)\Pi_+$ is strictly positive and of norm $0$.
- The Euclidean pairing $\langle Q_{\pm,1},Q_{\pm,2}\rangle_{\natural*}=\sum_{k}t_{k}w_{k}$ is non-negative on pairs of non-negative elements, and negative on a pair with a negative coordinate, which is the self-duality.
- The condition $h\mathcal{C}_{+}\subseteq\mathcal{C}_{+}$ holds exactly for the elements of $\mathcal{O}$.
- On the split-complex plane the coordinatewise cone is $\{q_+\ge0,q_-\ge0\}=\{u\ge|v|\}$ in the idempotent coordinates, distinct from the forward cone $\{u\ge0,v\ge0\}$.

## Summary

The reduced biquaternion algebra carries the **coordinatewise cone** $\mathcal{C}_{+}=\mathbb{R}_{+}^{4}$ of the non-negative elements, the positive orthant of the four real coordinates, with its **coordinatewise order** $Q_{\pm,1}\succeq Q_{\pm,2}\iff Q_{\pm,1}-Q_{\pm,2}\in\mathcal{C}_{+}$. The cone is closed, pointed, generating and **simplicial**, with the four coordinate rays as extreme rays, with nonempty interior, and it is **self-dual** for the Euclidean inner product $\operatorname{Re}K$; the element $u=1+i+j+ij$ is an order unit, the order interval $[-u,u]$ is the cube, and the order-unit norm is the maximum norm of the coordinates. The cone is **not compatible with the multiplication**: the product of two non-negative elements need not be non-negative and neither need the square of one, the witness being $(1+2i)^{2}=-3+4i$, so the algebra is not an ordered algebra for this order.

The cone meets the null cone, and it meets it in the interior: the first idempotent ray $\mathbb{R}_{+}\Pi_+$ lies in $\mathcal{C}_{+}$, the second does not, and the strictly positive element $(1+i)(1+j)=2(1+i)\Pi_+$ is a zero divisor. The multiplications that preserve the cone are exactly those by the elements of the **split-complex orthant** $\mathcal{O}=\{h_{0}+h_{2}j:h_{0},h_{2}\ge0\}$, equivalently the elements whose left multiplication matrix is entrywise non-negative; $\mathcal{O}$ is a proper subcone of $\mathcal{C}_{+}$ of dimension two, and the general ordered-algebra statement that a positive element gives a positive multiplication holds for the other cone of the algebra, generated by the involutive squares, and not for this one. In the idempotent coordinates the cone is the image of the orthant under $\varphi$, a simplicial cone cut by four inequalities and not a coordinatewise orthant; on the split-complex plane its trace is the cone on the coordinate axes, strictly larger than the forward cone of the split-complex algebra, and it meets the null cone along one idempotent ray alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}_{+}=\mathbb{R}_{+}^{4}$ | The coordinatewise cone, the set of the non-negative elements $q_+,q'_+,q_-,q'_-\ge0$ |
| $Q_{\pm,1}\succeq Q_{\pm,2}$ | The coordinatewise order, $Q_{\pm,1}-Q_{\pm,2}\in\mathcal{C}_{+}$ |
| $\mathcal{N}=\{Q_\pm\neq0:\langle Q_\pm\rangle_{\natural}=0\}$ | The null cone, the zero divisors of the product |
| $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-)$ | The reduced norm, vanishing on the two idempotent lines |
| $\mathbb{C}^{\times}\Pi_+,\mathbb{C}^{\times}\Pi_-$ | The two idempotent lines, the components of the null cone |
| $\mathcal{O}=\{h_{0}+h_{2}j:h_{0},h_{2}\ge0\}$ | The split-complex orthant, the multiplicative core of the cone |
| $\langle Q_\pm\rangle_{\natural*}=q_+^{2}+(q'_+)^{2}+q_-^{2}+(q'_-)^{2}$ | The positive definite form, the Euclidean norm and the self-duality |
| $u=1+i+j+ij$ | The order unit, whose order interval is the cube |
| $\lVert Q_\pm\rVert_{u}=\max(\lvert q_+\rvert,\lvert q'_+\rvert,\lvert q_-\rvert,\lvert q'_-\rvert)$ | The order-unit norm, the maximum norm of the coordinates |
| $\varphi(Q_\pm)=(Q_{++},Q_{--})=(Q_++Q_-,Q_+-Q_-)$ | The isomorphism with $\mathbb{C}\oplus\mathbb{C}$, in which $\mathcal{C}_{+}$ is simplicial |
| $q\Pi_+,\ q\in\mathbb{C}$ | The parametrisation of the intersection $\mathcal{C}_{+}\cap\mathcal{N}$ |
| $(1+i)(1+j)=2(1+i)\Pi_+$ | The strictly positive zero divisor of the interior |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), for the algebra, the basis, the idempotents and the isomorphism with $\mathbb{C}\oplus\mathbb{C}$.
- *The Four-Vector Element Representation of the Reduced Biquaternions* (`articles_maths/the-four-vector-element-representation-of-the-reduced-biquaternions.md`), for the four real coordinates used to define the cone.
- *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* (`articles_maths/reduced-biquaternions-as-a-vector-space-over-r-and-c.md`), for the change between the real and the complex readings.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the forms $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$, the positive definiteness of $\langle\cdot,\cdot\rangle_{\natural*}$ and the Euclidean inner product $\operatorname{Re}K$ of the self-duality.
- *The Euclidean Topology of the Reduced Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-reduced-biquaternion-algebra.md`), for the Euclidean norm $\sqrt{K}$ and the Cauchy–Schwarz inequality used on the cone.
- *Zero Divisors of the Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the null cone and the two idempotent lines.
- *The Multiplication Operators of the Algebra of the Reduced Biquaternions* (`articles_maths/the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the matrix of $L_{Q_\pm}$ whose entrywise sign characterises the cone-preserving elements.
- *The Classes of Element of the Split-Complex Algebra* (`articles_maths/the-classes-of-element-of-the-split-complex-algebra.md`), for the forward cone $\{h_{0}\ge|h_{2}|\}$ of the split-complex companion, compared here with the coordinatewise cone.
- *The Hermitian Form and the Cone of the Split-Complexoid Algebra* (`articles_maths/the-hermitian-form-and-the-cone-of-the-split-complexoid-algebra.md`), for the third notion of positivity, the cone of the form.
- *Reduced Biquaternions and Hyperbolic Geometry* (`articles_maths/reduced-biquaternions-and-hyperbolic-geometry.md`), for the hyperbolic reading of the split-complex plane and the null cone.
- *Ordered Vector Spaces and the Order Unit* (`articles_maths/ordered-vector-spaces-and-the-order-unit.md`), for the positive cone, the generating and pointed cases, the order unit and the order-unit norm.
- *Positive Definite Forms on an Ordered Space* (`articles_maths/positive-definite-forms-on-an-ordered-space.md`), for the self-dual cone and the autopolarity in finite dimension.
- *Positive Operators on an Ordered Space* and *The Cone of Positive Operators* (`articles_maths/positive-operators-on-an-ordered-space.md`, `articles_maths/the-cone-of-positive-operators.md`), for the definition of a positive operator and for the cone of the non-negative matrices.
- *Ordered Involutive Algebras* and *The Left and Right Multiplication Operators on an Ordered Algebra* (`articles_maths/ordered-involutive-algebras.md`, `articles_maths/the-left-and-right-multiplication-operators-on-an-ordered-algebra.md`), for the order of an algebra under its involution and for the general statement that a positive element gives a positive multiplication, which holds there and not for the coordinatewise cone here.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra of the engineering literature.
- J. F. Miao, J. J. Pan and M. K. Ng, "Non-negative reduced biquaternion matrix factorization with applications in color face recognition", arXiv:2408.05582v2 (2025), for the non-negativity of the four coefficient matrices and the product that keeps one; the matrix reading of the cone is the subject of *Non-Negative Matrix Factorization over the Reduced Biquaternions*.
